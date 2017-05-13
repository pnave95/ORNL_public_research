#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp19/sample/sampleassembly.xml'
psi = 0.4942467218689372
hkl2Q = array([[ -1.02483768e+00,   5.09120911e-01,   3.54649583e-17],
       [  3.60002849e-01,   7.24669673e-01,  -8.09165116e-01],
       [ -3.60002849e-01,  -7.24669673e-01,  -8.09165116e-01]])
pp = array([  1.88485978e+00,   2.33394593e+00,   1.62580820e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0041234391568494887
Q = array([  5.56985743e+00,  -2.76700491e+00,  -1.92747364e-16])
E = 100.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
