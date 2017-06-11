#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_250/E-222.515215003_hkl-17.1727785605,-0.348661129641,-3.50176300208/sample/sampleassembly.xml'
psi = -0.0032863990801390397
hkl2Q = array([[-0.65760636,  0.93650961,  0.        ],
       [ 0.66221229,  0.46499792, -0.80916512],
       [-0.66221229, -0.46499792, -0.80916512]])
pp = array([-0.47771078,  2.96172119, -0.63132481])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002289694462129985
Q = array([ 13.38095128, -14.61628628,   3.11562889])
E = -222.51521500311114
hkl_projection = array([ 0.11398597, -0.79419774,  0.81752781])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
