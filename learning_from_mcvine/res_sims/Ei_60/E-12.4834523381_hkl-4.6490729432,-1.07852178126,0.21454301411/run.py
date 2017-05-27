#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-12.4834523381_hkl-4.6490729432,-1.07852178126,0.21454301411/sample/sampleassembly.xml'
psi = -0.0021307981658341417
hkl2Q = array([[ -6.58688155e-01,   9.35749050e-01,  -7.76828479e-17],
       [  6.61674499e-01,   4.65762861e-01,  -8.09165116e-01],
       [ -6.61674499e-01,  -4.65762861e-01,  -8.09165116e-01]])
pp = array([ 1.62811849,  2.51976788, -0.35568465])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048289373571544086
Q = array([ 2.20670128, -4.95262715,  0.69910148])
E = -12.483452338111526
hkl_projection = array([-0.18614964,  0.93239622,  0.47452065])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
