#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E30.1356075302_hkl-3.74490029574,0.609492535018,-0.367046388064/sample/sampleassembly.xml'
psi = -0.004864832077556679
hkl2Q = array([[-0.65612733,  0.93754643,  0.        ],
       [ 0.66294544,  0.46395208, -0.80916512],
       [-0.66294544, -0.46395208, -0.80916512]])
pp = array([ 1.8044095 ,  2.39668654,  0.1537564 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0052656785739456455
Q = array([ 3.10452344, -3.05795062, -0.19617896])
E = 30.135607530233131
hkl_projection = array([ 0.79841194,  0.12960487,  0.91766598])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
