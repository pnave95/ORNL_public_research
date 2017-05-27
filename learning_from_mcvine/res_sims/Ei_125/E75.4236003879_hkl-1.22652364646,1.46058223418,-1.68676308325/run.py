#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E75.4236003879_hkl-1.22652364646,1.46058223418,-1.68676308325/sample/sampleassembly.xml'
psi = 0.036835888839959356
hkl2Q = array([[ -6.94641955e-01,   9.09378318e-01,  -7.99355446e-17],
       [  6.43027575e-01,   4.91186037e-01,  -8.09165116e-01],
       [ -6.43027575e-01,  -4.91186037e-01,  -8.09165116e-01]])
pp = array([ 2.9886178 , -0.26108166, -0.11097819])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0037468446818508063
Q = array([ 2.87582461,  0.43055806,  0.18301765])
E = 75.423600387934982
hkl_projection = array([ 0.30915071,  0.83822649,  0.69534994])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
