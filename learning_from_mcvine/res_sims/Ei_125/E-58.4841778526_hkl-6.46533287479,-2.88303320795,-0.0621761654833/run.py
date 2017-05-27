#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-58.4841778526_hkl-6.46533287479,-2.88303320795,-0.0621761654833/sample/sampleassembly.xml'
psi = -0.0015741517245283394
hkl2Q = array([[-0.65920893,  0.93538225,  0.        ],
       [ 0.66141513,  0.46613111, -0.80916512],
       [-0.66141513, -0.46613111, -0.80916512]])
pp = array([ 1.77602815,  2.41779321, -0.78261886])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033053346671148569
Q = array([ 2.39624767, -7.36244682,  2.38316069])
E = -58.484177852550303
hkl_projection = array([-0.43556873,  0.60675889,  0.94656741])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
