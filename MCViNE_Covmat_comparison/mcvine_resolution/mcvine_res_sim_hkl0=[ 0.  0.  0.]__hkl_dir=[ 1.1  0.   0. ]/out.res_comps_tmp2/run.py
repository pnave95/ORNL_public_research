#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[ 1.1  0.   0. ]/out.res_comps_tmp2/sample/sampleassembly.xml'
psi = 0.16700705006496896
hkl2Q = array([[ -8.06805883e-01,   8.11517491e-01,   8.95749653e-17],
       [  5.73829521e-01,   5.70497911e-01,  -8.09165116e-01],
       [ -5.73829521e-01,  -5.70497911e-01,  -8.09165116e-01]])
pp = array([  2.20910278e+00,   2.02974504e+00,   2.24042419e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0074460568855004398
Q = array([  1.82320808e+00,  -1.83385531e+00,  -2.02420191e-16])
E = 15.0
hkl_projection = array([ 1.1,  0. ,  0. ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
