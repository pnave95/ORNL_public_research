#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-873.324954449_hkl-8.7841700633,-9.33493955657,5.29281168806/sample/sampleassembly.xml'
psi = 0.0013930688149424097
hkl2Q = array([[-0.66198151,  0.93342212,  0.        ],
       [ 0.66002911,  0.46809162, -0.80916512],
       [-0.66002911, -0.46809162, -0.80916512]])
pp = array([ 2.59473054,  1.50578001, -0.32732126])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011419012613118041
Q = array([ -3.8397834 , -15.04646635,   3.27074887])
E = -873.32495444861252
hkl_projection = array([-0.00849953, -0.46481543, -0.19479667])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
