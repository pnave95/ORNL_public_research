#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E486.072236998_hkl-10.8863987597,-1.22125479547,-4.92292121474/sample/sampleassembly.xml'
psi = -0.006175342622659744
hkl2Q = array([[-0.6548981 ,  0.93840548,  0.        ],
       [ 0.66355288,  0.46308289, -0.80916512],
       [-0.66355288, -0.46308289, -0.80916512]])
pp = array([ 2.48076639,  1.68694935, -0.98650251])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012981063484744531
Q = array([ 9.58573327, -8.50167791,  4.9716529 ])
E = 486.07223699788892
hkl_projection = array([-0.79142743, -0.13143987, -0.02639706])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
