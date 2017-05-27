#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-149.364144079_hkl-10.0287582098,-4.09632595418,2.77430916393/sample/sampleassembly.xml'
psi = -0.0009002523946600547
hkl2Q = array([[ -6.59839139e-01,   9.34937796e-01,   7.77502540e-17],
       [  6.61100856e-01,   4.66576729e-01,  -8.09165116e-01],
       [ -6.61100856e-01,  -4.66576729e-01,  -8.09165116e-01]])
pp = array([ 2.53976871,  1.59673883, -0.13575639])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011845170686428424
Q = array([  2.07518442, -12.58194356,   1.06972987])
E = -149.36414407887366
hkl_projection = array([ 0.11658756,  0.09939044,  0.17470177])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
