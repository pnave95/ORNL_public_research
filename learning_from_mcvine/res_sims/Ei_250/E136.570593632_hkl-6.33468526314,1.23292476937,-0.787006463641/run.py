#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E136.570593632_hkl-6.33468526314,1.23292476937,-0.787006463641/sample/sampleassembly.xml'
psi = -0.003953905102562753
hkl2Q = array([[-0.65698109,  0.93694835,  0.        ],
       [ 0.66252253,  0.46455578, -0.80916512],
       [-0.66252253, -0.46455578, -0.80916512]])
pp = array([ 2.22469931,  2.01263832,  0.14533069])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002607576746051281
Q = array([ 5.5000184 , -4.99690219, -0.36082154])
E = 136.57059363177586
hkl_projection = array([ 0.08917662,  0.95679887,  0.9568116 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
