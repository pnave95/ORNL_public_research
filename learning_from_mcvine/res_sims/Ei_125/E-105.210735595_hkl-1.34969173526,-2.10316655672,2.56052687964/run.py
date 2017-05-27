#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-105.210735595_hkl-1.34969173526,-2.10316655672,2.56052687964/sample/sampleassembly.xml'
psi = 0.003059969147766307
hkl2Q = array([[-0.66353652,  0.93231736,  0.        ],
       [ 0.65924793,  0.46919117, -0.80916512],
       [-0.65924793, -0.46919117, -0.80916512]])
pp = array([ 2.83577301,  0.97897469,  0.10512069])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032349006589914267
Q = array([-2.17896049, -3.44650482, -0.37008002])
E = -105.21073559477058
hkl_projection = array([-0.13866929, -0.65685154, -0.69707262])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
