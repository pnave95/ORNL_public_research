#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E231.213432612_hkl-9.66495380309,-2.40943237676,-1.12102124018/sample/sampleassembly.xml'
psi = -0.003116002610169636
hkl2Q = array([[-0.65776593,  0.93639754,  0.        ],
       [ 0.66213305,  0.46511075, -0.80916512],
       [-0.66213305, -0.46511075, -0.80916512]])
pp = array([ 2.59299551,  1.50876581, -0.44666817])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012312909191894612
Q = array([ 5.50417775, -9.64949282,  2.85671991])
E = 231.21343261239053
hkl_projection = array([ 0.53396259,  0.91415004,  0.82792284])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
