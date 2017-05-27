#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E129.312929987_hkl-7.63963909708,2.15674207306,-0.192197313331/sample/sampleassembly.xml'
psi = -0.0038935795874725154
hkl2Q = array([[-0.65703761,  0.93690872,  0.        ],
       [ 0.66249451,  0.46459575, -0.80916512],
       [-0.66249451, -0.46459575, -0.80916512]])
pp = array([ 1.77385254,  2.41938984,  0.63398412])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0026012951512819123
Q = array([ 6.57568967, -6.06633722, -1.58964109])
E = 129.31292998721926
hkl_projection = array([-0.98439581, -0.33808164,  0.82158674])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
