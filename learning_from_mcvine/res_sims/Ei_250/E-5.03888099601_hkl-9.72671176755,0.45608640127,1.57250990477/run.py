#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-5.03888099601_hkl-9.72671176755,0.45608640127,1.57250990477/sample/sampleassembly.xml'
psi = -0.0021129649032855828
hkl2Q = array([[-0.65870484,  0.9357373 ,  0.        ],
       [ 0.66166619,  0.46577466, -0.80916512],
       [-0.66166619, -0.46577466, -0.80916512]])
pp = array([ 1.45895291,  2.6213463 ,  0.44720606])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024005720392112021
Q = array([ 5.66833246, -9.62164882, -1.64146937])
E = -5.0388809960060144
hkl_projection = array([-0.35796635,  0.14003973, -0.08687868])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
