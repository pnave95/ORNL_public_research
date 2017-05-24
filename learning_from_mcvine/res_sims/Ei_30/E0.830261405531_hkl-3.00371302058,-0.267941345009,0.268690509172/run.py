#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E0.830261405531_hkl-3.00371302058,-0.267941345009,0.268690509172/sample/sampleassembly.xml'
psi = -0.0019709857243286394
hkl2Q = array([[ -6.58837691e-01,   9.35643772e-01,   7.76915887e-17],
       [  6.61600056e-01,   4.65868599e-01,  -8.09165116e-01],
       [ -6.61600056e-01,  -4.65868599e-01,  -8.09165116e-01]])
pp = array([  1.74855510e+00,   2.43773564e+00,   4.82860641e-04])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069532556771775729
Q = array([  1.62392369e+00,  -3.06040531e+00,  -6.06197507e-04])
E = 0.83026140553095473
hkl_projection = array([-0.38971596,  0.72078365,  0.96584626])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
