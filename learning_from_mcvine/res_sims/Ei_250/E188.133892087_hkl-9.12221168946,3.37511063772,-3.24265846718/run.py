#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E188.133892087_hkl-9.12221168946,3.37511063772,-3.24265846718/sample/sampleassembly.xml'
psi = -0.006793824555130453
hkl2Q = array([[-0.65431759,  0.93881035,  0.        ],
       [ 0.66383916,  0.4626724 , -0.80916512],
       [-0.66383916, -0.4626724 , -0.80916512]])
pp = array([ 0.35807584,  2.97855362,  0.05801868])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0028276527355816801
Q = array([ 10.36195784,  -5.50216758,  -0.10717568])
E = 188.13389208685334
hkl_projection = array([ 0.33024428, -0.58827799,  0.56093192])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
