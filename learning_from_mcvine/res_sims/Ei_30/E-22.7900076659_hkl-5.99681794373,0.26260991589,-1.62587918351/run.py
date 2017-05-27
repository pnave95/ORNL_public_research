#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-22.7900076659_hkl-5.99681794373,0.26260991589,-1.62587918351/sample/sampleassembly.xml'
psi = -0.00407265250809182
hkl2Q = array([[ -6.56869826e-01,   9.37026362e-01,   7.75769542e-17],
       [  6.62577695e-01,   4.64477109e-01,  -8.09165116e-01],
       [ -6.62577695e-01,  -4.64477109e-01,  -8.09165116e-01]])
pp = array([-0.83338865,  2.88192008, -0.67040565])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066533952658323226
Q = array([ 5.19039952, -4.74201654,  1.10310994])
E = -22.790007665865421
hkl_projection = array([ 0.25709716, -0.62793528, -0.73984131])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
