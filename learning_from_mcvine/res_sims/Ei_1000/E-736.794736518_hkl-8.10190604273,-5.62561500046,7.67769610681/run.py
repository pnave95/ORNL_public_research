#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-736.794736518_hkl-8.10190604273,-5.62561500046,7.67769610681/sample/sampleassembly.xml'
psi = 0.0013529907935563256
hkl2Q = array([[-0.6619441 ,  0.93344865,  0.        ],
       [ 0.66004787,  0.46806516, -0.80916512],
       [-0.66004787, -0.46806516, -0.80916512]])
pp = array([ 2.63900665,  1.42675993,  0.17180394])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011472879513619574
Q = array([ -3.41781319, -13.78952973,  -1.66047245])
E = -736.79473651833734
hkl_projection = array([ 0.70600266, -0.22223691, -0.32337385])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
