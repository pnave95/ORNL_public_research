#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E33.800752502_hkl-4.23733371692,0.697040732784,-0.90775388592/sample/sampleassembly.xml'
psi = -0.005701775942884329
hkl2Q = array([[-0.65534242,  0.93809524,  0.        ],
       [ 0.66333351,  0.46339707, -0.80916512],
       [-0.66333351, -0.46339707, -0.80916512]])
pp = array([ 1.30790179,  2.69988757, -0.14245851])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0053479017259472584
Q = array([ 3.84141859, -3.23136546,  0.17050173])
E = 33.800752502033603
hkl_projection = array([ 0.98823267, -0.83962845, -0.60844412])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
