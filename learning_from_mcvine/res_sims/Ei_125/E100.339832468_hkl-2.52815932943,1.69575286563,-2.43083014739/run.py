#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E100.339832468_hkl-2.52815932943,1.69575286563,-2.43083014739/sample/sampleassembly.xml'
psi = -0.04044352179127836
hkl2Q = array([[-0.62236246,  0.96029232,  0.        ],
       [ 0.67902921,  0.44007671, -0.80916512],
       [-0.67902921, -0.44007671, -0.80916512]])
pp = array([ 2.95336513,  0.52691023, -0.51230251])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0041517290746235233
Q = array([ 4.37550187, -0.6117589 ,  0.59479889])
E = 100.3398324682517
hkl_projection = array([ 0.35839202,  0.2683991 , -0.31782585])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
