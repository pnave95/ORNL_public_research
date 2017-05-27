#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-114.610374332_hkl-4.9280922798,-3.60774003892,1.54918201357/sample/sampleassembly.xml'
psi = 7.698718823198802e-05
hkl2Q = array([[-0.66075248,  0.93429253,  0.        ],
       [ 0.66064458,  0.46722256, -0.80916512],
       [-0.66064458, -0.46722256, -0.80916512]])
pp = array([ 2.54093217,  1.59488674, -0.37877587])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023290260195060011
Q = array([-0.15064341, -7.01371012,  1.66571334])
E = -114.61037433174725
hkl_projection = array([-0.03362911, -0.28982302, -0.20860911])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
