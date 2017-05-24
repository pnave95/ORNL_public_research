#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-183.472985248_hkl-19.3205041933,1.72133852892,1.25203314187/sample/sampleassembly.xml'
psi = -0.0034648846624978674
hkl2Q = array([[ -6.57439200e-01,   9.36626964e-01,  -7.76100346e-17],
       [  6.62295278e-01,   4.64879716e-01,  -8.09165116e-01],
       [ -6.62295278e-01,  -4.64879716e-01,  -8.09165116e-01]])
pp = array([ 0.43089855,  2.96889313,  0.39954304])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016545171065278997
Q = array([ 13.01287555, -17.87793464,  -2.40594863])
E = -183.47298524815227
hkl_projection = array([-0.18043804, -0.59634379,  0.523067  ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
