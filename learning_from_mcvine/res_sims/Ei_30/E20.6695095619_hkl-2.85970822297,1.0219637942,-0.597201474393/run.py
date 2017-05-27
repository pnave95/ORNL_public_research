#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E20.6695095619_hkl-2.85970822297,1.0219637942,-0.597201474393/sample/sampleassembly.xml'
psi = -0.005688942123512408
hkl2Q = array([[ -6.55354463e-01,   9.38086829e-01,   7.74892567e-17],
       [  6.63327558e-01,   4.63405585e-01,  -8.09165116e-01],
       [ -6.63327558e-01,  -4.63405585e-01,  -8.09165116e-01]])
pp = array([ 1.23274866,  2.73501933,  0.48647833])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0079361689988593533
Q = array([ 2.94815949, -1.93232439, -0.34370285])
E = 20.669509561863798
hkl_projection = array([-0.70379781,  0.3879547 , -0.16005276])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
