#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E90.6174997475_hkl-12.7645936294,3.62185926779,-3.84379553674/sample/sampleassembly.xml'
psi = -0.005631771968089426
hkl2Q = array([[ -6.55408093e-01,   9.38049361e-01,  -7.74923518e-17],
       [  6.63301064e-01,   4.63443507e-01,  -8.09165116e-01],
       [ -6.63301064e-01,  -4.63443507e-01,  -8.09165116e-01]])
pp = array([-0.78067246,  2.8966447 , -0.06109865])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025082278506582578
Q = array([ 13.31799474,  -8.51390965,   0.17958309])
E = 90.617499747503018
hkl_projection = array([-0.56616996,  0.86651694, -0.02500422])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
