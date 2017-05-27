#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-35.3972059147_hkl-4.61543263534,-2.16120554489,0.7356388646/sample/sampleassembly.xml'
psi = -0.0009642660186498889
hkl2Q = array([[-0.65977929,  0.93498003,  0.        ],
       [ 0.66113072,  0.46653441, -0.80916512],
       [-0.66113072, -0.46653441, -0.80916512]])
pp = array([ 2.28691473,  1.94165419, -0.39523695])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033279522969667024
Q = array([ 1.12997403, -5.66681495,  1.15351883])
E = -35.397205914700152
hkl_projection = array([-0.05508946,  0.25590818,  0.15733841])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
