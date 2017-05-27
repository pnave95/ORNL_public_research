#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-240.12322863_hkl-26.8458367583,0.319059324932,-1.45513029015/sample/sampleassembly.xml'
psi = -0.004224907302932326
hkl2Q = array([[-0.65672715,  0.93712636,  0.        ],
       [ 0.66264841,  0.46437622, -0.80916512],
       [-0.66264841, -0.46437622, -0.80916512]])
pp = array([ 0.4009801 ,  2.97308173, -0.1123143 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011770056945081167
Q = array([ 18.80605384, -24.33404988,   0.91926899])
E = -240.12322863039333
hkl_projection = array([ 0.31691386, -0.802951  , -0.22038229])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
