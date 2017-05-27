#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-82.7395411168_hkl-9.08188511456,1.25312256984,2.62319157225/sample/sampleassembly.xml'
psi = -0.0026846639543168798
hkl2Q = array([[-0.65816978,  0.93611373,  0.        ],
       [ 0.66193237,  0.46539631, -0.80916512],
       [-0.66193237, -0.46539631, -0.80916512]])
pp = array([ 0.85977252,  2.87415922,  0.98640188])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032832390192588587
Q = array([ 5.07052926, -9.13930242, -3.13657818])
E = -82.739541116803025
hkl_projection = array([ 0.14685945,  0.84827336, -0.37060823])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
