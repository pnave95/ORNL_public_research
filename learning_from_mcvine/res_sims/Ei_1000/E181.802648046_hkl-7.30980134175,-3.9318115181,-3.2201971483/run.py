#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E181.802648046_hkl-7.30980134175,-3.9318115181,-3.2201971483/sample/sampleassembly.xml'
psi = -0.0033005545287026396
hkl2Q = array([[-0.65759311,  0.93651891,  0.        ],
       [ 0.66221888,  0.46498854, -0.80916512],
       [-0.66221888, -0.46498854, -0.80916512]])
pp = array([ 2.78132076,  1.12439086, -0.90669273])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012317932511200017
Q = array([ 4.33563051, -7.17665975,  5.78715593])
E = 181.80264804584363
hkl_projection = array([ 0.85652615, -0.26857459,  0.46317691])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
