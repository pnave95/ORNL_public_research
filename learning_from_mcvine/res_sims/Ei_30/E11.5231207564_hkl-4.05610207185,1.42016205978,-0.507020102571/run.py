#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E11.5231207564_hkl-4.05610207185,1.42016205978,-0.507020102571/sample/sampleassembly.xml'
psi = -0.005042892362271931
hkl2Q = array([[ -6.55960377e-01,   9.37663242e-01,  -7.75242623e-17],
       [  6.63028037e-01,   4.63834031e-01,  -8.09165116e-01],
       [ -6.63028037e-01,  -4.63834031e-01,  -8.09165116e-01]])
pp = array([-0.12292008,  2.99748072,  0.76126106])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073245050967608834
Q = array([ 3.93841805, -2.90936515, -0.73888262])
E = 11.523120756429833
hkl_projection = array([-0.22225126, -0.56413174, -0.26610783])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
