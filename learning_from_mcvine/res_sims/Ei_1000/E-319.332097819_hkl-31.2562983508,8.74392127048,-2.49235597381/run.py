#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-319.332097819_hkl-31.2562983508,8.74392127048,-2.49235597381/sample/sampleassembly.xml'
psi = -0.006338160904265784
hkl2Q = array([[ -6.54745301e-01,   9.38512100e-01,  -7.74541438e-17],
       [  6.63628270e-01,   4.62974843e-01,  -8.09165116e-01],
       [ -6.63628270e-01,  -4.62974843e-01,  -8.09165116e-01]])
pp = array([-0.70490305,  2.91600955,  0.61124616])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011748717995694867
Q = array([ 27.92162571, -24.13230051,  -5.05854856])
E = -319.3320978191806
hkl_projection = array([ 0.64615995,  0.71379008, -0.8338966 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
