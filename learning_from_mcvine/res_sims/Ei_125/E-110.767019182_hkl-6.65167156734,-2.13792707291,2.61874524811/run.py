#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-110.767019182_hkl-6.65167156734,-2.13792707291,2.61874524811/sample/sampleassembly.xml'
psi = -0.0007140254125562711
hkl2Q = array([[-0.66001324,  0.9348149 ,  0.        ],
       [ 0.66101396,  0.46669984, -0.80916512],
       [-0.66101396, -0.46669984, -0.80916512]])
pp = array([ 1.84104871,  2.36865777,  0.10921437])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032296021866058239
Q = array([ 1.2459645 , -8.43801988, -0.38906129])
E = -110.76701918171409
hkl_projection = array([ 0.24817987,  0.56006997,  0.01621765])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
