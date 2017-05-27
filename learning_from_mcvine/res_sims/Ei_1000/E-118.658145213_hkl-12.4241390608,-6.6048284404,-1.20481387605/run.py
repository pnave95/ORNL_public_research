#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-118.658145213_hkl-12.4241390608,-6.6048284404,-1.20481387605/sample/sampleassembly.xml'
psi = -0.0017821269337407648
hkl2Q = array([[ -6.59014384e-01,   9.35519328e-01,   7.77019234e-17],
       [  6.61512061e-01,   4.65993540e-01,  -8.09165116e-01],
       [ -6.61512061e-01,  -4.65993540e-01,  -8.09165116e-01]])
pp = array([ 2.33206059,  1.88719194, -0.84343878])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011949413053741289
Q = array([  4.61551159, -14.13939413,   6.31929013])
E = -118.65814521276025
hkl_projection = array([-0.13204556, -0.61952473, -0.39857641])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
