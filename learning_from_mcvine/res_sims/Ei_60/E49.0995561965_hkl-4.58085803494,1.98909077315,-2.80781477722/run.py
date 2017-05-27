#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E49.0995561965_hkl-4.58085803494,1.98909077315,-2.80781477722/sample/sampleassembly.xml'
psi = -0.014150849599857287
hkl2Q = array([[ -6.47393091e-01,   9.43598727e-01,   7.70366142e-17],
       [  6.67225058e-01,   4.57776045e-01,  -8.09165116e-01],
       [ -6.67225058e-01,  -4.57776045e-01,  -8.09165116e-01]])
pp = array([-1.0089551 ,  2.82524505, -0.88013317])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006130930288597557
Q = array([ 6.16623143, -2.12658336,  0.6624829 ])
E = 49.099556196487654
hkl_projection = array([ 0.07167012, -0.78285054, -0.86178422])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
