#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E21.2421735368_hkl-4.40047647126,0.557168630456,1.2492411195/sample/sampleassembly.xml'
psi = -0.002656501417201436
hkl2Q = array([[-0.65819614,  0.9360952 ,  0.        ],
       [ 0.66191926,  0.46541495, -0.80916512],
       [-0.66191926, -0.46541495, -0.80916512]])
pp = array([ 2.31109864,  1.91280503,  0.62951718])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034677879372285321
Q = array([ 2.43828051, -4.44136577, -1.46168376])
E = 21.242173536847019
hkl_projection = array([ 0.85243628, -0.9981551 , -0.12145745])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
