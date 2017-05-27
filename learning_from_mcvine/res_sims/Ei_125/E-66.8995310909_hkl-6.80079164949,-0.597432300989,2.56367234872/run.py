#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-66.8995310909_hkl-6.80079164949,-0.597432300989,2.56367234872/sample/sampleassembly.xml'
psi = -0.0014772967981816888
hkl2Q = array([[ -6.59299528e-01,   9.35318397e-01,   7.77186158e-17],
       [  6.61369981e-01,   4.66195167e-01,  -8.09165116e-01],
       [ -6.61369981e-01,  -4.66195167e-01,  -8.09165116e-01]])
pp = array([ 1.70494492,  2.46843327,  0.50127772])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032841679413191686
Q = array([ 2.393099  , -7.83459725, -1.59101286])
E = -66.899531090927553
hkl_projection = array([-0.827161  , -0.24891832, -0.85271102])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
