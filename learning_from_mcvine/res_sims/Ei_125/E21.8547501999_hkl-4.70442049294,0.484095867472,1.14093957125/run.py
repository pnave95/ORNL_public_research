#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E21.8547501999_hkl-4.70442049294,0.484095867472,1.14093957125/sample/sampleassembly.xml'
psi = -0.0027343902742819003
hkl2Q = array([[ -6.58123225e-01,   9.36146459e-01,  -7.76498703e-17],
       [  6.61955509e-01,   4.65363395e-01,  -8.09165116e-01],
       [ -6.61955509e-01,  -4.65363395e-01,  -8.09165116e-01]])
pp = array([ 2.21250517,  2.02603576,  0.56565818])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034670007450222596
Q = array([ 2.66128708, -4.7096976 , -1.31492199])
E = 21.854750199891839
hkl_projection = array([-0.53690326, -0.90221469, -0.5141364 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
