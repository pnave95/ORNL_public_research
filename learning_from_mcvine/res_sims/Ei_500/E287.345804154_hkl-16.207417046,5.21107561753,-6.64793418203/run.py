#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E287.345804154_hkl-16.207417046,5.21107561753,-6.64793418203/sample/sampleassembly.xml'
psi = -0.009057658284056858
hkl2Q = array([[ -6.52190602e-01,   9.40289205e-01,   7.73077588e-17],
       [  6.64884873e-01,   4.61168397e-01,  -8.09165116e-01],
       [ -6.64884873e-01,  -4.61168397e-01,  -8.09165116e-01]])
pp = array([-0.83939867,  2.88017532, -0.34272537])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018589467173845721
Q = array([ 18.45520131,  -9.77065875,   1.16265583])
E = 287.34580415367327
hkl_projection = array([-0.24254126, -0.62934119,  0.80726031])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
