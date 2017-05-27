#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-720.689755027_hkl-19.024859224,-5.53378187435,6.09014541461/sample/sampleassembly.xml'
psi = -0.001143621430253761
hkl2Q = array([[-0.65961158,  0.93509835,  0.        ],
       [ 0.66121439,  0.46641582, -0.80916512],
       [-0.66121439, -0.46641582, -0.80916512]])
pp = array([ 1.78776165,  2.40913019,  0.04672498])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011478002935695235
Q = array([  4.86310958, -23.21169815,  -0.45018997])
E = -720.68975502724038
hkl_projection = array([ 0.68892591, -0.73394042, -0.43497274])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
