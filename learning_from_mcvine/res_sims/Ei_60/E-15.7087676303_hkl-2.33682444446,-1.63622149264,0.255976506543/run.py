#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-15.7087676303_hkl-2.33682444446,-1.63622149264,0.255976506543/sample/sampleassembly.xml'
psi = -0.00045558242246111124
hkl2Q = array([[-0.66025481,  0.93464429,  0.        ],
       [ 0.66089332,  0.46687065, -0.80916512],
       [-0.66089332, -0.46687065, -0.80916512]])
pp = array([ 2.57273251,  1.5430643 , -0.56181221])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048198217167450246
Q = array([ 0.29235857, -3.06751135,  1.11684609])
E = -15.708767630251785
hkl_projection = array([ 0.8028452 ,  0.30439283, -0.39197393])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
