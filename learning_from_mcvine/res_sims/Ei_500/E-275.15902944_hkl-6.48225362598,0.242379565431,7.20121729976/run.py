#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-275.15902944_hkl-6.48225362598,0.242379565431,7.20121729976/sample/sampleassembly.xml'
psi = 0.0001600719573354157
hkl2Q = array([[-0.6608301 ,  0.93423763,  0.        ],
       [ 0.66060576,  0.46727745, -0.80916512],
       [-0.66060576, -0.46727745, -0.80916512]])
pp = array([ 2.58989035,  1.51408981,  0.97978437])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016491273326354227
Q = array([-0.31337996, -9.30767319, -6.02309892])
E = -275.15902943959259
hkl_projection = array([ 0.45073874,  0.0699336 , -0.05368729])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
