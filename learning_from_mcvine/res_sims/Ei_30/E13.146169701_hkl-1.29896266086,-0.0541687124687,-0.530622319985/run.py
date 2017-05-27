#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E13.146169701_hkl-1.29896266086,-0.0541687124687,-0.530622319985/sample/sampleassembly.xml'
psi = -0.004366350989613486
hkl2Q = array([[ -6.56594595e-01,   9.37219243e-01,  -7.75609887e-17],
       [  6.62714082e-01,   4.64282490e-01,  -8.09165116e-01],
       [ -6.62714082e-01,  -4.64282490e-01,  -8.09165116e-01]])
pp = array([ 2.80819303,  1.05548658, -0.5013516 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073709169053544034
Q = array([ 1.16864438, -0.99620373,  0.4731925 ])
E = 13.146169701034374
hkl_projection = array([-0.55498942,  0.79549154,  0.11221408])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
