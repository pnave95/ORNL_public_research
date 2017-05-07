#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp23/sample/sampleassembly.xml'
psi = -0.08143244288700707
hkl2Q = array([[ -5.82489392e-01,   9.84988568e-01,   7.37994871e-17],
       [  6.96492096e-01,   4.11882199e-01,  -8.09165116e-01],
       [ -6.96492096e-01,  -4.11882199e-01,  -8.09165116e-01]])
pp = array([  2.37974858e+00,   1.82669010e+00,   1.36863306e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002466379821382723
Q = array([  3.44161944e+00,  -5.81977260e+00,  -4.36041845e-16])
E = 62.5
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
