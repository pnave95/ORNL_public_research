#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-54.2301235437_hkl-6.42649787084,-0.989187992858,1.1063130129/sample/sampleassembly.xml'
psi = -0.0019484496028459302
hkl2Q = array([[ -6.58858777e-01,   9.35628924e-01,  -7.76928216e-17],
       [  6.61589557e-01,   4.65883509e-01,  -8.09165116e-01],
       [ -6.61589557e-01,  -4.65883509e-01,  -8.09165116e-01]])
pp = array([ 1.03145948,  2.81710691,  0.03820062])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046610569670095213
Q = array([ 2.84779295, -6.98907665, -0.09477348])
E = -54.230123543662614
hkl_projection = array([-0.60362517,  0.72578615,  0.74150883])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
