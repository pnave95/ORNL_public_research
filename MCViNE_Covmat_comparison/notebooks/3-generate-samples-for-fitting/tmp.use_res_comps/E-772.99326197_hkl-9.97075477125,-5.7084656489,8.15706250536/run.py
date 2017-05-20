#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-772.99326197_hkl-9.97075477125,-5.7084656489,8.15706250536/sample/sampleassembly.xml'
psi = 0.0008843373837425713
hkl2Q = array([[ -6.61506567e-01,   9.33758766e-01,  -7.78484270e-17],
       [  6.60267155e-01,   4.67755780e-01,  -8.09165116e-01],
       [ -6.60267155e-01,  -4.67755780e-01,  -8.09165116e-01]])
pp = array([ 2.52580234,  1.61874103,  0.20304195])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011457175811715858
Q = array([ -2.55923307, -15.7959606 ,  -1.98131916])
E = -772.99326197029404
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
