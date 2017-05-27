#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-42.396200602_hkl-0.0774070659396,-1.51600819258,0.873915593095/sample/sampleassembly.xml'
psi = 0.006090040160848924
hkl2Q = array([[-0.66635845,  0.93030252,  0.        ],
       [ 0.65782322,  0.47118658, -0.80916512],
       [-0.65782322, -0.47118658, -0.80916512]])
pp = array([ 2.95611262,  0.51127114, -0.22171173])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046986316471698299
Q = array([-1.52056651, -1.19811201,  0.51955893])
E = -42.396200602040025
hkl_projection = array([-0.65132713, -0.93705425,  0.75449097])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
