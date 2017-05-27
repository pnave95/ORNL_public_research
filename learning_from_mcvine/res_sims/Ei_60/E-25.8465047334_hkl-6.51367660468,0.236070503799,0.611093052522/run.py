#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-25.8465047334_hkl-6.51367660468,0.236070503799,0.611093052522/sample/sampleassembly.xml'
psi = -0.0030784432117204564
hkl2Q = array([[ -6.57801102e-01,   9.36372833e-01,   7.76310980e-17],
       [  6.62115580e-01,   4.65135620e-01,  -8.09165116e-01],
       [ -6.62115580e-01,  -4.65135620e-01,  -8.09165116e-01]])
pp = array([ 0.64020938,  2.93089269,  0.32024542])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004762865706187086
Q = array([ 4.03639538, -6.27366616, -0.6854952 ])
E = -25.846504733371397
hkl_projection = array([ 0.38948923, -0.81366484,  0.02551247])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
