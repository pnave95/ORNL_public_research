#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E10.9791531651_hkl-0.137624844866,1.03424847181,0.217489427841/sample/sampleassembly.xml'
psi = 0.01168742416068707
hkl2Q = array([[ -6.71555247e-01,   9.26558105e-01,  -7.84534189e-17],
       [  6.55175519e-01,   4.74861269e-01,  -8.09165116e-01],
       [ -6.55175519e-01,  -4.74861269e-01,  -8.09165116e-01]])
pp = array([ 2.99555925, -0.163171  ,  0.6348478 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050163700109830574
Q = array([ 0.62754322,  0.26032982, -1.01286264])
E = 10.979153165142549
hkl_projection = array([-0.55126464, -0.68604891, -0.02889761])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
