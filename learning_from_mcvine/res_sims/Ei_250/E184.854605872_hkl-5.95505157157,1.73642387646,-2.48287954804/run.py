#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E184.854605872_hkl-5.95505157157,1.73642387646,-2.48287954804/sample/sampleassembly.xml'
psi = -0.0066408831907794775
hkl2Q = array([[ -6.54461163e-01,   9.38710263e-01,  -7.74377931e-17],
       [  6.63768392e-01,   4.62773926e-01,  -8.09165116e-01],
       [ -6.63768392e-01,  -4.62773926e-01,  -8.09165116e-01]])
pp = array([ 2.29603573,  1.93085989, -0.32062014])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0028109458896636089
Q = array([ 6.69799023, -3.63748441,  0.60400589])
E = 184.85460587200708
hkl_projection = array([-0.88385804,  0.11830076, -0.77683774])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
