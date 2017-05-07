#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp13/sample/sampleassembly.xml'
psi = 0.17858362850005566
hkl2Q = array([[ -8.16146207e-01,   8.02123270e-01,  -8.90669472e-17],
       [  5.67186803e-01,   5.77102517e-01,  -8.09165116e-01],
       [ -5.67186803e-01,  -5.77102517e-01,  -8.09165116e-01]])
pp = array([ -4.04934181e-02,   2.99972670e+00,  -3.33086584e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0049055610580797052
Q = array([  5.47948007e+00,  -5.38533223e+00,   5.97981781e-16])
E = 0.46875
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
