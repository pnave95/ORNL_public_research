#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E56.9765640518_hkl-3.1631137894,2.02867791029,-2.04974251847/sample/sampleassembly.xml'
psi = -0.02069965598758298
hkl2Q = array([[-0.64119981,  0.94781811,  0.        ],
       [ 0.67020862,  0.45339673, -0.80916512],
       [-0.67020862, -0.45339673, -0.80916512]])
pp = array([ 1.46894777,  2.61575848, -0.03880616])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076368903220876633
Q = array([ 4.76158046, -1.14891405,  0.01704475])
E = 56.97656405182812
hkl_projection = array([-0.37038766,  0.70476154,  0.32605995])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
