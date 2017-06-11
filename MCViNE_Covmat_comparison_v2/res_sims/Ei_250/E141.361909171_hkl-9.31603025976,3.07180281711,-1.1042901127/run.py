#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_250/E141.361909171_hkl-9.31603025976,3.07180281711,-1.1042901127/sample/sampleassembly.xml'
psi = -0.0046996624470562
hkl2Q = array([[ -6.56282172e-01,   9.37438041e-01,   7.75428859e-17],
       [  6.62868796e-01,   4.64061575e-01,  -8.09165116e-01],
       [ -6.62868796e-01,  -4.64061575e-01,  -8.09165116e-01]])
pp = array([ 0.90163532,  2.86130281,  0.67036899])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0026366379354309456
Q = array([ 8.88214627, -6.7952369 , -1.59204265])
E = 141.36190917062521
hkl_projection = array([-0.78814634, -0.79966767, -0.42044947])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
