#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-35.702936923_hkl-9.66372502054,1.00485368485,0.291912425964/sample/sampleassembly.xml'
psi = -0.0037879570844140628
hkl2Q = array([[-0.65713657,  0.93683932,  0.        ],
       [ 0.66244543,  0.46466572, -0.80916512],
       [-0.66244543, -0.46466572, -0.80916512]])
pp = array([ 0.3355678 ,  2.9811733 ,  0.35864605])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033266186763950059
Q = array([ 6.82267176, -8.72207817, -1.0492979 ])
E = -35.702936922973592
hkl_projection = array([ 0.62519287,  0.68120544, -0.34328189])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
