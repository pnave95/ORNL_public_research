#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E86.5793335331_hkl-6.1336773586,1.2780128842,-2.40862672477/sample/sampleassembly.xml'
psi = -0.0077399878146345615
hkl2Q = array([[-0.65342903,  0.93942902,  0.        ],
       [ 0.66427663,  0.4620441 , -0.80916512],
       [-0.66427663, -0.4620441 , -0.80916512]])
pp = array([ 0.94530896,  2.84717245, -0.64175813])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0038979001149511529
Q = array([ 6.45687136, -4.05876443,  0.91485328])
E = 86.579333533138339
hkl_projection = array([ 0.18215211,  0.19028048, -0.5399014 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
