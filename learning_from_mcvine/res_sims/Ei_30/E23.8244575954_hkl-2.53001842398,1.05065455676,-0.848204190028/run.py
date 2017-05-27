#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E23.8244575954_hkl-2.53001842398,1.05065455676,-0.848204190028/sample/sampleassembly.xml'
psi = -0.007276192913418523
hkl2Q = array([[-0.65386466,  0.93912586,  0.        ],
       [ 0.66406226,  0.46235213, -0.80916512],
       [-0.66406226, -0.46235213, -0.80916512]])
pp = array([ 1.54981514,  2.56867145,  0.28088841])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0084114645935456523
Q = array([ 2.91525007, -1.49806433, -0.16381577])
E = 23.824457595441096
hkl_projection = array([ 0.32886327,  0.99561239, -0.57297307])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
