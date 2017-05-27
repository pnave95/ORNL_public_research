#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-14.2854763682_hkl-0.247155633495,-0.962135347264,0.364598065967/sample/sampleassembly.xml'
psi = 0.0030970312230704923
hkl2Q = array([[-0.66357107,  0.93229277,  0.        ],
       [ 0.65923054,  0.4692156 , -0.80916512],
       [-0.65923054, -0.4692156 , -0.80916512]])
pp = array([ 2.94818878,  0.55514226, -0.31469164])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006721867691443598
Q = array([-0.71061786, -0.85294543,  0.48350632])
E = -14.285476368176042
hkl_projection = array([-0.28386931,  0.96300553, -0.06041023])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
