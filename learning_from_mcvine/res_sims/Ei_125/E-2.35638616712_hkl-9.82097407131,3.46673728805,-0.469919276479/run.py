#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-2.35638616712_hkl-9.82097407131,3.46673728805,-0.469919276479/sample/sampleassembly.xml'
psi = -0.005939515961019667
hkl2Q = array([[-0.65511938,  0.93825101,  0.        ],
       [ 0.66344365,  0.46323936, -0.80916512],
       [-0.66344365, -0.46323936, -0.80916512]])
pp = array([-0.49685393,  2.95856995,  0.97069008])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003419533912306749
Q = array([ 9.04566029, -7.39092463, -2.4249206 ])
E = -2.3563861671244126
hkl_projection = array([-0.45372669,  0.98673359, -0.0261484 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
