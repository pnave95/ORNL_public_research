#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-95.3372524983_hkl-4.34218919006,-3.25503293633,1.51840853051/sample/sampleassembly.xml'
psi = 0.00021807217904272342
hkl2Q = array([[-0.66088429,  0.9341993 ,  0.        ],
       [ 0.66057866,  0.46731576, -0.80916512],
       [-0.66057866, -0.46731576, -0.80916512]])
pp = array([ 2.36855196,  1.84118485, -0.4115143 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032488760181841859
Q = array([-0.28354894, -6.28717453,  1.40521589])
E = -95.337252498278687
hkl_projection = array([-0.78090632, -0.15327099,  0.84541898])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
