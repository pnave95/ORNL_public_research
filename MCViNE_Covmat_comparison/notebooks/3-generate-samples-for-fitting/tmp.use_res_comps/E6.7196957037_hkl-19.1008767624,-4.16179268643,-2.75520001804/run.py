#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E6.7196957037_hkl-19.1008767624,-4.16179268643,-2.75520001804/sample/sampleassembly.xml'
psi = -0.003425717616590427
hkl2Q = array([[ -6.57475884e-01,   9.36601214e-01,  -7.76121684e-17],
       [  6.62277069e-01,   4.64905656e-01,  -8.09165116e-01],
       [ -6.62277069e-01,  -4.64905656e-01,  -8.09165116e-01]])
pp = array([ 1.47402277,  2.612902  , -0.78863852])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001206747705260292
Q = array([ 11.62681176, -18.54383725,   5.59698921])
E = 6.7196957036981075
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
