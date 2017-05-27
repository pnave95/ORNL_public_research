#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-830.023239444_hkl1.80360781544,-5.85668813198,3.79523099462/sample/sampleassembly.xml'
psi = 0.014275754189641682
hkl2Q = array([[ -6.73951233e-01,   9.24816796e-01,   7.86011364e-17],
       [  6.53944228e-01,   4.76555487e-01,  -8.09165116e-01],
       [ -6.53944228e-01,  -4.76555487e-01,  -8.09165116e-01]])
pp = array([ 2.98540818,  0.29553004, -0.16815054])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011430619186463204
Q = array([-7.52736051, -2.93166822,  1.6680592 ])
E = -830.02323944437398
hkl_projection = array([ 0.84136571,  0.07226524,  0.93981018])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
