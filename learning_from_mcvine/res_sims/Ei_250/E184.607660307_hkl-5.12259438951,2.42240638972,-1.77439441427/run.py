#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E184.607660307_hkl-5.12259438951,2.42240638972,-1.77439441427/sample/sampleassembly.xml'
psi = -0.007717785078535317
hkl2Q = array([[-0.65344988,  0.93941451,  0.        ],
       [ 0.66426637,  0.46205884, -0.80916512],
       [-0.66426637, -0.46205884, -0.80916512]])
pp = array([ 2.58635269,  1.52012492,  0.27742984])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0028082003020189475
Q = array([ 6.13515235, -2.87307056, -0.52434869])
E = 184.60766030675467
hkl_projection = array([ 0.92870637,  0.6742347 , -0.14176286])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
