#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp17/sample/sampleassembly.xml'
psi = 0.0630672342499029
hkl2Q = array([[ -7.18254464e-01,   8.90846168e-01,  -8.15984327e-17],
       [  6.29923367e-01,   5.07882602e-01,  -8.09165116e-01],
       [ -6.29923367e-01,  -5.07882602e-01,  -8.09165116e-01]])
pp = array([  7.56852715e-01,   2.90295952e+00,  -2.65901067e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034140988087274474
Q = array([  5.89742166e+00,  -7.31453231e+00,   6.69985900e-16])
E = 7.8125
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
