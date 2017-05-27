#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E203.53414774_hkl-6.05217689553,2.8465629954,-2.44345489968/sample/sampleassembly.xml'
psi = -0.008325695149661376
hkl2Q = array([[-0.65287868,  0.93981157,  0.        ],
       [ 0.66454714,  0.46165495, -0.80916512],
       [-0.66454714, -0.46165495, -0.80916512]])
pp = array([ 2.21595289,  2.02226428,  0.20322749])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0029574281094200804
Q = array([ 7.46680354, -3.24574297, -0.32618101])
E = 203.53414774001686
hkl_projection = array([ 0.8610953 ,  0.44122605, -0.74520607])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
