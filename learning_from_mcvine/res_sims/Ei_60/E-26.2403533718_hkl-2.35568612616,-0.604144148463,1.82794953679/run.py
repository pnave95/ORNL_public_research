#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-26.2403533718_hkl-2.35568612616,-0.604144148463,1.82794953679/sample/sampleassembly.xml'
psi = 7.196129851819099e-05
hkl2Q = array([[-0.66074779,  0.93429585,  0.        ],
       [ 0.66064693,  0.46721924, -0.80916512],
       [-0.66064693, -0.46721924, -0.80916512]])
pp = array([ 2.55934858,  1.56516289,  0.46443301])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047657673608995392
Q = array([-0.05024084, -3.33722873, -0.99026063])
E = -26.240353371811647
hkl_projection = array([-0.39520831, -0.53790517, -0.90139159])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
