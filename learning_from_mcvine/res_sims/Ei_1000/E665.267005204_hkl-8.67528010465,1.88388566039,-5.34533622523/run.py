#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E665.267005204_hkl-8.67528010465,1.88388566039,-5.34533622523/sample/sampleassembly.xml'
psi = -0.011905807757317326
hkl2Q = array([[ -6.49509876e-01,   9.42142925e-01,  -7.71556514e-17],
       [  6.66195651e-01,   4.59272838e-01,  -8.09165116e-01],
       [ -6.66195651e-01,  -4.59272838e-01,  -8.09165116e-01]])
pp = array([ 2.76886567,  1.15472199, -0.66641897])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0013608521182688574
Q = array([ 10.45075629,  -4.85316852,   2.80088505])
E = 665.26700520447525
hkl_projection = array([-0.80571979, -0.60913797,  0.33436315])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
