#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E40.036842982_hkl-2.68505269204,0.40748482407,0.260139164689/sample/sampleassembly.xml'
psi = -0.0036854255259352858
hkl2Q = array([[-0.65723262,  0.93677193,  0.        ],
       [ 0.66239779,  0.46473364, -0.80916512],
       [-0.66239779, -0.46473364, -0.80916512]])
pp = array([ 2.77402763,  1.1422656 ,  0.25219515])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0035252193803185735
Q = array([ 1.86230565, -2.44680552, -0.54021804])
E = 40.03684298201577
hkl_projection = array([-0.54781633,  0.11111758,  0.95150225])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
