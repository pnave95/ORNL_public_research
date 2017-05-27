#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-79.7515411555_hkl-6.14962281993,-3.52676569968,-0.0395708163465/sample/sampleassembly.xml'
psi = -0.0011475722117951334
hkl2Q = array([[-0.65960789,  0.93510096,  0.        ],
       [ 0.66121623,  0.46641321, -0.80916512],
       [-0.66121623, -0.46641321, -0.80916512]])
pp = array([ 1.90313447,  2.3190686 , -0.90718061])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032830510268392959
Q = array([ 1.75054988, -7.37699196,  2.8857551 ])
E = -79.751541155507908
hkl_projection = array([ 0.41824508,  0.27682804, -0.57244355])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
