#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp5/sample/sampleassembly.xml'
psi = 0.14926254213785864
hkl2Q = array([[ -7.92279645e-01,   8.25705356e-01,   8.80358236e-17],
       [  5.83861857e-01,   5.60226310e-01,  -8.09165116e-01],
       [ -5.83861857e-01,  -5.60226310e-01,  -8.09165116e-01]])
pp = array([  1.48512141e-01,   2.99632177e+00,   3.19464629e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069455467385374867
Q = array([  3.63152179e+00,  -3.78473310e+00,  -4.03524203e-16])
E = 0.46875
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
