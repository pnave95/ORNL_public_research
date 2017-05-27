#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E27.4779919365_hkl-5.94690890195,1.81123102218,-1.86456450474/sample/sampleassembly.xml'
psi = -0.007827097097401658
hkl2Q = array([[ -6.53347192e-01,   9.39485933e-01,   7.73738579e-17],
       [  6.64316874e-01,   4.61986230e-01,  -8.09165116e-01],
       [ -6.64316874e-01,  -4.61986230e-01,  -8.09165116e-01]])
pp = array([-0.69101367,  2.91933213, -0.03239643])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0052131600427291697
Q = array([ 6.32728922, -3.88887034,  0.04315559])
E = 27.477991936484287
hkl_projection = array([-0.65584049, -0.83023528,  0.81481151])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
