#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E17.3802352774_hkl-3.79405416534,0.981454459955,-1.41239280148/sample/sampleassembly.xml'
psi = -0.006199196529179681
hkl2Q = array([[ -6.54875715e-01,   9.38421105e-01,  -7.74616542e-17],
       [  6.63563927e-01,   4.63067059e-01,  -8.09165116e-01],
       [ -6.63563927e-01,  -4.63067059e-01,  -8.09165116e-01]])
pp = array([-0.30911589,  2.98403207, -0.42437665])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0076210914856683666
Q = array([ 4.07310462, -2.45190869,  0.34870027])
E = 17.380235277394029
hkl_projection = array([ 0.86325774, -0.28272552, -0.56290151])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
