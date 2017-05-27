#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E7.18975211773_hkl-0.956069021256,-0.12382186465,-0.102683478372/sample/sampleassembly.xml'
psi = -0.0025274683402809004
hkl2Q = array([[-0.65831692,  0.93601026,  0.        ],
       [ 0.6618592 ,  0.46550036, -0.80916512],
       [-0.6618592 , -0.46550036, -0.80916512]])
pp = array([ 2.88708493,  0.81531627, -0.16516673])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071194353474157909
Q = array([ 0.61540578, -0.90473034,  0.18328022])
E = 7.1897521177257246
hkl_projection = array([-0.86018082,  0.46442976,  0.59717431])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
