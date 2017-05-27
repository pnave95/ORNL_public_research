#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E88.1075971008_hkl-6.475914698,2.74545966025,-1.53532253065/sample/sampleassembly.xml'
psi = -0.00838063970304528
hkl2Q = array([[ -6.52827046e-01,   9.39847445e-01,  -7.73440961e-17],
       [  6.64572501e-01,   4.61618431e-01,  -8.09165116e-01],
       [ -6.64572501e-01,  -4.61618431e-01,  -8.09165116e-01]])
pp = array([ 0.52592863,  2.95354009,  0.70362747])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0039250366713658256
Q = array([ 7.07254239, -4.11028392, -0.97920075])
E = 88.107597100825814
hkl_projection = array([ 0.15626597, -0.81286378,  0.81019951])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
