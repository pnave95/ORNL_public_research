#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E438.56958303_hkl-3.37763206606,2.70042685819,-2.2944232024/sample/sampleassembly.xml'
psi = -0.032880569367968016
hkl2Q = array([[-0.62960723,  0.95555801,  0.        ],
       [ 0.67568155,  0.44519954, -0.80916512],
       [-0.67568155, -0.44519954, -0.80916512]])
pp = array([ 2.99452099,  0.18122922,  0.05931167])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012696994389245304
Q = array([ 5.50150959, -1.00381839, -0.328524  ])
E = 438.56958302972953
hkl_projection = array([ 0.93050985,  0.91749887,  0.04149525])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
