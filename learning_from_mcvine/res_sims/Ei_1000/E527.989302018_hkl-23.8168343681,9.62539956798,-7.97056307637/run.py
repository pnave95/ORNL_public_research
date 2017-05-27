#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E527.989302018_hkl-23.8168343681,9.62539956798,-7.97056307637/sample/sampleassembly.xml'
psi = -0.010476989926969184
hkl2Q = array([[-0.65085536,  0.94121393,  0.        ],
       [ 0.66553875,  0.46022424, -0.80916512],
       [-0.66553875, -0.46022424, -0.80916512]])
pp = array([-1.01081358,  2.82458066,  0.26414611])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012962646406216298
Q = array([ 27.21210945, -14.31864779,  -1.33903596])
E = 527.98930201770054
hkl_projection = array([ 0.40600306,  0.84458483, -0.18085995])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
