#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-777.295440545_hkl-27.1751401978,-3.19406835204,2.78036031174/sample/sampleassembly.xml'
psi = -0.002696118535223074
hkl2Q = array([[-0.65815905,  0.93612127,  0.        ],
       [ 0.6619377 ,  0.46538873, -0.80916512],
       [-0.6619377 , -0.46538873, -0.80916512]])
pp = array([ 0.83306961,  2.88201232, -0.03418812])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011451611526546075
Q = array([ 13.93086496, -28.21965853,   0.33475811])
E = -777.29544054505595
hkl_projection = array([-0.67487031,  0.51427389, -0.42438352])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
