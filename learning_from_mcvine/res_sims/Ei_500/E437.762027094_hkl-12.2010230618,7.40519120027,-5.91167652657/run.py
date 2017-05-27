#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E437.762027094_hkl-12.2010230618,7.40519120027,-5.91167652657/sample/sampleassembly.xml'
psi = -0.015036804215148112
hkl2Q = array([[-0.64655685,  0.94417192,  0.        ],
       [ 0.66763037,  0.45718473, -0.80916512],
       [-0.66763037, -0.45718473, -0.80916512]])
pp = array([-0.63263776,  2.93253635,  0.65247322])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022482683051590065
Q = array([ 16.77940032,  -5.43159471,  -1.20849997])
E = 437.76202709383153
hkl_projection = array([ 0.76385291,  0.55714022,  0.93444095])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
