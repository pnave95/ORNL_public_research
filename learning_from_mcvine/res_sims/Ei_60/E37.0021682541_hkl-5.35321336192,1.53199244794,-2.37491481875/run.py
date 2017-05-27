#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E37.0021682541_hkl-5.35321336192,1.53199244794,-2.37491481875/sample/sampleassembly.xml'
psi = -0.009083098155232198
hkl2Q = array([[-0.65216668,  0.9403058 ,  0.        ],
       [ 0.66489661,  0.46115148, -0.80916512],
       [-0.66489661, -0.46115148, -0.80916512]])
pp = array([-0.61948923,  2.93534207, -0.61946188])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0054633554535576763
Q = array([ 6.08887677, -3.23198148,  0.68206338])
E = 37.002168254082207
hkl_projection = array([-0.63852928, -0.05088739,  0.4562559 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
