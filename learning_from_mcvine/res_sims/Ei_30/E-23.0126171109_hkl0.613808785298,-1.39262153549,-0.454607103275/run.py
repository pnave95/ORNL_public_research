#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-23.0126171109_hkl0.613808785298,-1.39262153549,-0.454607103275/sample/sampleassembly.xml'
psi = -0.02555742648301806
hkl2Q = array([[-0.63658798,  0.95092172,  0.        ],
       [ 0.6724032 ,  0.45013568, -0.80916512],
       [-0.6724032 , -0.45013568, -0.80916512]])
pp = array([ 2.9983327 , -0.10000496, -0.9258494 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066719376907780374
Q = array([-1.0214672 ,  0.16145035,  1.49471298])
E = -23.01261711093364
hkl_projection = array([ 0.58173359, -0.40262154,  0.27576893])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
