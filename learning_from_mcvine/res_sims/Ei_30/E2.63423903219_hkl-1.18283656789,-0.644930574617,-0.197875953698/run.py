#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E2.63423903219_hkl-1.18283656789,-0.644930574617,-0.197875953698/sample/sampleassembly.xml'
psi = -0.0013680019048293614
hkl2Q = array([[ -6.59401750e-01,   9.35246333e-01,   7.77246042e-17],
       [  6.61319024e-01,   4.66267449e-01,  -8.09165116e-01],
       [ -6.61319024e-01,  -4.66267449e-01,  -8.09165116e-01]])
pp = array([ 2.79094414,  1.1002867 , -0.57075189])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0070173842046884136
Q = array([ 0.48431878, -1.31469058,  0.68196964])
E = 2.6342390321948024
hkl_projection = array([ 0.37566376, -0.2504306 , -0.19967362])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
