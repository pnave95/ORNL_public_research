#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-231.090588013_hkl-14.2137032421,1.0015042696,3.48501390729/sample/sampleassembly.xml'
psi = -0.0019157870123303778
hkl2Q = array([[-0.65888934,  0.9356074 ,  0.        ],
       [ 0.66157434,  0.46590512, -0.80916512],
       [-0.66157434, -0.46590512, -0.80916512]])
pp = array([ 0.66791027,  2.92470441,  0.73450485])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022892064509777341
Q = array([  7.72223125, -14.45552583,  -3.630334  ])
E = -231.09058801324525
hkl_projection = array([-0.92477244,  0.88622102, -0.36868391])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
