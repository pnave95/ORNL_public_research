#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp26/sample/sampleassembly.xml'
psi = 0.5626104078433408
hkl2Q = array([[ -1.05722205e+00,   4.37924542e-01,  -3.43786109e-17],
       [  3.09659413e-01,   7.47568882e-01,  -8.09165116e-01],
       [ -3.09659413e-01,  -7.47568882e-01,  -8.09165116e-01]])
pp = array([  1.79991580e+00,   2.40006315e+00,  -1.88413366e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0030620172369440831
Q = array([  8.41068959e+00,  -3.48389194e+00,   2.73497724e-16])
E = 212.5
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
