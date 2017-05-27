#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-335.774357218_hkl-9.97964662106,0.559884988615,8.41809782849/sample/sampleassembly.xml'
psi = -0.0005854256423281478
hkl2Q = array([[ -6.60133449e-01,   9.34730015e-01,  -7.77675371e-17],
       [  6.60953932e-01,   4.66784838e-01,  -8.09165116e-01],
       [ -6.60953932e-01,  -4.66784838e-01,  -8.09165116e-01]])
pp = array([ 2.54053413,  1.5955207 ,  0.89185921])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011779408594380508
Q = array([  1.39398187, -12.99636984,  -7.26467051])
E = -335.77435721806421
hkl_projection = array([ 0.24819697,  0.91918893, -0.23071391])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
