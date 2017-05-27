#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E456.464624896_hkl-16.9497511524,5.44432998874,0.496564871127/sample/sampleassembly.xml'
psi = -0.005788345133876649
hkl2Q = array([[ -6.55261211e-01,   9.38151969e-01,   7.74838763e-17],
       [  6.63373619e-01,   4.63339646e-01,  -8.09165116e-01],
       [ -6.63373619e-01,  -4.63339646e-01,  -8.09165116e-01]])
pp = array([ 1.47722546,  2.61109267,  0.92233097])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012876880798350036
Q = array([ 14.38873132, -13.60894668,  -4.80716488])
E = 456.46462489625537
hkl_projection = array([-0.96644457,  0.10612237, -0.68698871])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
