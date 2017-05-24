#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E364.589262131_hkl-7.1066716123,2.87055145646,-2.86717852894/sample/sampleassembly.xml'
psi = -0.010033320617558784
hkl2Q = array([[ -6.51272887e-01,   9.40925076e-01,   7.72555148e-17],
       [  6.65334502e-01,   4.60519475e-01,  -8.09165116e-01],
       [ -6.65334502e-01,  -4.60519475e-01,  -8.09165116e-01]])
pp = array([  2.61222502e+00,   1.47522217e+00,   9.95487405e-04])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0019700751571830669
Q = array([  8.44589226e+00,  -4.04450912e+00,  -2.72925528e-03])
E = 364.5892621314398
hkl_projection = array([ 0.0259077 , -0.69978963,  0.39549823])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
