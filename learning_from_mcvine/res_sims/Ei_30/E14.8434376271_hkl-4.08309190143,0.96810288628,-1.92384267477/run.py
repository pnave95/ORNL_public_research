#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E14.8434376271_hkl-4.08309190143,0.96810288628,-1.92384267477/sample/sampleassembly.xml'
psi = -0.006873574665779843
hkl2Q = array([[-0.65424272,  0.93886253,  0.        ],
       [ 0.66387606,  0.46261946, -0.80916512],
       [-0.66387606, -0.46261946, -0.80916512]])
pp = array([-0.88670545,  2.86596466, -0.88812505])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0075121161532785584
Q = array([ 4.59122655, -2.49559168,  0.7733513 ])
E = 14.843437627104421
hkl_projection = array([-0.75863585, -0.47985417,  0.14623229])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
