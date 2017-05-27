#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-30.2296772757_hkl0.17404430441,-0.0749943426565,1.4231242673/sample/sampleassembly.xml'
psi = 0.009686000266727947
hkl2Q = array([[-0.66969947,  0.92790031,  0.        ],
       [ 0.6561246 ,  0.47354904, -0.80916512],
       [-0.6561246 , -0.47354904, -0.80916512]])
pp = array([ 2.98941764,  0.25175812,  0.50121247])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047506230033653035
Q = array([-1.09950986, -0.54793686, -1.09085971])
E = -30.229677275700464
hkl_projection = array([ 0.20605738,  0.75322773, -0.53702465])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
