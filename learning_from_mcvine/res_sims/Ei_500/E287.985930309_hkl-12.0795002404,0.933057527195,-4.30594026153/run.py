#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E287.985930309_hkl-12.0795002404,0.933057527195,-4.30594026153/sample/sampleassembly.xml'
psi = -0.006101254940462387
hkl2Q = array([[-0.65496762,  0.93835696,  0.        ],
       [ 0.66351857,  0.46313205, -0.80916512],
       [-0.66351857, -0.46313205, -0.80916512]])
pp = array([ 1.28424731,  2.71121907, -0.83060912])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018741327818302099
Q = array([ 11.38785387,  -8.90853536,   2.72921905])
E = 287.9859303089811
hkl_projection = array([-0.332088  , -0.00390661, -0.48099392])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
