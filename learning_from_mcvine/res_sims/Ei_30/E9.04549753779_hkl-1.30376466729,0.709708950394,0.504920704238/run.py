#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E9.04549753779_hkl-1.30376466729,0.709708950394,0.504920704238/sample/sampleassembly.xml'
psi = -0.0032794237173262206
hkl2Q = array([[ -6.57612896e-01,   9.36505019e-01,   7.76201405e-17],
       [  6.62209050e-01,   4.65002538e-01,  -8.09165116e-01],
       [ -6.62209050e-01,  -4.65002538e-01,  -8.09165116e-01]])
pp = array([ 2.78702392,  1.11017911,  0.96923739])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0072544266693021697
Q = array([ 0.99298509, -1.1257551 , -0.98283595])
E = 9.0454975377886413
hkl_projection = array([ 0.65853747,  0.19140402, -0.06770808])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
