#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp22/sample/sampleassembly.xml'
psi = 0.16823906274602948
hkl2Q = array([[ -8.07805071e-01,   8.10522880e-01,   8.96848848e-17],
       [  5.73126225e-01,   5.71204443e-01,  -8.09165116e-01],
       [ -5.73126225e-01,  -5.71204443e-01,  -8.09165116e-01]])
pp = array([  2.25049544e+00,   1.98375157e+00,   2.19503404e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025769761260387731
Q = array([  5.15527034e+00,  -5.17261493e+00,  -5.72353212e-16])
E = 125.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
