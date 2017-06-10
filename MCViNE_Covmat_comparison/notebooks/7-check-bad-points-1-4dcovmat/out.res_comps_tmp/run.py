#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/7-check-bad-points-1-4dcovmat/out.res_comps_tmp/sample/sampleassembly.xml'
psi = 0.06294505139597527
hkl2Q = array([[ -7.18145613e-01,   8.90933920e-01,   8.15903957e-17],
       [  6.29985417e-01,   5.07805633e-01,  -8.09165116e-01],
       [ -6.29985417e-01,  -5.07805633e-01,  -8.09165116e-01]])
pp = array([  7.57386687e-01,   2.90282025e+00,   2.65835936e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034140655373103394
Q = array([  5.89597548e+00,  -7.31456748e+00,  -6.69857149e-16])
E = 7.8
hkl_projection = array([ 1.,  0.,  0.])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
