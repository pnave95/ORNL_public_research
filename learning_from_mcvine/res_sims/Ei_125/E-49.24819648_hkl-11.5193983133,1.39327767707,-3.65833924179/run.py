#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-49.24819648_hkl-11.5193983133,1.39327767707,-3.65833924179/sample/sampleassembly.xml'
psi = -0.006244125213136183
hkl2Q = array([[-0.65483355,  0.93845053,  0.        ],
       [ 0.66358473,  0.46303725, -0.80916512],
       [-0.66358473, -0.46303725, -0.80916512]])
pp = array([-1.0283264 ,  2.81825208, -0.60974326])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003312143638912204
Q = array([ 10.89546437,  -8.47129863,   1.8328088 ])
E = -49.24819648001602
hkl_projection = array([-0.38830385,  0.46798999,  0.05576637])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
