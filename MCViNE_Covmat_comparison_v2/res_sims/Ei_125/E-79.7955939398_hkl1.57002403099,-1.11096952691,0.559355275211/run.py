#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_125/E-79.7955939398_hkl1.57002403099,-1.11096952691,0.559355275211/sample/sampleassembly.xml'
psi = -0.014668897961991417
hkl2Q = array([[-0.64690417,  0.94393398,  0.        ],
       [ 0.66746212,  0.45743033, -0.80916512],
       [-0.66746212, -0.45743033, -0.80916512]])
pp = array([ 2.99219741, -0.21622822, -0.13442986])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032621064632756764
Q = array([-2.13053363,  0.71794181,  0.44634701])
E = -79.795593939789427
hkl_projection = array([ 0.3422508 , -0.36240297, -0.6189983 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
