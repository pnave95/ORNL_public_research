#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-18.687030525_hkl-10.2108563319,-0.132653091267,1.16802118067/sample/sampleassembly.xml'
psi = -0.002070596411888715
hkl2Q = array([[-0.65874449,  0.93570939,  0.        ],
       [ 0.66164646,  0.46580269, -0.80916512],
       [-0.66164646, -0.46580269, -0.80916512]])
pp = array([ 1.35794668,  2.6750665 ,  0.22057792])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023860314031455649
Q = array([  5.8657588 , -10.16025178,  -0.83778374])
E = -18.687030525025961
hkl_projection = array([ 0.80591497,  0.81680807, -0.43849828])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
