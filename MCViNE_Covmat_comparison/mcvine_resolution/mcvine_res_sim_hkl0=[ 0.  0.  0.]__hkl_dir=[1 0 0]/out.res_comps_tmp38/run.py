#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp38/sample/sampleassembly.xml'
psi = 0.07540899193906457
hkl2Q = array([[ -7.29194092e-01,   8.81914025e-01,   8.24248725e-17],
       [  6.23607388e-01,   5.15618087e-01,  -8.09165116e-01],
       [ -6.23607388e-01,  -5.15618087e-01,  -8.09165116e-01]])
pp = array([  6.81655566e-01,   2.92153139e+00,   2.73050259e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012056677730521118
Q = array([  1.72268053e+01,  -2.08347289e+01,  -1.94724182e-15])
E = 62.5
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
