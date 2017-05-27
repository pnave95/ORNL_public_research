#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E86.7120348337_hkl-7.62228386234,3.53360635791,-3.42342194523/sample/sampleassembly.xml'
psi = -0.011798841097534662
hkl2Q = array([[-0.64961065,  0.94207344,  0.        ],
       [ 0.66614652,  0.4593441 , -0.80916512],
       [-0.66614652, -0.4593441 , -0.80916512]])
pp = array([-1.22433552,  2.73879582,  0.0612745 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0038753067573975117
Q = array([ 9.58591698, -3.98508133, -0.08915738])
E = 86.712034833655451
hkl_projection = array([-0.6235806 , -0.08226367,  0.30709024])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
