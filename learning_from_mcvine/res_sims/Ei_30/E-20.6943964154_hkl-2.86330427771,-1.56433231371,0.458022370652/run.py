#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-20.6943964154_hkl-2.86330427771,-1.56433231371,0.458022370652/sample/sampleassembly.xml'
psi = -0.0005676524133416123
hkl2Q = array([[-0.66015006,  0.93471828,  0.        ],
       [ 0.66094564,  0.46679659, -0.80916512],
       [-0.66094564, -0.46679659, -0.80916512]])
pp = array([ 2.00933975,  2.22767901, -0.55081872])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066654177164575884
Q = array([ 0.55354399, -3.62041112,  0.89518741])
E = -20.694396415421497
hkl_projection = array([ 0.69222515,  0.35959071,  0.14787975])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
