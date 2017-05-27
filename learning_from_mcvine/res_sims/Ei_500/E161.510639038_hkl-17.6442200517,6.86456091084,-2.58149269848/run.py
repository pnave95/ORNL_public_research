#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E161.510639038_hkl-17.6442200517,6.86456091084,-2.58149269848/sample/sampleassembly.xml'
psi = -0.006978829275396796
hkl2Q = array([[-0.65414389,  0.93893138,  0.        ],
       [ 0.66392475,  0.46254958, -0.80916512],
       [-0.66392475, -0.46254958, -0.80916512]])
pp = array([-0.53383793,  2.95212077,  0.8387981 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017751659775038331
Q = array([ 17.81332753, -12.19744377,  -3.46570939])
E = 161.51063903775298
hkl_projection = array([-0.12135061, -0.05049661, -0.18247122])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
