#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-157.137365384_hkl-0.638150097349,0.122763401731,2.95926965615/sample/sampleassembly.xml'
psi = 0.004096973496966528
hkl2Q = array([[ -6.64502976e-01,   9.31628771e-01,  -7.80264129e-17],
       [  6.58761021e-01,   4.69874560e-01,  -8.09165116e-01],
       [ -6.58761021e-01,  -4.69874560e-01,  -8.09165116e-01]])
pp = array([ 2.98998884,  0.24488108,  0.31686597])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011847562263868317
Q = array([-1.44452712, -1.92732112, -2.49387364])
E = -157.13736538411501
hkl_projection = array([-0.17557053,  0.86881483, -0.03744199])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
