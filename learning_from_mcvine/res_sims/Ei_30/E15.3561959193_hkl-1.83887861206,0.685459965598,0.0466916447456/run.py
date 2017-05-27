#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E15.3561959193_hkl-1.83887861206,0.685459965598,0.0466916447456/sample/sampleassembly.xml'
psi = -0.004254248029922347
hkl2Q = array([[-0.65669966,  0.93714563,  0.        ],
       [ 0.66266203,  0.46435678, -0.80916512],
       [-0.66266203, -0.46435678, -0.80916512]])
pp = array([ 2.51305656,  1.63845865,  0.68037271])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0075121640748796754
Q = array([ 1.63087846, -1.42668066, -0.59243154])
E = 15.356195919269865
hkl_projection = array([ 0.13820318,  0.45843272,  0.60392   ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
