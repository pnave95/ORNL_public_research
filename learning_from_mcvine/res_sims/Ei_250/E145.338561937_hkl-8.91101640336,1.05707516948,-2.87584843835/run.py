#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E145.338561937_hkl-8.91101640336,1.05707516948,-2.87584843835/sample/sampleassembly.xml'
psi = -0.004656738740738296
hkl2Q = array([[-0.65632241,  0.93740987,  0.        ],
       [ 0.66284888,  0.46409003, -0.80916512],
       [-0.66284888, -0.46409003, -0.80916512]])
pp = array([ 1.0982148 ,  2.79176006, -0.62937679])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0026470912973120581
Q = array([ 8.45543376, -6.52804411,  1.47168788])
E = 145.33856193698131
hkl_projection = array([-0.51518143, -0.55026177, -0.9780799 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
