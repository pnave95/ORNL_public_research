#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E79.6399573426_hkl-3.58490389466,0.906842128946,-1.17371605267/sample/sampleassembly.xml'
psi = -0.007531203147313919
hkl2Q = array([[ -6.53625151e-01,   9.39292571e-01,  -7.73897861e-17],
       [  6.64180146e-01,   4.62182777e-01,  -8.09165116e-01],
       [ -6.64180146e-01,  -4.62182777e-01,  -8.09165116e-01]])
pp = array([ 2.5841323 ,  1.52389641, -0.13679232])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0037898533098086953
Q = array([ 3.72504879, -2.40567544,  0.21594507])
E = 79.63995734264131
hkl_projection = array([ 0.24569774,  0.96375201, -0.22396121])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
