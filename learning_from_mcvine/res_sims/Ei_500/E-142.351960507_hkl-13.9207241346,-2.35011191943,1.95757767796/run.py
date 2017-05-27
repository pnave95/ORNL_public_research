#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-142.351960507_hkl-13.9207241346,-2.35011191943,1.95757767796/sample/sampleassembly.xml'
psi = -0.0020000781746503543
hkl2Q = array([[-0.65881047,  0.93566294,  0.        ],
       [ 0.66161361,  0.46584935, -0.80916512],
       [-0.66161361, -0.46584935, -0.80916512]])
pp = array([ 1.57674591,  2.5522289 , -0.05392898])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016604310197054517
Q = array([  6.32109276, -15.03184006,   0.31762502])
E = -142.35196050696362
hkl_projection = array([ 0.8353656 , -0.60787942,  0.46762935])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
