#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-214.657643697_hkl-3.75801698647,-6.01621181782,-0.433330925487/sample/sampleassembly.xml'
psi = 0.0009321686093905106
hkl2Q = array([[-0.66155123,  0.93372712,  0.        ],
       [ 0.66024478,  0.46778736, -0.80916512],
       [-0.66024478, -0.46778736, -0.80916512]])
pp = array([ 2.8189106 ,  1.02651986, -0.87526996])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016571407465685636
Q = array([-1.19994722, -6.12056351,  5.21874501])
E = -214.65764369748257
hkl_projection = array([ 0.31258406, -0.42534068,  0.25743187])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
