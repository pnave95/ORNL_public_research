#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-24.134252185_hkl-6.83048002019,-0.149437591091,-0.293312244006/sample/sampleassembly.xml'
psi = -0.0034669273100702267
hkl2Q = array([[-0.65743729,  0.93662831,  0.        ],
       [ 0.66229623,  0.46487836, -0.80916512],
       [-0.66229623, -0.46487836, -0.80916512]])
pp = array([ 0.38576947,  2.9750936 , -0.16836117])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047672658981041931
Q = array([ 4.58589989, -6.33073673,  0.35825772])
E = -24.134252185029681
hkl_projection = array([ 0.24940403, -0.8967737 ,  0.61844832])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
