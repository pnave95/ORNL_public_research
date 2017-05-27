#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E47.3007903593_hkl-4.67537358734,2.61553240193,-1.80561077852/sample/sampleassembly.xml'
psi = -0.012220121178770464
hkl2Q = array([[-0.64921372,  0.94234703,  0.        ],
       [ 0.66633997,  0.45906342, -0.80916512],
       [-0.66633997, -0.45906342, -0.80916512]])
pp = array([-0.70501481,  2.91598253,  0.80422004])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0059698885566085678
Q = array([ 5.98130109, -2.37623929, -0.65536032])
E = 47.300790359258315
hkl_projection = array([-0.6791045 ,  0.18214723,  0.73284844])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
