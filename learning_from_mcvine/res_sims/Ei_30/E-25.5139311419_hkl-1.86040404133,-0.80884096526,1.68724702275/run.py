#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-25.5139311419_hkl-1.86040404133,-0.80884096526,1.68724702275/sample/sampleassembly.xml'
psi = 0.0005348424656531234
hkl2Q = array([[-0.66118018,  0.9339899 ,  0.        ],
       [ 0.66043059,  0.46752499, -0.80916512],
       [-0.66043059, -0.46752499, -0.80916512]])
pp = array([ 2.47450271,  1.69612391,  0.41505571])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006615604632421032
Q = array([-0.41843059, -2.9045821 , -0.71077554])
E = -25.513931141906905
hkl_projection = array([-0.65786488, -0.18841905, -0.09375211])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
