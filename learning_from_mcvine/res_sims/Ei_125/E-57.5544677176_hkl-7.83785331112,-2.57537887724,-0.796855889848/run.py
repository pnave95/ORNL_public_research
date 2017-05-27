#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-57.5544677176_hkl-7.83785331112,-2.57537887724,-0.796855889848/sample/sampleassembly.xml'
psi = -0.0023611219511523378
hkl2Q = array([[-0.65847261,  0.93590074,  0.        ],
       [ 0.66178176,  0.46561045, -0.80916512],
       [-0.66178176, -0.46561045, -0.80916512]])
pp = array([ 1.27160041,  2.7171736 , -0.90822447])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033123972504826289
Q = array([ 3.98401768, -8.16355158,  2.72869474])
E = -57.554467717588288
hkl_projection = array([ 0.46782089, -0.26248986,  0.60211481])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
