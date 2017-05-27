#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E49.8880958625_hkl-4.5809670097,2.22294492993,-2.7639241119/sample/sampleassembly.xml'
psi = -0.015051275645904269
hkl2Q = array([[-0.64654319,  0.94418127,  0.        ],
       [ 0.66763698,  0.45717507, -0.80916512],
       [-0.66763698, -0.45717507, -0.80916512]])
pp = array([-1.19065916,  2.75360323, -0.58930851])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0061590592959137854
Q = array([ 6.29121121, -2.04539105,  0.43774148])
E = 49.888095862450655
hkl_projection = array([-0.85617529, -0.50961948,  0.52335109])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
