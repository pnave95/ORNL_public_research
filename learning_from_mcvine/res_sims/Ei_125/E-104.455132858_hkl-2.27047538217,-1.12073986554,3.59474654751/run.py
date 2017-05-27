#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-104.455132858_hkl-2.27047538217,-1.12073986554,3.59474654751/sample/sampleassembly.xml'
psi = 0.0017969548962820372
hkl2Q = array([[-0.66235846,  0.93315467,  0.        ],
       [ 0.65984   ,  0.46835816, -0.80916512],
       [-0.65984   , -0.46835816, -0.80916512]])
pp = array([ 2.72572424,  1.25316694,  0.57974344])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032437170023484211
Q = array([-1.60759798, -4.32724124, -2.0018799 ])
E = -104.4551328577852
hkl_projection = array([ 0.86713603, -0.970857  ,  0.24613383])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
