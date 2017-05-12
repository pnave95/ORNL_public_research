#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp11/sample/sampleassembly.xml'
psi = 0.04881981954017726
hkl2Q = array([[ -7.05489741e-01,   9.00988677e-01,  -8.06798720e-17],
       [  6.37095203e-01,   4.98856580e-01,  -8.09165116e-01],
       [ -6.37095203e-01,  -4.98856580e-01,  -8.09165116e-01]])
pp = array([  8.43004416e-01,   2.87912201e+00,  -2.57813668e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049307448827922342
Q = array([  3.93524840e+00,  -5.02574884e+00,   4.50035370e-16])
E = 3.75
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
