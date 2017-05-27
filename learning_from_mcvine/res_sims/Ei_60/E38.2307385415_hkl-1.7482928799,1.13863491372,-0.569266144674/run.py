#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E38.2307385415_hkl-1.7482928799,1.13863491372,-0.569266144674/sample/sampleassembly.xml'
psi = -0.012777080999493776
hkl2Q = array([[ -6.48688766e-01,   9.42708468e-01,  -7.71093647e-17],
       [  6.66595551e-01,   4.58692225e-01,  -8.09165116e-01],
       [ -6.66595551e-01,  -4.58692225e-01,  -8.09165116e-01]])
pp = array([ 2.89194923,  0.79789074,  0.42510274])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.005486366143210665
Q = array([ 2.2725772 , -0.86472957, -0.46071335])
E = 38.230738541483788
hkl_projection = array([-0.39606992, -0.12016727, -0.84225994])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
