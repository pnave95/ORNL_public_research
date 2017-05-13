#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[2 0 0]/out.res_comps_tmp15/sample/sampleassembly.xml'
psi = 0.2706746872848944
hkl2Q = array([[ -8.86451896e-01,   7.23670786e-01,  -8.20029281e-17],
       [  5.11712520e-01,   6.26816147e-01,  -8.09165116e-01],
       [ -5.11712520e-01,  -6.26816147e-01,  -8.09165116e-01]])
pp = array([  2.16081394e+00,   2.08107740e+00,  -2.35817783e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0054044492423633364
Q = array([  2.92630757e+00,  -2.38894328e+00,   2.70703679e-16])
E = 36.0
hkl_projection = array([2, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
