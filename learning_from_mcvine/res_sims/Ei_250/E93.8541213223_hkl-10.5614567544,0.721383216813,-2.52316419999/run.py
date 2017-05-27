#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E93.8541213223_hkl-10.5614567544,0.721383216813,-2.52316419999/sample/sampleassembly.xml'
psi = -0.0038922085164725135
hkl2Q = array([[-0.6570389 ,  0.93690782,  0.        ],
       [ 0.66249387,  0.46459666, -0.80916512],
       [-0.66249387, -0.46459666, -0.80916512]])
pp = array([ 0.67425177,  2.92324897, -0.50811473])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025213959977478167
Q = array([ 9.08878067, -8.38770552,  1.45793832])
E = 93.854121322343246
hkl_projection = array([-0.63768863,  0.94203928, -0.39170989])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
