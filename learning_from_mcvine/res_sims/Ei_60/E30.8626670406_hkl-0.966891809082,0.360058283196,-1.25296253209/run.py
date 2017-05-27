#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E30.8626670406_hkl-0.966891809082,0.360058283196,-1.25296253209/sample/sampleassembly.xml'
psi = -0.04340994817979434
hkl2Q = array([[ -6.19511087e-01,   9.62134286e-01,  -7.55525005e-17],
       [  6.80331678e-01,   4.38060490e-01,  -8.09165116e-01],
       [ -6.80331678e-01,  -4.38060490e-01,  -8.09165116e-01]])
pp = array([ 2.99456349,  0.18052562, -0.58311679])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0053027142580238914
Q = array([ 1.69638935, -0.22367907,  0.72250697])
E = 30.862667040582082
hkl_projection = array([-0.50670917, -0.11545207,  0.20008224])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
