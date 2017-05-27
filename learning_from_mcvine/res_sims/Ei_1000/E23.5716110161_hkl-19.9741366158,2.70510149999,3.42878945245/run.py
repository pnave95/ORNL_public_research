#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E23.5716110161_hkl-19.9741366158,2.70510149999,3.42878945245/sample/sampleassembly.xml'
psi = -0.0036290559932759445
hkl2Q = array([[-0.65728542,  0.93673488,  0.        ],
       [ 0.66237159,  0.46477098, -0.80916512],
       [-0.66237159, -0.46477098, -0.80916512]])
pp = array([ 1.33206073,  2.68805026,  0.7004677 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001207104266075404
Q = array([ 12.6493585 , -19.04681971,  -4.96333059])
E = 23.571611016110865
hkl_projection = array([ 0.52452361,  0.00679763,  0.34935573])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
