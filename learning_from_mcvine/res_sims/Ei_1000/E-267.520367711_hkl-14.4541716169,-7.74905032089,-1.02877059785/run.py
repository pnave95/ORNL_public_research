#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-267.520367711_hkl-14.4541716169,-7.74905032089,-1.02877059785/sample/sampleassembly.xml'
psi = -0.0016659515231727817
hkl2Q = array([[-0.65912306,  0.93544276,  0.        ],
       [ 0.66145792,  0.46607039, -0.80916512],
       [-0.66145792, -0.46607039, -0.80916512]])
pp = array([ 2.14344489,  2.0989626 , -0.89522368])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011831394604420453
Q = array([  5.08189564, -16.65317357,   7.10270649])
E = -267.52036771105952
hkl_projection = array([-0.07618601,  0.53810313,  0.0861001 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
