#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E19.3663441471_hkl-5.06957046146,0.828359436655,-0.291794484501/sample/sampleassembly.xml'
psi = -0.004606988107729085
hkl2Q = array([[ -6.56369046e-01,   9.37377217e-01,   7.75479175e-17],
       [  6.62825787e-01,   4.64123003e-01,  -8.09165116e-01],
       [ -6.62825787e-01,  -4.64123003e-01,  -8.09165116e-01]])
pp = array([ 0.90359059,  2.86068594,  0.29346909])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050944266405925816
Q = array([ 4.06997603, -4.23221065, -0.43416964])
E = 19.366344147148538
hkl_projection = array([-0.2860197 ,  0.84779684, -0.40465751])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
