#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-7.98574177896_hkl-1.2631196834,-0.985399386564,0.344825718364/sample/sampleassembly.xml'
psi = 9.102125241479965e-05
hkl2Q = array([[ -6.60765593e-01,   9.34283256e-01,  -7.78047243e-17],
       [  6.60638026e-01,   4.67231832e-01,  -8.09165116e-01],
       [ -6.60638026e-01,  -4.67231832e-01,  -8.09165116e-01]])
pp = array([ 2.71888109,  1.26794542, -0.36478751])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0068059207318674521
Q = array([-0.04417126, -1.80163508,  0.51832987])
E = -7.9857417789580012
hkl_projection = array([-0.94671581, -0.60236987,  0.47499947])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
