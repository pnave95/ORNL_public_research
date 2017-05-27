#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E236.410115614_hkl-7.0664060677,4.38411427424,-4.38260501527/sample/sampleassembly.xml'
psi = -0.014467230203634766
hkl2Q = array([[-0.64709452,  0.9438035 ,  0.        ],
       [ 0.66736986,  0.45756492, -0.80916512],
       [-0.66736986, -0.45756492, -0.80916512]])
pp = array([  6.60737788e-01,   2.92633313e+00,   1.34455004e-03])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0037164871759888893
Q = array([  1.04232769e+01,  -2.65795554e+00,  -1.22123971e-03])
E = 236.41011561393896
hkl_projection = array([ 0.07546432, -0.46919236, -0.3878117 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
