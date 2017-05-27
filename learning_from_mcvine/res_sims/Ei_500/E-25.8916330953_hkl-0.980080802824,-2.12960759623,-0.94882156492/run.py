#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-25.8916330953_hkl-0.980080802824,-2.12960759623,-0.94882156492/sample/sampleassembly.xml'
psi = 0.0004275911820951896
hkl2Q = array([[ -6.61080008e-01,   9.34060809e-01,  -7.78232535e-17],
       [  6.60480732e-01,   4.67454156e-01,  -8.09165116e-01],
       [ -6.60480732e-01,  -4.67454156e-01,  -8.09165116e-01]])
pp = array([ 2.98704638,  0.27848503, -0.47273114])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016921813432830858
Q = array([-0.1319746 , -1.46741841,  2.49095749])
E = -25.891633095280099
hkl_projection = array([-0.19008622, -0.68545886,  0.00412979])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
