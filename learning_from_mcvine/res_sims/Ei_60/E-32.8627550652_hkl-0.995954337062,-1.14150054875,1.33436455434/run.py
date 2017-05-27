#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-32.8627550652_hkl-0.995954337062,-1.14150054875,1.33436455434/sample/sampleassembly.xml'
psi = 0.002227358285725031
hkl2Q = array([[ -6.62760028e-01,   9.32869507e-01,   7.79226361e-17],
       [  6.59638354e-01,   4.68642110e-01,  -8.09165116e-01],
       [ -6.59638354e-01,  -4.68642110e-01,  -8.09165116e-01]])
pp = array([ 2.85100252,  0.93369409,  0.06973863])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047306243802726555
Q = array([-0.97309686, -2.08939008, -0.15605883])
E = -32.862755065212966
hkl_projection = array([ 0.48493801,  0.83424001,  0.98209325])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
