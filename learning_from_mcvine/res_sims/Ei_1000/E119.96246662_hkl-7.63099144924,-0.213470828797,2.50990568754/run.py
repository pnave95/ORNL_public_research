#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E119.96246662_hkl-7.63099144924,-0.213470828797,2.50990568754/sample/sampleassembly.xml'
psi = -0.002093873265282223
hkl2Q = array([[ -6.58722707e-01,   9.35724728e-01,  -7.76848671e-17],
       [  6.61657300e-01,   4.65787293e-01,  -8.09165116e-01],
       [ -6.61657300e-01,  -4.65787293e-01,  -8.09165116e-01]])
pp = array([ 2.74006545,  1.22149144,  0.26992073])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001213665470470116
Q = array([ 3.22476539, -8.40902157, -1.85819498])
E = 119.96246662033309
hkl_projection = array([-0.12276689, -0.28295518, -0.31831243])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
