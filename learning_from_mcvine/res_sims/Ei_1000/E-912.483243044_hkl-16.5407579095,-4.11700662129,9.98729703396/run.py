#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-912.483243044_hkl-16.5407579095,-4.11700662129,9.98729703396/sample/sampleassembly.xml'
psi = -0.0003963826383036241
hkl2Q = array([[-0.66031014,  0.9346052 ,  0.        ],
       [ 0.66086568,  0.46690978, -0.80916512],
       [-0.66086568, -0.46690978, -0.80916512]])
pp = array([ 2.04226872,  2.19753009,  0.47351202])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011412829491566465
Q = array([  1.60098   , -22.04451573,  -4.75003423])
E = -912.48324304424614
hkl_projection = array([ 0.57392468, -0.36840835, -0.87196195])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
