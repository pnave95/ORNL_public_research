#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E90.3934804071_hkl-5.40685369332,1.72928472165,-1.52161058566/sample/sampleassembly.xml'
psi = -0.007742094313569846
hkl2Q = array([[-0.65342705,  0.93943039,  0.        ],
       [ 0.6642776 ,  0.4620427 , -0.80916512],
       [-0.6642776 , -0.4620427 , -0.80916512]])
pp = array([ 1.52517223,  2.58337951,  0.12135318])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0039307285125634714
Q = array([ 5.69248139, -3.57731026, -0.16804267])
E = 90.393480407147649
hkl_projection = array([-0.93364252, -0.23744393, -0.49633118])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
