#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-34.4515267519_hkl-4.85297019704,-0.979785494561,1.35777555794/sample/sampleassembly.xml'
psi = -0.0014048753429541394
hkl2Q = array([[-0.65936726,  0.93527065,  0.        ],
       [ 0.66133622,  0.46624306, -0.80916512],
       [-0.66133622, -0.46624306, -0.80916512]])
pp = array([ 1.66420269,  2.49608281,  0.13563366])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047251947789741996
Q = array([ 1.6539759 , -5.6287122 , -0.30585637])
E = -34.451526751896154
hkl_projection = array([-0.01853233,  0.67665004,  0.95801703])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
