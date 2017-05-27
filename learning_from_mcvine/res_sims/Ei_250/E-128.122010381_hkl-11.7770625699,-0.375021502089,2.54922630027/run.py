#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-128.122010381_hkl-11.7770625699,-0.375021502089,2.54922630027/sample/sampleassembly.xml'
psi = -0.0016880832446320181
hkl2Q = array([[-0.65910236,  0.93545735,  0.        ],
       [ 0.66146823,  0.46605575, -0.80916512],
       [-0.66146823, -0.46605575, -0.80916512]])
pp = array([ 1.16092014,  2.76627266,  0.39311433])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023227601707812677
Q = array([  5.82799272, -12.37980221,  -1.75929068])
E = -128.12201038062474
hkl_projection = array([-0.81667722, -0.12341556, -0.39748026])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
