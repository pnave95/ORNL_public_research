#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E331.210290919_hkl-6.48892756381,1.19675734911,-3.80108139748/sample/sampleassembly.xml'
psi = -0.009539881989707134
hkl2Q = array([[ -6.51737097e-01,   9.40603598e-01,   7.72819191e-17],
       [  6.65107182e-01,   4.60847721e-01,  -8.09165116e-01],
       [ -6.65107182e-01,  -4.60847721e-01,  -8.09165116e-01]])
pp = array([ 2.71316614,  1.2801287 , -0.70985854])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0019257715667395491
Q = array([ 7.55317326, -3.80026602,  2.10732817])
E = 331.21029091859532
hkl_projection = array([ 0.12397226,  0.16246175,  0.90679696])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
