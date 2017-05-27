#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E211.269923586_hkl-5.20002608764,3.71348360823,-2.25332470729/sample/sampleassembly.xml'
psi = -0.012447245425776297
hkl2Q = array([[ -6.48999670e-01,   9.42494456e-01,   7.71268739e-17],
       [  6.66444221e-01,   4.58912067e-01,  -8.09165116e-01],
       [ -6.66444221e-01,  -4.58912067e-01,  -8.09165116e-01]])
pp = array([ 2.58496497,  1.52248354,  0.83173019])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030859246278273078
Q = array([ 7.35136013, -2.16275542, -1.18150965])
E = 211.26992358587739
hkl_projection = array([ 0.10220921, -0.46633944, -0.55365969])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
