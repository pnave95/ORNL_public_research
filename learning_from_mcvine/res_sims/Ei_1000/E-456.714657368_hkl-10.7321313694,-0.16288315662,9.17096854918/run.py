#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-456.714657368_hkl-10.7321313694,-0.16288315662,9.17096854918/sample/sampleassembly.xml'
psi = -0.0003485292248981109
hkl2Q = array([[-0.66035486,  0.93457361,  0.        ],
       [ 0.66084333,  0.4669414 , -0.80916512],
       [-0.66084333, -0.4669414 , -0.80916512]])
pp = array([ 2.48114573,  1.68639137,  0.85431429])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011691083608093812
Q = array([  0.91880148, -14.38832852,  -7.28902847])
E = -456.71465736764986
hkl_projection = array([-0.4653831 ,  0.63587898,  0.90281318])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
