#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_60/E-23.12494335_hkl-7.18150150339,-0.261575911401,-1.36411006101/sample/sampleassembly.xml'
psi = -0.004195194937939414
hkl2Q = array([[-0.656755  ,  0.93710685,  0.        ],
       [ 0.66263461,  0.46439591, -0.80916512],
       [-0.66263461, -0.46439591, -0.80916512]])
pp = array([-0.01943453,  2.99993705, -0.63466957])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047871661764422148
Q = array([ 5.44706427, -6.21782189,  1.31544838])
E = -23.12494335004795
hkl_projection = array([-0.28483648,  0.51993042,  0.31873636])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
