#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E177.545944675_hkl-2.40616545277,-0.734341342208,-3.85395562583/sample/sampleassembly.xml'
psi = -0.0208435134789377
hkl2Q = array([[-0.64106345,  0.94791035,  0.        ],
       [ 0.67027383,  0.45330031, -0.80916512],
       [-0.67027383, -0.45330031, -0.80916512]])
pp = array([ 2.99217211,  0.21657812, -0.92774999])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017876470935150183
Q = array([ 3.63350055, -0.866707  ,  3.71268985])
E = 177.54594467515938
hkl_projection = array([-0.23014687,  0.88807009,  0.04871159])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
