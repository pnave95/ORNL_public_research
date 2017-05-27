#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E27.6081759055_hkl-1.90602486041,1.14835041277,-1.38469788953/sample/sampleassembly.xml'
psi = -0.01741185980563636
hkl2Q = array([[ -6.44312569e-01,   9.45704861e-01,   7.68650496e-17],
       [  6.68714320e-01,   4.55597787e-01,  -8.09165116e-01],
       [ -6.68714320e-01,  -4.55597787e-01,  -8.09165116e-01]])
pp = array([ 2.43133754,  1.75744068, -0.51828465])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0099924260944285678
Q = array([ 2.92196145, -0.64848578,  0.19124413])
E = 27.608175905473161
hkl_projection = array([ 0.43546954, -0.4679015 ,  0.98759796])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
