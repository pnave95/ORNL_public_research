#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E210.624584453_hkl-5.99331494612,2.29807690578,-3.59608100147/sample/sampleassembly.xml'
psi = -0.009725036665542672
hkl2Q = array([[ -6.51562928e-01,   9.40724254e-01,  -7.72720070e-17],
       [  6.65192499e-01,   4.60724565e-01,  -8.09165116e-01],
       [ -6.65192499e-01,  -4.60724565e-01,  -8.09165116e-01]])
pp = array([ 2.21446189,  2.02389687, -0.7273627 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030677760764361429
Q = array([ 7.82577147, -2.92247339,  1.05029964])
E = 210.62458445312188
hkl_projection = array([ 0.81783011,  0.5370921 ,  0.72370879])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
