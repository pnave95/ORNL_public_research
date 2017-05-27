#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-97.1479965304_hkl-10.6797433609,-1.61767945674,-1.57209123523/sample/sampleassembly.xml'
psi = -0.0033768975685937947
hkl2Q = array([[ -6.57521608e-01,   9.36569115e-01,  -7.76148284e-17],
       [  6.62254372e-01,   4.64937988e-01,  -8.09165116e-01],
       [ -6.62254372e-01,  -4.64937988e-01,  -8.09165116e-01]])
pp = array([ 0.24237672,  2.99019289, -0.76997361])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032575639333925514
Q = array([  6.99197103, -10.02351348,   2.58105117])
E = -97.147996530420301
hkl_projection = array([ 0.03800999, -0.14756416,  0.796531  ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
