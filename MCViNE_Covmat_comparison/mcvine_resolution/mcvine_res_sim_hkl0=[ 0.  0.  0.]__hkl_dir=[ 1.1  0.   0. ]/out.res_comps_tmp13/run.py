#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp13/sample/sampleassembly.xml'
psi = 0.12431927074402957
hkl2Q = array([[ -7.71439536e-01,   8.45208503e-01,   8.60044011e-17],
       [  5.97652664e-01,   5.45490127e-01,  -8.09165116e-01],
       [ -5.97652664e-01,  -5.45490127e-01,  -8.09165116e-01]])
pp = array([  2.98954560e-01,   2.98506720e+00,   3.03746254e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049090310669732719
Q = array([  4.87217474e+00,  -5.33807684e+00,  -5.43177334e-16])
E = 0.9375
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
