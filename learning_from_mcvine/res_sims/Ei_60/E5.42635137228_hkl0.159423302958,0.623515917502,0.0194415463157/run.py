#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E5.42635137228_hkl0.159423302958,0.623515917502,0.0194415463157/sample/sampleassembly.xml'
psi = 0.0032377900472408644
hkl2Q = array([[ -6.63702290e-01,   9.32199357e-01,   7.79786540e-17],
       [  6.59164487e-01,   4.69308390e-01,  -8.09165116e-01],
       [ -6.59164487e-01,  -4.69308390e-01,  -8.09165116e-01]])
pp = array([ 2.98934939, -0.25256726,  0.30408896])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.004949202612130086
Q = array([ 0.29237476,  0.43211147, -0.52025875])
E = 5.4263513722812107
hkl_projection = array([ 0.84703544,  0.45668914,  0.71382508])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
