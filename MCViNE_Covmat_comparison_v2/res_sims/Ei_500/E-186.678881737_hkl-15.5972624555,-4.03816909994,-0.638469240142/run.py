#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_500/E-186.678881737_hkl-15.5972624555,-4.03816909994,-0.638469240142/sample/sampleassembly.xml'
psi = -0.0023580539298552927
hkl2Q = array([[-0.65847548,  0.93589872,  0.        ],
       [ 0.66178033,  0.46561248, -0.80916512],
       [-0.66178033, -0.46561248, -0.80916512]])
pp = array([ 1.2736479 ,  2.71621447, -0.63525154])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016573854892904345
Q = array([  8.02056045, -16.1804006 ,   3.78417261])
E = -186.67888173670366
hkl_projection = array([ 0.93536882,  0.7358091 ,  0.95093581])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
