#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp1/sample/sampleassembly.xml'
psi = 0.6326227321813352
hkl2Q = array([[ -1.08526708e+00,   3.62893569e-01,   3.34902130e-17],
       [  2.56604504e-01,   7.67399710e-01,  -8.09165116e-01],
       [ -2.56604504e-01,  -7.67399710e-01,  -8.09165116e-01]])
pp = array([  1.60312750e+00,   2.53574096e+00,   2.34014907e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0095085381805373338
Q = array([  3.15264166e+00,  -1.05418602e+00,  -9.72872420e-17])
E = 27.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
