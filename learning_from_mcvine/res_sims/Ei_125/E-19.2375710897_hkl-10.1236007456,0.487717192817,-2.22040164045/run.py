#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-19.2375710897_hkl-10.1236007456,0.487717192817,-2.22040164045/sample/sampleassembly.xml'
psi = -0.0049660511163882514
hkl2Q = array([[ -6.56032426e-01,   9.37612834e-01,   7.75284301e-17],
       [  6.62992393e-01,   4.63884977e-01,  -8.09165116e-01],
       [ -6.62992393e-01,  -4.63884977e-01,  -8.09165116e-01]])
pp = array([-0.22969349,  2.99119389, -0.50921054])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033606065965359308
Q = array([ 8.43687255, -8.23576235,  1.40202781])
E = -19.237571089728178
hkl_projection = array([ 0.6200121 ,  0.34440627,  0.24945512])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
