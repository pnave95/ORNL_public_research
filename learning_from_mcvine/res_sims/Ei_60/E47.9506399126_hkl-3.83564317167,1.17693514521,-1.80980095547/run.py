#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E47.9506399126_hkl-3.83564317167,1.17693514521,-1.80980095547/sample/sampleassembly.xml'
psi = -0.009701287514149415
hkl2Q = array([[-0.65158527,  0.94070878,  0.        ],
       [ 0.66518156,  0.46074036, -0.80916512],
       [-0.66518156, -0.46074036, -0.80916512]])
pp = array([ 1.14406303,  2.77328682, -0.63624932])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059942002037275252
Q = array([ 4.48597036, -2.23211333,  0.51209294])
E = 47.950639912622663
hkl_projection = array([-0.12370261, -0.41119641, -0.47134308])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
