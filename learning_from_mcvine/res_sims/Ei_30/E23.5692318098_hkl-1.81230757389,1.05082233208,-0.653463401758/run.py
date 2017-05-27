#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E23.5692318098_hkl-1.81230757389,1.05082233208,-0.653463401758/sample/sampleassembly.xml'
psi = -0.009463209785693677
hkl2Q = array([[-0.65180921,  0.94055362,  0.        ],
       [ 0.66507185,  0.46089871, -0.80916512],
       [-0.66507185, -0.46089871, -0.80916512]])
pp = array([ 2.56004375,  1.56402557,  0.5471617 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0083909585092001686
Q = array([ 2.31475123, -0.91906935, -0.32152899])
E = 23.569231809795255
hkl_projection = array([ 0.91528588, -0.35812318, -0.9369535 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
