#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp16/sample/sampleassembly.xml'
psi = -0.08535172302928193
hkl2Q = array([[ -5.78624482e-01,   9.87263936e-01,   7.36293998e-17],
       [  6.98101024e-01,   4.09149295e-01,  -8.09165116e-01],
       [ -6.98101024e-01,  -4.09149295e-01,  -8.09165116e-01]])
pp = array([  2.41714158e+00,   1.77691490e+00,   1.32520973e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034876004578304949
Q = array([  2.35004200e+00,  -4.00970196e+00,  -2.99040548e-16])
E = 31.25
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
