#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-95.8854403461_hkl-3.42683867979,-1.762505964,3.07330014762/sample/sampleassembly.xml'
psi = 0.0008202024054251212
hkl2Q = array([[-0.66144668,  0.93380119,  0.        ],
       [ 0.66029715,  0.46771343, -0.80916512],
       [-0.66029715, -0.46771343, -0.80916512]])
pp = array([ 2.54334295,  1.59103948,  0.30897277])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032464263985916625
Q = array([-0.92639794, -5.46175751, -1.06064893])
E = -95.885440346081282
hkl_projection = array([ 0.87334423,  0.84461451, -0.16553787])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
