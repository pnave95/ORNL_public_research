#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-0.41895468422_hkl0.652299983332,-0.577621263474,-1.33795840058/sample/sampleassembly.xml'
psi = 0.00040163726676460497
hkl2Q = array([[ -6.61055765e-01,   9.34077966e-01,   7.78218240e-17],
       [  6.60492864e-01,   4.67437014e-01,  -8.09165116e-01],
       [ -6.60492864e-01,  -4.67437014e-01,  -8.09165116e-01]])
pp = array([ 2.99712431, -0.13132361, -0.21100073])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001199161665005609
Q = array([ 0.07099059,  0.96470876,  1.55002024])
E = -0.41895468421978421
hkl_projection = array([ 0.23195882, -0.61312319, -0.76061494])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
