#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-10.6268212535_hkl-5.80425972079,-0.426019866711,-0.142160243426/sample/sampleassembly.xml'
psi = -0.0031198225144000048
hkl2Q = array([[-0.65776235,  0.93640005,  0.        ],
       [ 0.66213483,  0.46510822, -0.80916512],
       [-0.66213483, -0.46510822, -0.80916512]])
pp = array([ 0.9121988 ,  2.85795265, -0.23601874])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048362235220933761
Q = array([ 3.6298702 , -5.56713454,  0.45975152])
E = -10.626821253513803
hkl_projection = array([-0.25678312,  0.00455321, -0.52870785])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
