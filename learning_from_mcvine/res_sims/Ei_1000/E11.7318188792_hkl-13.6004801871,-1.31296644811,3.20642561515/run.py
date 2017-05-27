#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E11.7318188792_hkl-13.6004801871,-1.31296644811,3.20642561515/sample/sampleassembly.xml'
psi = -0.0021967532925722183
hkl2Q = array([[ -6.58626437e-01,   9.35792492e-01,  -7.76792416e-17],
       [  6.61705217e-01,   4.65719220e-01,  -8.09165116e-01],
       [ -6.61705217e-01,  -4.65719220e-01,  -8.09165116e-01]])
pp = array([ 2.20773827,  2.03122912,  0.20982268])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012004662972672159
Q = array([  5.9671305 , -14.83199499,  -1.53212111])
E = 11.731818879186221
hkl_projection = array([ 0.32669546, -0.29638279, -0.88412447])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
