#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E218.773734873_hkl-4.15806838246,2.81492151281,-4.07291719944/sample/sampleassembly.xml'
psi = -0.033083618483890104
hkl2Q = array([[-0.6294132 ,  0.95568583,  0.        ],
       [ 0.67577193,  0.44506234, -0.80916512],
       [-0.67577193, -0.44506234, -0.80916512]])
pp = array([ 2.9157647 ,  0.70591516, -0.79112401])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032022427104697023
Q = array([ 7.27175116, -0.90828941,  1.01792623])
E = 218.77373487257614
hkl_projection = array([-0.23514918, -0.64149506,  0.34380602])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
