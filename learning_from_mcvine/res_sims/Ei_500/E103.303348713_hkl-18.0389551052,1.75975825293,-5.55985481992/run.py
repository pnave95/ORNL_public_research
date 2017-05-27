#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E103.303348713_hkl-18.0389551052,1.75975825293,-5.55985481992/sample/sampleassembly.xml'
psi = -0.0058791439056545824
hkl2Q = array([[-0.65517603,  0.93821146,  0.        ],
       [ 0.66341569,  0.46327941, -0.80916512],
       [-0.66341569, -0.46327941, -0.80916512]])
pp = array([-0.23579496,  2.9907191 , -0.67952085])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017417512415640417
Q = array([ 16.67463704, -13.53332841,   3.07490558])
E = 103.30334871275352
hkl_projection = array([ 0.22948066,  0.98935002, -0.12415065])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
