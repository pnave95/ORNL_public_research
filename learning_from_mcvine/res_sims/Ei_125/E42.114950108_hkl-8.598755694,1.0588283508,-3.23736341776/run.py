#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E42.114950108_hkl-8.598755694,1.0588283508,-3.23736341776/sample/sampleassembly.xml'
psi = -0.006769577452124991
hkl2Q = array([[ -6.54340351e-01,   9.38794481e-01,  -7.74308463e-17],
       [  6.63827943e-01,   4.62688499e-01,  -8.09165116e-01],
       [ -6.63827943e-01,  -4.62688499e-01,  -8.09165116e-01]])
pp = array([-0.33028858,  2.98176281, -0.86384946])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035620762545999158
Q = array([ 8.47844496, -6.08466586,  1.76279458])
E = 42.114950107951813
hkl_projection = array([ 0.82596988, -0.69522679,  0.88102259])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
