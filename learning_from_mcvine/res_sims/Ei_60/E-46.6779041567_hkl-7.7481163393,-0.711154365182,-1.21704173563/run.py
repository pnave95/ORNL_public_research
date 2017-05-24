#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-46.6779041567_hkl-7.7481163393,-0.711154365182,-1.21704173563/sample/sampleassembly.xml'
psi = -0.0036991406797516374
hkl2Q = array([[-0.65721977,  0.93678095,  0.        ],
       [ 0.66240416,  0.46472456, -0.80916512],
       [-0.66240416, -0.46472456, -0.80916512]])
pp = array([-0.00877113,  2.99998718, -0.66645889])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046993048389869776
Q = array([ 5.42731714, -7.02318948,  1.56022902])
E = -46.677904156744084
hkl_projection = array([-0.65810232, -0.32315093, -0.74318786])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
