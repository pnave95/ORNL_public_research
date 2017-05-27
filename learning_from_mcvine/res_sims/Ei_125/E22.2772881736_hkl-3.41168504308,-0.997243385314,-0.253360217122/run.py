#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E22.2772881736_hkl-3.41168504308,-0.997243385314,-0.253360217122/sample/sampleassembly.xml'
psi = -0.002397739093228495
hkl2Q = array([[-0.65843834,  0.93592485,  0.        ],
       [ 0.66179881,  0.46558622, -0.80916512],
       [-0.66179881, -0.46558622, -0.80916512]])
pp = array([ 2.58946408,  1.51481873, -0.4330969 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034635079759876659
Q = array([ 1.75408325, -3.53942255,  1.01194481])
E = 22.277288173624555
hkl_projection = array([ 0.18808939,  0.95168753,  0.83305084])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
