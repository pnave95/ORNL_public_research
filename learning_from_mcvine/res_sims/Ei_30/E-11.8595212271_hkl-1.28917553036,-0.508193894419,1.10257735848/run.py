#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-11.8595212271_hkl-1.28917553036,-0.508193894419,1.10257735848/sample/sampleassembly.xml'
psi = 0.0004015621642318076
hkl2Q = array([[-0.66105569,  0.93407802,  0.        ],
       [ 0.6604929 ,  0.46743696, -0.80916512],
       [-0.6604929 , -0.46743696, -0.80916512]])
pp = array([ 2.69870637,  1.31033733,  0.32200938])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067515180086392479
Q = array([-0.21168615, -1.95712455, -0.48095436])
E = -11.859521227109148
hkl_projection = array([-0.31873139, -0.09024906,  0.05199173])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
