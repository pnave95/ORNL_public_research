#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-27.6268496574_hkl-2.87489558622,-1.38403376524,1.21787183717/sample/sampleassembly.xml'
psi = -0.0002199083249573936
hkl2Q = array([[-0.66047507,  0.93448866,  0.        ],
       [ 0.66078327,  0.4670264 , -0.80916512],
       [-0.66078327, -0.4670264 , -0.80916512]])
pp = array([ 2.40413198,  1.79447748, -0.06183737])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047513448816116962
Q = array([ 0.17950116, -3.90171593,  0.13445244])
E = -27.626849657379495
hkl_projection = array([-0.36867764,  0.09849636,  0.34900029])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
