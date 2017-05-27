#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E98.0717207355_hkl-16.2305215886,1.55408886076,-1.65663858494/sample/sampleassembly.xml'
psi = -0.004438427970902548
hkl2Q = array([[-0.65652704,  0.93726657,  0.        ],
       [ 0.66274754,  0.46423472, -0.80916512],
       [-0.66274754, -0.46423472, -0.80916512]])
pp = array([ 0.6047299 ,  2.93841824, -0.01776947])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017308768527009371
Q = array([ 12.78367805, -13.72179407,   0.08297966])
E = 98.071720735497252
hkl_projection = array([-0.54371927, -0.50084446,  0.97998396])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
