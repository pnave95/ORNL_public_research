#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-487.184105381_hkl-28.8515658985,1.47527569873,0.751146868024/sample/sampleassembly.xml'
psi = -0.003978887124361384
hkl2Q = array([[ -6.56957684e-01,   9.36964766e-01,  -7.75820540e-17],
       [  6.62534140e-01,   4.64539233e-01,  -8.09165116e-01],
       [ -6.62534140e-01,  -4.64539233e-01,  -8.09165116e-01]])
pp = array([ 0.29677534,  2.98528464,  0.20145402])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011605595821342419
Q = array([ 19.43401799, -26.69651444,  -1.80154348])
E = -487.18410538068963
hkl_projection = array([ 0.49542276, -0.5838728 ,  0.99348908])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
