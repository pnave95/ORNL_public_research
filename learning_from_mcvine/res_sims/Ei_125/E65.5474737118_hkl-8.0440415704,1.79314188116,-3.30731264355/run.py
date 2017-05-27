#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E65.5474737118_hkl-8.0440415704,1.79314188116,-3.30731264355/sample/sampleassembly.xml'
psi = -0.008085929465193174
hkl2Q = array([[-0.653104  ,  0.93965501,  0.        ],
       [ 0.66443643,  0.46181427, -0.80916512],
       [-0.66443643, -0.46181427, -0.80916512]])
pp = array([-0.47706194,  2.96182577, -0.69743579])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0036878507510323356
Q = array([ 8.64252352, -5.20316129,  1.22521416])
E = 65.547473711833533
hkl_projection = array([ 0.41597759, -0.80966479, -0.84194639])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
