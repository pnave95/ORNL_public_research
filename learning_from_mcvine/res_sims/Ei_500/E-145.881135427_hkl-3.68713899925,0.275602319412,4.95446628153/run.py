#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-145.881135427_hkl-3.68713899925,0.275602319412,4.95446628153/sample/sampleassembly.xml'
psi = 0.0005505746505950705
hkl2Q = array([[-0.66119488,  0.9339795 ,  0.        ],
       [ 0.66042324,  0.46753538, -0.80916512],
       [-0.66042324, -0.46753538, -0.80916512]])
pp = array([ 2.83480347,  0.98177865,  0.73782534])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016676680994361268
Q = array([-0.65211307, -5.63124668, -4.23198907])
E = -145.88113542699836
hkl_projection = array([-0.43292348, -0.04660251,  0.03521383])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
