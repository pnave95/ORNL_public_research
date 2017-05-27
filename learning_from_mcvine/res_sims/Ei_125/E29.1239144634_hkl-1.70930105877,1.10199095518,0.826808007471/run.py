#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E29.1239144634_hkl-1.70930105877,1.10199095518,0.826808007471/sample/sampleassembly.xml'
psi = -0.004288069439669644
hkl2Q = array([[-0.65666796,  0.93716784,  0.        ],
       [ 0.66267774,  0.46433437, -0.80916512],
       [-0.66267774, -0.46433437, -0.80916512]])
pp = array([ 2.92569669,  0.66355019,  0.70252787])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034986827906384093
Q = array([ 1.30480085, -1.47412508, -1.56071684])
E = 29.12391446340277
hkl_projection = array([-0.14200821,  0.47519536,  0.10570575])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
