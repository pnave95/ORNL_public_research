#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-9.14078169329_hkl-0.692867422337,-1.27825471867,-0.38105057535/sample/sampleassembly.xml'
psi = 0.0006021538534544903
hkl2Q = array([[-0.66124305,  0.93394539,  0.        ],
       [ 0.66039912,  0.46756944, -0.80916512],
       [-0.66039912, -0.46756944, -0.80916512]])
pp = array([ 2.94592058,  0.56705552, -0.71381419])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048652623373988593
Q = array([-0.13435906, -1.06660558,  1.34265196])
E = -9.1407816932906201
hkl_projection = array([ 0.40035852,  0.41433236, -0.60841548])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
