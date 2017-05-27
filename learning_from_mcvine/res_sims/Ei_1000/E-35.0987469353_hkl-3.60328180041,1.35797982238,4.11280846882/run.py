#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-35.0987469353_hkl-3.60328180041,1.35797982238,4.11280846882/sample/sampleassembly.xml'
psi = -0.0006538300764420846
hkl2Q = array([[-0.66006951,  0.93477517,  0.        ],
       [ 0.66098586,  0.46673963, -0.80916512],
       [-0.66098586, -0.46673963, -0.80916512]])
pp = array([ 2.93227604,  0.63384323,  0.60289022])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011992635391071533
Q = array([ 0.55751366, -4.65404604, -4.42677104])
E = -35.098746935263193
hkl_projection = array([ 0.01160109, -0.81972475, -0.9185569 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
