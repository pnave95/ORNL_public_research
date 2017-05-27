#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-79.3222832094_hkl-12.2852535862,4.72120272178,-1.76091581445/sample/sampleassembly.xml'
psi = -0.007024581227721181
hkl2Q = array([[ -6.54100933e-01,   9.38961309e-01,  -7.74170889e-17],
       [  6.63945909e-01,   4.62519206e-01,  -8.09165116e-01],
       [ -6.63945909e-01,  -4.62519206e-01,  -8.09165116e-01]])
pp = array([-1.40739216,  2.64938621,  0.74335631])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032766449358077607
Q = array([ 12.33957192,  -8.53727348,  -2.3953609 ])
E = -79.322283209446852
hkl_projection = array([ 0.14386097, -0.98414369,  0.23981626])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
