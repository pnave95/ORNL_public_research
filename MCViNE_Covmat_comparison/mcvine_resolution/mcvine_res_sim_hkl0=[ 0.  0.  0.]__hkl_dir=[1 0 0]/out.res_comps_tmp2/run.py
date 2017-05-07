#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/mcvine_res_sim_hkl0=[ 0.  0.  0.]__hkl_dir=[1 0 0]/out.res_comps_tmp2/sample/sampleassembly.xml'
psi = 0.16908232898568648
hkl2Q = array([[ -8.08488270e-01,   8.09841397e-01,   8.97603547e-17],
       [  5.72644344e-01,   5.71687538e-01,  -8.09165116e-01],
       [ -5.72644344e-01,  -5.71687538e-01,  -8.09165116e-01]])
pp = array([  2.27666356e+00,   1.95366400e+00,   2.16538170e-16])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.007446056885500439
Q = array([  1.76216756e+00,  -1.76511681e+00,  -1.95640173e-16])
E = 15.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
