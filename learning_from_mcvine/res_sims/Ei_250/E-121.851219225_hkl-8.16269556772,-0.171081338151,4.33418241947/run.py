#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-121.851219225_hkl-8.16269556772,-0.171081338151,4.33418241947/sample/sampleassembly.xml'
psi = -0.0008867524933617506
hkl2Q = array([[-0.65985176,  0.93492889,  0.        ],
       [ 0.66109456,  0.46658565, -0.80916512],
       [-0.66109456, -0.46658565, -0.80916512]])
pp = array([ 1.98838624,  2.2464016 ,  0.77743952])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002334413429203075
Q = array([ 2.40776369, -9.73363133, -3.36863617])
E = -121.85121922450708
hkl_projection = array([ 0.95650565,  0.77416373, -0.66784742])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
