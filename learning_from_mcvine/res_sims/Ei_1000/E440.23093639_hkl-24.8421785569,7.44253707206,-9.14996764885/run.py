#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E440.23093639_hkl-24.8421785569,7.44253707206,-9.14996764885/sample/sampleassembly.xml'
psi = -0.009531777758672626
hkl2Q = array([[ -6.51744719e-01,   9.40598316e-01,   7.72823530e-17],
       [  6.65103448e-01,   4.60853111e-01,  -8.09165116e-01],
       [ -6.65103448e-01,  -4.60853111e-01,  -8.09165116e-01]])
pp = array([-0.93210715,  2.85152174, -0.25061656])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012710604570978601
Q = array([ 27.22649079, -15.7198039 ,   1.38159326])
E = 440.23093638956266
hkl_projection = array([ 0.19622997, -0.19857756,  0.8667379 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
