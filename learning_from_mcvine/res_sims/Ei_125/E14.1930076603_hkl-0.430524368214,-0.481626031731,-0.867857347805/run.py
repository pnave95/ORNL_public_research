#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E14.1930076603_hkl-0.430524368214,-0.481626031731,-0.867857347805/sample/sampleassembly.xml'
psi = -0.011544232329556422
hkl2Q = array([[-0.64985049,  0.94190802,  0.        ],
       [ 0.66602955,  0.45951369, -0.80916512],
       [-0.66602955, -0.45951369, -0.80916512]])
pp = array([ 2.99852424,  0.094087  , -0.4505379 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034390692316608519
Q = array([ 0.53701794, -0.22803578,  1.09195488])
E = 14.193007660263362
hkl_projection = array([ 0.62406437,  0.53078492, -0.04915737])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
