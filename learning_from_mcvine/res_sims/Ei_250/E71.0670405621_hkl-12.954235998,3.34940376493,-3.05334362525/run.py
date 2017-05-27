#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E71.0670405621_hkl-12.954235998,3.34940376493,-3.05334362525/sample/sampleassembly.xml'
psi = -0.004994990695358945
hkl2Q = array([[-0.65600529,  0.93763182,  0.        ],
       [ 0.66300582,  0.46386579, -0.80916512],
       [-0.66300582, -0.46386579, -0.80916512]])
pp = array([-0.55259693,  2.94866692,  0.07697962])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024782264982130026
Q = array([ 12.74310614,  -9.17628839,  -0.23956154])
E = 71.067040562122315
hkl_projection = array([ 0.67373812,  0.8414818 , -0.46267969])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
