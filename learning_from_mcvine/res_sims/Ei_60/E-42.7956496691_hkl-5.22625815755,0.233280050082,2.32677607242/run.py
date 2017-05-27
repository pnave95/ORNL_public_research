#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-42.7956496691_hkl-5.22625815755,0.233280050082,2.32677607242/sample/sampleassembly.xml'
psi = -0.0016794420826380058
hkl2Q = array([[-0.65911044,  0.93545165,  0.        ],
       [ 0.66146421,  0.46606146, -0.80916512],
       [-0.66146421, -0.46606146, -0.80916512]])
pp = array([ 1.48696607,  2.60555789,  0.92033991])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047265123406583535
Q = array([ 2.05990865, -5.86460965, -2.07150811])
E = -42.795649669053709
hkl_projection = array([-0.03965628, -0.22665404,  0.31057468])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
