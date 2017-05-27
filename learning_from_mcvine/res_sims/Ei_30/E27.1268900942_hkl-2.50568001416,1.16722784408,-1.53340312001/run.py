#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E27.1268900942_hkl-2.50568001416,1.16722784408,-1.53340312001/sample/sampleassembly.xml'
psi = -0.011572612292272022
hkl2Q = array([[-0.64982376,  0.94192646,  0.        ],
       [ 0.66604259,  0.45949479, -0.80916512],
       [-0.66604259, -0.45949479, -0.80916512]])
pp = array([ 0.99193372,  2.83126606, -0.74952039])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0097058468110306721
Q = array([ 3.42698564, -1.11924046,  0.29629626])
E = 27.12689009418154
hkl_projection = array([ 0.08113454,  0.42139615, -0.10915728])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
