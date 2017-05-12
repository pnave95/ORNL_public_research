#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp14/sample/sampleassembly.xml'
psi = 0.1415417723130882
hkl2Q = array([[ -7.85881014e-01,   8.31797694e-01,  -8.73910226e-17],
       [  5.88169790e-01,   5.55701794e-01,  -8.09165116e-01],
       [ -5.88169790e-01,  -5.55701794e-01,  -8.09165116e-01]])
pp = array([  1.82531852e-01,   2.99444187e+00,  -3.14604548e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049055610580797052
Q = array([  5.07908854e+00,  -5.37584451e+00,   5.64801457e-16])
E = 0.46875
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
