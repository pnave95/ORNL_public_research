#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-2.15679183253_hkl-7.3284214416,2.1942819834,-1.55237331796/sample/sampleassembly.xml'
psi = -0.006796357860913492
hkl2Q = array([[ -6.54315209e-01,   9.38812004e-01,  -7.74294010e-17],
       [  6.63840334e-01,   4.62670722e-01,  -8.09165116e-01],
       [ -6.63840334e-01,  -4.62670722e-01,  -8.09165116e-01]])
pp = array([-1.02717606,  2.81867155,  0.28447186])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048907341115465002
Q = array([ 7.28227852, -5.14654231, -0.5194101 ])
E = -2.1567918325301321
hkl_projection = array([ 0.06860899,  0.43333112,  0.99008335])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
