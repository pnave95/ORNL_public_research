#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp9/sample/sampleassembly.xml'
psi = 0.6305660663877665
hkl2Q = array([[ -1.08451843e+00,   3.65124832e-01,  -3.35133313e-17],
       [  2.58182244e-01,   7.66870337e-01,  -8.09165116e-01],
       [ -2.58182244e-01,  -7.66870337e-01,  -8.09165116e-01]])
pp = array([  1.63529921e+00,   2.51511361e+00,  -2.30852105e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066957415871206219
Q = array([  4.43579219e+00,  -1.49339820e+00,   1.37072980e-16])
E = 54.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
