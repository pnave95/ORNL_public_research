#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-14.2443580605_hkl-5.15310121699,-0.904454309992,0.169043412633/sample/sampleassembly.xml'
psi = -0.002410427913789344
hkl2Q = array([[-0.65842647,  0.9359332 ,  0.        ],
       [ 0.66180471,  0.46557782, -0.80916512],
       [-0.66180471, -0.46557782, -0.80916512]])
pp = array([ 1.36683329,  2.67053679, -0.29855839])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048177350215502669
Q = array([ 2.68249237, -5.32275525,  0.59506884])
E = -14.244358060507103
hkl_projection = array([ 0.57424448, -0.61040277, -0.08695474])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
