#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-332.670098157_hkl-9.89864831934,-0.872690086744,7.22117445991/sample/sampleassembly.xml'
psi = -0.000433001219147516
hkl2Q = array([[ -6.60275917e-01,   9.34629384e-01,  -7.77759103e-17],
       [  6.60882775e-01,   4.66885579e-01,  -8.09165116e-01],
       [ -6.60882775e-01,  -4.66885579e-01,  -8.09165116e-01]])
pp = array([ 2.2259124 ,  2.01129659,  0.79290843])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016359164311621054
Q = array([  1.18674344, -13.03047621,  -5.1369721 ])
E = -332.67009815710128
hkl_projection = array([-0.83395344,  0.40544048, -0.29039172])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
