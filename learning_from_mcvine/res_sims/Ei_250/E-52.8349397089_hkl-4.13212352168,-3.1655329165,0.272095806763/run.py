#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-52.8349397089_hkl-4.13212352168,-3.1655329165,0.272095806763/sample/sampleassembly.xml'
psi = -0.0002997677547413123
hkl2Q = array([[-0.66040044,  0.9345414 ,  0.        ],
       [ 0.66082056,  0.46697363, -0.80916512],
       [-0.66082056, -0.46697363, -0.80916512]])
pp = array([ 2.66448438,  1.37859457, -0.59039796])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023683743125601899
Q = array([ 0.45720042, -5.46692247,  2.34126838])
E = -52.834939708935821
hkl_projection = array([-0.94113815,  0.19704315,  0.53364106])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
