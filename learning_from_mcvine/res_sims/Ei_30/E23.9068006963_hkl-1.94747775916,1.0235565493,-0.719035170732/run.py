#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E23.9068006963_hkl-1.94747775916,1.0235565493,-0.719035170732/sample/sampleassembly.xml'
psi = -0.008872646050796911
hkl2Q = array([[ -6.52364556e-01,   9.40168526e-01,   7.73176820e-17],
       [  6.64799540e-01,   4.61291401e-01,  -8.09165116e-01],
       [ -6.64799540e-01,  -4.61291401e-01,  -8.09165116e-01]])
pp = array([ 2.41286317,  1.7827202 ,  0.42768023])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0084448147773422792
Q = array([ 2.42893964, -1.02711472, -0.24640808])
E = 23.906800696273699
hkl_projection = array([ 0.26188929,  0.15386079,  0.50069457])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
