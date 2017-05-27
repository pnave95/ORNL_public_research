#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-845.728014629_hkl-27.7921686124,-2.82777747485,3.32181752026/sample/sampleassembly.xml'
psi = -0.0026894914627035695
hkl2Q = array([[-0.65816526,  0.93611691,  0.        ],
       [ 0.66193461,  0.46539312, -0.80916512],
       [-0.66193461, -0.46539312, -0.80916512]])
pp = array([ 0.7884914 ,  2.89452609,  0.04006814])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011421477040157286
Q = array([ 14.22120998, -28.87869815,  -0.39975997])
E = -845.72801462924554
hkl_projection = array([-0.57544266, -0.7215788 ,  0.32561341])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
