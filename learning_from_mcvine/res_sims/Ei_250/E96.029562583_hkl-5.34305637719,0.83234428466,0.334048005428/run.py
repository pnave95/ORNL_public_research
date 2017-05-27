#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E96.029562583_hkl-5.34305637719,0.83234428466,0.334048005428/sample/sampleassembly.xml'
psi = -0.0028926823210585605
hkl2Q = array([[-0.65797503,  0.93625062,  0.        ],
       [ 0.66202916,  0.46525861, -0.80916512],
       [-0.66202916, -0.46525861, -0.80916512]])
pp = array([ 2.49850766,  1.66055999,  0.32852095])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025207064357953887
Q = array([ 3.84548436, -4.77060323, -0.94380395])
E = 96.029562583034874
hkl_projection = array([ 0.72071588,  0.24425221,  0.5887681 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
