#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E753.318382581_hkl-20.4837134522,9.82702912423,-10.0989203431/sample/sampleassembly.xml'
psi = -0.014459493385009854
hkl2Q = array([[-0.64710182,  0.9437985 ,  0.        ],
       [ 0.66736632,  0.45757009, -0.80916512],
       [-0.66736632, -0.45757009, -0.80916512]])
pp = array([-1.20153275,  2.74887596, -0.05920385])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0014103594206526524
Q = array([ 26.55295584, -10.21497949,   0.22000489])
E = 753.31838258121138
hkl_projection = array([ 0.89929375, -0.46712761,  0.64928462])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
