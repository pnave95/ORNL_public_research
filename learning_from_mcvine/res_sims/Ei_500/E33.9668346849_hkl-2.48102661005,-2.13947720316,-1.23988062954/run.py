#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E33.9668346849_hkl-2.48102661005,-2.13947720316,-1.23988062954/sample/sampleassembly.xml'
psi = -0.00180476216466597
hkl2Q = array([[ -6.58993208e-01,   9.35534245e-01,  -7.77006844e-17],
       [  6.61522608e-01,   4.65978566e-01,  -8.09165116e-01],
       [ -6.61522608e-01,  -4.65978566e-01,  -8.09165116e-01]])
pp = array([ 2.94829264,  0.55459041, -0.55341261])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017122026208246607
Q = array([ 1.03987621, -2.74027808,  2.73445847])
E = 33.966834684913465
hkl_projection = array([ 0.54994506,  0.9259243 , -0.85381332])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
