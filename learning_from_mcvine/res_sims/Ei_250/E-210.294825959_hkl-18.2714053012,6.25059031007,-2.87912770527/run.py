#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-210.294825959_hkl-18.2714053012,6.25059031007,-2.87912770527/sample/sampleassembly.xml'
psi = -0.005030920749952244
hkl2Q = array([[ -6.55971602e-01,   9.37655389e-01,  -7.75249116e-17],
       [  6.63022484e-01,   4.63841968e-01,  -8.09165116e-01],
       [ -6.63022484e-01,  -4.63841968e-01,  -8.09165116e-01]])
pp = array([-1.4334522 ,  2.63537754,  0.55743164])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002292394960298622
Q = array([ 18.03873133, -12.89753527,  -2.72806993])
E = -210.29482595945822
hkl_projection = array([-0.46289064, -0.75877791, -0.28829818])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
