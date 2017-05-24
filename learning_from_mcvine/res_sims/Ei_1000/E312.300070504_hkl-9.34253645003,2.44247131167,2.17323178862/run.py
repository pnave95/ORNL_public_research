#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E312.300070504_hkl-9.34253645003,2.44247131167,2.17323178862/sample/sampleassembly.xml'
psi = -0.004000799436106105
hkl2Q = array([[ -6.56937153e-01,   9.36979161e-01,   7.75808621e-17],
       [  6.62544319e-01,   4.64524716e-01,  -8.09165116e-01],
       [ -6.62544319e-01,  -4.64524716e-01,  -8.09165116e-01]])
pp = array([ 2.63188161,  1.43986082,  0.62323306])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012479865264064431
Q = array([ 6.31584241, -8.62869355, -3.73486594])
E = 312.30007050384506
hkl_projection = array([-0.76186461, -0.27043949, -0.86031889])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
