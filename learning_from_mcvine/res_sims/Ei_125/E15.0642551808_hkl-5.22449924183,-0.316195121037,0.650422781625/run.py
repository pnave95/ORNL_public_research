#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E15.0642551808_hkl-5.22449924183,-0.316195121037,0.650422781625/sample/sampleassembly.xml'
psi = -0.0025365879251765884
hkl2Q = array([[-0.65830838,  0.93601626,  0.        ],
       [ 0.66186345,  0.46549432, -0.80916512],
       [-0.66186345, -0.46549432, -0.80916512]])
pp = array([ 2.05149086,  2.18892331,  0.1108549 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00343478099854083
Q = array([ 2.7995626 , -5.3401714 , -0.27044536])
E = 15.064255180846857
hkl_projection = array([ 0.55803179,  0.68350954,  0.79701888])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
