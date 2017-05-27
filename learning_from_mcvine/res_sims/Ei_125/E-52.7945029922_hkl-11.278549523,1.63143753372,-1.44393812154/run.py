#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-52.7945029922_hkl-11.278549523,1.63143753372,-1.44393812154/sample/sampleassembly.xml'
psi = -0.00500104486828133
hkl2Q = array([[-0.65599962,  0.93763579,  0.        ],
       [ 0.66300863,  0.46386178, -0.80916512],
       [-0.66300863, -0.46386178, -0.80916512]])
pp = array([-0.52724459,  2.95330546,  0.04897672])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032964704349261287
Q = array([ 9.43772474, -9.14862249, -0.15171798])
E = -52.794502992179076
hkl_projection = array([-0.31604096, -0.63456322, -0.0078348 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
