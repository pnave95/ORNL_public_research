#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-308.894886437_hkl-18.6115153334,-3.10031977934,3.90051633534/sample/sampleassembly.xml'
psi = -0.002014711842553381
hkl2Q = array([[-0.65879678,  0.93567258,  0.        ],
       [ 0.66162043,  0.46583967, -0.80916512],
       [-0.66162043, -0.46583967, -0.80916512]])
pp = array([ 1.71925326,  2.45848901,  0.07699189])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011718123887287275
Q = array([  7.62931018, -20.67555174,  -0.64749114])
E = -308.89488643695756
hkl_projection = array([-0.30014346, -0.69625149, -0.79836959])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
