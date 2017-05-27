#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E81.0096337609_hkl-7.8705552051,3.71776741741,-3.17431078269/sample/sampleassembly.xml'
psi = -0.011205205190712372
hkl2Q = array([[ -6.50169785e-01,   9.41687646e-01,  -7.71929540e-17],
       [  6.65873720e-01,   4.59739464e-01,  -8.09165116e-01],
       [ -6.65873720e-01,  -4.59739464e-01,  -8.09165116e-01]])
pp = array([-1.22713948,  2.73754063,  0.2837168 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0038084744620997166
Q = array([ 9.70645093, -4.24304427, -0.43974615])
E = 81.009633760882707
hkl_projection = array([-0.75199756, -0.22772139,  0.09989274])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
