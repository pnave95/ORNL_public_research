#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-105.842797827_hkl0.728607667739,-3.59132617053,-3.82661603247/sample/sampleassembly.xml'
psi = -0.002236511515776535
hkl2Q = array([[ -6.58589231e-01,   9.35818677e-01,   7.76770681e-17],
       [  6.61723733e-01,   4.65692911e-01,  -8.09165116e-01],
       [ -6.61723733e-01,  -4.65692911e-01,  -8.09165116e-01]])
pp = array([ 2.99813134, -0.10586998, -0.80294864])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011954211262203769
Q = array([-0.32415628,  0.79141748,  6.00234007])
E = -105.84279782716385
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
