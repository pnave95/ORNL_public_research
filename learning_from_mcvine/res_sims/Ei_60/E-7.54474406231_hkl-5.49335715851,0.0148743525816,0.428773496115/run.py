#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-7.54474406231_hkl-5.49335715851,0.0148743525816,0.428773496115/sample/sampleassembly.xml'
psi = -0.002994691799974961
hkl2Q = array([[-0.65787952,  0.93631774,  0.        ],
       [ 0.66207662,  0.46519107, -0.80916512],
       [-0.66207662, -0.46519107, -0.80916512]])
pp = array([ 1.08356296,  2.79747946,  0.18820057])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048535305374278227
Q = array([ 3.33993424, -5.33606993, -0.35898436])
E = -7.5447440623092703
hkl_projection = array([-0.96425718, -0.20268017,  0.80350952])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
