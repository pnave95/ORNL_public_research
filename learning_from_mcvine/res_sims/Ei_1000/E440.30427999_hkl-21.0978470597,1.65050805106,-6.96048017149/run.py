#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E440.30427999_hkl-21.0978470597,1.65050805106,-6.96048017149/sample/sampleassembly.xml'
psi = -0.0067622064006074645
hkl2Q = array([[-0.65434727,  0.93878966,  0.        ],
       [ 0.66382453,  0.46269339, -0.80916512],
       [-0.66382453, -0.46269339, -0.80916512]])
pp = array([ 0.48034603,  2.96129494, -0.80416353])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012802152559324791
Q = array([ 19.52150388, -15.82219326,   4.29664421])
E = 440.30427999006179
hkl_projection = array([ 0.95863705,  0.37959193, -0.89771324])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
