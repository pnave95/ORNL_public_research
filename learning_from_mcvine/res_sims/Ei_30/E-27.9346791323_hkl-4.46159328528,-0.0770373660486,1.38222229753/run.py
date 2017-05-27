#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-27.9346791323_hkl-4.46159328528,-0.0770373660486,1.38222229753/sample/sampleassembly.xml'
psi = -0.001512168470448398
hkl2Q = array([[-0.65926691,  0.93534139,  0.        ],
       [ 0.66138624,  0.4661721 , -0.80916512],
       [-0.66138624, -0.4661721 , -0.80916512]])
pp = array([ 1.06493662,  2.80462297,  0.61029454])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066059520404611214
Q = array([ 1.97624657, -4.853379  , -1.05611012])
E = -27.934679132301035
hkl_projection = array([-0.33009297,  0.01654918,  0.57636559])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
