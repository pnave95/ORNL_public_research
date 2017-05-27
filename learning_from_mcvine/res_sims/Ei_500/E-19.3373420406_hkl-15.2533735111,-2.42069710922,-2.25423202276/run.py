#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-19.3373420406_hkl-15.2533735111,-2.42069710922,-2.25423202276/sample/sampleassembly.xml'
psi = -0.0032876426314002783
hkl2Q = array([[-0.6576052 ,  0.93651042,  0.        ],
       [ 0.66221287,  0.4649971 , -0.80916512],
       [-0.66221287, -0.4649971 , -0.80916512]])
pp = array([ 1.10449464,  2.78928156, -0.73464759])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016992157361615697
Q = array([  9.9204624 , -14.36234907,   3.78278958])
E = -19.337342040639726
hkl_projection = array([ 0.31254627, -0.09297802, -0.6958118 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
