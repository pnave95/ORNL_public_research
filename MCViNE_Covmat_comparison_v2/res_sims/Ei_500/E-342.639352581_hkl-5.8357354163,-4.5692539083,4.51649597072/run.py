#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_500/E-342.639352581_hkl-5.8357354163,-4.5692539083,4.51649597072/sample/sampleassembly.xml'
psi = 0.0010476227682867686
hkl2Q = array([[-0.66165903,  0.93365074,  0.        ],
       [ 0.66019077,  0.46786359, -0.80916512],
       [-0.66019077, -0.46786359, -0.80916512]])
pp = array([ 2.63240706,  1.43889995, -0.006333  ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001626379987730056
Q = array([-2.13706118, -9.6994302 ,  0.04268988])
E = -342.63935258139929
hkl_projection = array([ 0.86112605,  0.40484789,  0.17328778])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
