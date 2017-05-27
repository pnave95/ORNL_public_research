#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-233.933736251_hkl-7.87550682916,-0.616466269225,6.07617201999/sample/sampleassembly.xml'
psi = -0.0002662045722657754
hkl2Q = array([[ -6.60431801e-01,   9.34519239e-01,  -7.77850772e-17],
       [  6.60804891e-01,   4.66995805e-01,  -8.09165116e-01],
       [ -6.60804891e-01,  -4.66995805e-01,  -8.09165116e-01]])
pp = array([ 2.09656487,  2.14579024,  0.90409695])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022928978801158044
Q = array([  0.77870705, -10.48524665,  -4.41780344])
E = -233.93373625142704
hkl_projection = array([-0.43077322, -0.75051991, -0.07513412])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
