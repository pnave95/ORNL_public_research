#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-125.825125357_hkl-22.1655367937,6.4118485827,-3.00941040302/sample/sampleassembly.xml'
psi = -0.0060315243731431465
hkl2Q = array([[-0.65503305,  0.93831129,  0.        ],
       [ 0.66348627,  0.46317831, -0.80916512],
       [-0.66348627, -0.46317831, -0.80916512]])
pp = array([-0.89904914,  2.86211646,  0.47946787])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016673641876786961
Q = array([ 20.77003525, -16.43445051,  -2.75313429])
E = -125.82512535688227
hkl_projection = array([-0.59933463,  0.76800249, -0.73797266])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
