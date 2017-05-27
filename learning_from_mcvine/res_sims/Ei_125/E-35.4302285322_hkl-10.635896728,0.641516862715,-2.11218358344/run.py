#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-35.4302285322_hkl-10.635896728,0.641516862715,-2.11218358344/sample/sampleassembly.xml'
psi = -0.004908289973287029
hkl2Q = array([[-0.65608658,  0.93757494,  0.        ],
       [ 0.6629656 ,  0.46392327, -0.80916512],
       [-0.6629656 , -0.46392327, -0.80916512]])
pp = array([-0.34252709,  2.98038172, -0.40792608])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033281994515085341
Q = array([ 8.8036778 , -8.69444451,  1.19001221])
E = -35.430228532188281
hkl_projection = array([ 0.58257016, -0.04893805,  0.98156215])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
