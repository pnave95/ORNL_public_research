#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-5.66992463877_hkl-2.80235468306,-1.04449784387,-0.0276434937742/sample/sampleassembly.xml'
psi = -0.001410125553556945
hkl2Q = array([[ -6.59362353e-01,   9.35274109e-01,   7.77222960e-17],
       [  6.61338665e-01,   4.66239591e-01,  -8.09165116e-01],
       [ -6.61338665e-01,  -4.66239591e-01,  -8.09165116e-01]])
pp = array([ 1.94851115,  2.28107525, -0.63937945])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068586961475247087
Q = array([ 1.17528208, -3.09506754,  0.86753937])
E = -5.6699246387674584
hkl_projection = array([ 0.60380775,  0.56189557, -0.74913194])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
