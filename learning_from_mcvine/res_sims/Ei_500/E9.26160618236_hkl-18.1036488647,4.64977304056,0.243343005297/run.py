#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E9.26160618236_hkl-18.1036488647,4.64977304056,0.243343005297/sample/sampleassembly.xml'
psi = -0.004725554653026366
hkl2Q = array([[-0.6562579 ,  0.93745503,  0.        ],
       [ 0.66288081,  0.46404441, -0.80916512],
       [-0.66288081, -0.46404441, -0.80916512]])
pp = array([ 0.16176503,  2.9956355 ,  0.79460519])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017095131726002069
Q = array([ 14.8016005 , -14.92657753,  -3.95933882])
E = 9.2616061823587756
hkl_projection = array([-0.41924346, -0.24247798, -0.05853629])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
