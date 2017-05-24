#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-0.72930464112_hkl0.149540562332,0.397946785288,0.254473376786/sample/sampleassembly.xml'
psi = -7.17121808315304e-05
hkl2Q = array([[-0.66061355,  0.93439077,  0.        ],
       [ 0.66071405,  0.46712432, -0.80916512],
       [-0.66071405, -0.46712432, -0.80916512]])
pp = array([ 2.99562281, -0.16199993,  0.41365228])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0069326360346128506
Q = array([-0.00399362,  0.20674924, -0.52791564])
E = -0.72930464111981053
hkl_projection = array([ 0.07624505,  0.39887239, -0.94314267])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
