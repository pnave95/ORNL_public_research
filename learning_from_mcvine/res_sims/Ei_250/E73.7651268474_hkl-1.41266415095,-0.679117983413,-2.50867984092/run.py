#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E73.7651268474_hkl-1.41266415095,-0.679117983413,-2.50867984092/sample/sampleassembly.xml'
psi = -0.01586711639390709
hkl2Q = array([[ -6.45772671e-01,   9.44708436e-01,  -7.69461226e-17],
       [  6.68009741e-01,   4.56630235e-01,  -8.09165116e-01],
       [ -6.68009741e-01,  -4.56630235e-01,  -8.09165116e-01]])
pp = array([ 2.99528182,  0.16818694, -0.8691867 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025030506169379401
Q = array([ 2.13442505, -0.49912248,  2.5794548 ])
E = 73.765126847388046
hkl_projection = array([-0.10333555, -0.82617256, -0.46647302])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
