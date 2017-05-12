#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp9/sample/sampleassembly.xml'
psi = -0.08163109080334247
hkl2Q = array([[ -5.82293715e-01,   9.85104259e-01,   7.37908201e-17],
       [  6.96573902e-01,   4.11743834e-01,  -8.09165116e-01],
       [ -6.96573902e-01,  -4.11743834e-01,  -8.09165116e-01]])
pp = array([  2.37600009e+00,   1.83156315e+00,   1.37196186e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050368563205903166
Q = array([  1.69245100e+00,  -2.86322975e+00,  -2.14474833e-16])
E = 15.0
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
