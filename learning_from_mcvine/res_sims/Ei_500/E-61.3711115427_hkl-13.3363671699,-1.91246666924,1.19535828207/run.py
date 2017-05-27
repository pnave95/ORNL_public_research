#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-61.3711115427_hkl-13.3363671699,-1.91246666924,1.19535828207/sample/sampleassembly.xml'
psi = -0.0022970909117115265
hkl2Q = array([[ -6.58532538e-01,   9.35858572e-01,   7.76737567e-17],
       [  6.61751943e-01,   4.65652823e-01,  -8.09165116e-01],
       [ -6.61751943e-01,  -4.65652823e-01,  -8.09165116e-01]])
pp = array([ 1.61301285,  2.52946428, -0.10537995])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016792045867449687
Q = array([  6.72582252, -13.928121  ,   0.58025909])
E = -61.371111542697122
hkl_projection = array([ 0.40049063, -0.6787051 ,  0.66311205])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
