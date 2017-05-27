#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-180.930836424_hkl-16.9175965491,-2.44782051552,0.0818505233783/sample/sampleassembly.xml'
psi = -0.0026456629147946493
hkl2Q = array([[-0.65820628,  0.93608806,  0.        ],
       [ 0.66191422,  0.46542213, -0.80916512],
       [-0.66191422, -0.46542213, -0.80916512]])
pp = array([ 1.01936631,  2.82150533, -0.31748839])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016541555445703053
Q = array([  9.46084314, -17.01372504,   1.91446038])
E = -180.93083642404326
hkl_projection = array([ 0.28910953,  0.92294072, -0.89417261])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
