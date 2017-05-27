#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E213.609772995_hkl-6.68358173938,3.13116624691,-3.03253210911/sample/sampleassembly.xml'
psi = -0.008908414406291325
hkl2Q = array([[-0.65233093,  0.94019186,  0.        ],
       [ 0.66481604,  0.46126762, -0.80916512],
       [-0.66481604, -0.46126762, -0.80916512]])
pp = array([ 1.79338781,  2.40494494,  0.05578512])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030779947027569235
Q = array([ 8.4576326 , -3.44073466, -0.0798113 ])
E = 213.60977299523216
hkl_projection = array([-0.76960526, -0.05429864, -0.1858669 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
