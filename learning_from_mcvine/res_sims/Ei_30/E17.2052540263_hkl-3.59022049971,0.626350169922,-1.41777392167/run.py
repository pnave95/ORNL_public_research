#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E17.2052540263_hkl-3.59022049971,0.626350169922,-1.41777392167/sample/sampleassembly.xml'
psi = -0.005712796534113987
hkl2Q = array([[ -6.55332085e-01,   9.38102462e-01,   7.74879654e-17],
       [  6.63338612e-01,   4.63389761e-01,  -8.09165116e-01],
       [ -6.63338612e-01,  -4.63389761e-01,  -8.09165116e-01]])
pp = array([ 0.13664715,  2.99688631, -0.79279926])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076543900232084339
Q = array([ 3.70873313, -2.42076851,  0.64039249])
E = 17.205254026295471
hkl_projection = array([-0.31811132, -0.82796869,  0.60788185])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
