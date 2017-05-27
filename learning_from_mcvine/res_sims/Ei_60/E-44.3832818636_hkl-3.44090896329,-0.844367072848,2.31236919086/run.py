#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-44.3832818636_hkl-3.44090896329,-0.844367072848,2.31236919086/sample/sampleassembly.xml'
psi = -0.00019045019073519253
hkl2Q = array([[ -6.60502593e-01,   9.34469205e-01,  -7.77892419e-17],
       [  6.60769512e-01,   4.67045863e-01,  -8.09165116e-01],
       [ -6.60769512e-01,  -4.67045863e-01,  -8.09165116e-01]])
pp = array([ 2.23161881,  2.00496321,  0.50783104])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046998837030586965
Q = array([ 0.18685421, -4.68976408, -1.1878561 ])
E = -44.383281863589033
hkl_projection = array([ 0.82299864,  0.06423135, -0.49235349])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
