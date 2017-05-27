#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E83.0946300162_hkl-7.3522393435,3.28982040473,-2.11347454408/sample/sampleassembly.xml'
psi = -0.009249838973343687
hkl2Q = array([[-0.65200988,  0.94041453,  0.        ],
       [ 0.66497349,  0.46104061, -0.80916512],
       [-0.66497349, -0.46104061, -0.80916512]])
pp = array([-0.39159879,  2.97433192,  0.64009329])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0038518084661008445
Q = array([ 8.38678062, -4.42301428, -0.95185804])
E = 83.094630016230042
hkl_projection = array([-0.27791794,  0.2300232 , -0.19377722])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
