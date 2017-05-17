#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/lj7/simulations/ARCS/beam/100meV-n1e10/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/2-fix-pixel-position-v2/tmp.use_res_comps/sample/sampleassembly.xml'
psi = 0.5198598086862193
hkl2Q = array([[ -1.03754027e+00,   4.82707535e-01,   3.50307614e-17],
       [  3.41325771e-01,   7.33651759e-01,  -8.09165116e-01],
       [ -3.41325771e-01,  -7.33651759e-01,  -8.09165116e-01]])
pp = array([  2.98854165e+00,   2.61951930e-01,   1.33560309e-17])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003884779248906272
Q = array([  7.55020156e-01,  -5.44370306e-01,  -2.77555756e-17])
E = 20.0
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
