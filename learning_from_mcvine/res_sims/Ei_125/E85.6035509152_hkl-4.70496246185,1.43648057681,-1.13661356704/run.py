#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E85.6035509152_hkl-4.70496246185,1.43648057681,-1.13661356704/sample/sampleassembly.xml'
psi = -0.007205446279699697
hkl2Q = array([[ -6.53931097e-01,   9.39079598e-01,   7.74073372e-17],
       [  6.64029552e-01,   4.62399113e-01,  -8.09165116e-01],
       [ -6.64029552e-01,  -4.62399113e-01,  -8.09165116e-01]])
pp = array([ 2.04906318,  2.19119604,  0.16468013])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0038617015941487384
Q = array([ 4.78533182, -3.22853781, -0.24264192])
E = 85.603550915220268
hkl_projection = array([ 0.26408905, -0.33873542,  0.05713784])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
