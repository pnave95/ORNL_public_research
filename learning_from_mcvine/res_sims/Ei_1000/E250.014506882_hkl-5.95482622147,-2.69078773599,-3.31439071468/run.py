#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E250.014506882_hkl-5.95482622147,-2.69078773599,-3.31439071468/sample/sampleassembly.xml'
psi = -0.004466394633388774
hkl2Q = array([[-0.65650083,  0.93728493,  0.        ],
       [ 0.66276053,  0.46421619, -0.80916512],
       [-0.66276053, -0.46421619, -0.80916512]])
pp = array([ 2.87515361,  0.8564413 , -0.78641267])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012400002355816761
Q = array([ 4.32264779, -5.29188226,  4.85918092])
E = 250.01450688161253
hkl_projection = array([ 0.74741814,  0.93267743,  0.17340863])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
