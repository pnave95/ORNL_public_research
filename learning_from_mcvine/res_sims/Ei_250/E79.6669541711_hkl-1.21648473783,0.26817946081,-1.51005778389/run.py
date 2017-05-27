#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E79.6669541711_hkl-1.21648473783,0.26817946081,-1.51005778389/sample/sampleassembly.xml'
psi = -0.021596331156661423
hkl2Q = array([[-0.64034966,  0.94839268,  0.        ],
       [ 0.6706149 ,  0.45279559, -0.80916512],
       [-0.6706149 , -0.45279559, -0.80916512]])
pp = array([ 2.99777874,  0.11542374, -0.33279332])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024938552282371337
Q = array([ 1.97148798, -0.34852724,  1.00488462])
E = 79.6669541710923
hkl_projection = array([ 0.25363591,  0.60214363,  0.77156062])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
