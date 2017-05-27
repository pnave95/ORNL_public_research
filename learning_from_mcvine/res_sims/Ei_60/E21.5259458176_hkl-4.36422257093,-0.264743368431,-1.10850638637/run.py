#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E21.5259458176_hkl-4.36422257093,-0.264743368431,-1.10850638637/sample/sampleassembly.xml'
psi = -0.004434659581381915
hkl2Q = array([[-0.65653057,  0.93726409,  0.        ],
       [ 0.6627458 ,  0.46423722, -0.80916512],
       [-0.6627458 , -0.46423722, -0.80916512]])
pp = array([ 1.41715228,  2.6441784 , -0.79437513])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0051563014329138405
Q = array([ 3.42444594, -3.69872291,  1.1111858 ])
E = 21.525945817564988
hkl_projection = array([ 0.19169791,  0.15450053,  0.25374048])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
