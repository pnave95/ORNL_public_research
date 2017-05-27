#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-4.9116846022_hkl-1.87067501917,-0.646455884855,0.585965190633/sample/sampleassembly.xml'
psi = -0.0006712067461564367
hkl2Q = array([[-0.66005326,  0.93478664,  0.        ],
       [ 0.66099397,  0.46672814, -0.80916512],
       [-0.66099397, -0.46672814, -0.80916512]])
pp = array([ 2.47651129,  1.69318984, -0.03566287])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068453530747702969
Q = array([ 0.42012225, -2.32388761,  0.04894696])
E = -4.9116846021994043
hkl_projection = array([ 0.08898328,  0.85686166, -0.91068183])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
