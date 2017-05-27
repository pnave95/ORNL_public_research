#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E160.684791297_hkl-20.7199037032,0.471906144918,-0.89279301518/sample/sampleassembly.xml'
psi = -0.00422353546598823
hkl2Q = array([[ -6.56728438e-01,   9.37125462e-01,  -7.75687505e-17],
       [  6.62647769e-01,   4.64377132e-01,  -8.09165116e-01],
       [ -6.62647769e-01,  -4.64377132e-01,  -8.09165116e-01]])
pp = array([ 1.1222069 ,  2.78220267, -0.05044484])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012182087366316779
Q = array([ 14.51166484, -18.78341424,   0.34056697])
E = 160.68479129726711
hkl_projection = array([ 0.50335888,  0.53272476,  0.57269005])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
