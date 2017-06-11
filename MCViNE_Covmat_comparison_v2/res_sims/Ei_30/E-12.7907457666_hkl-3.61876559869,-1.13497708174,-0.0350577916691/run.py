#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison_v2/res_sims/Ei_30/E-12.7907457666_hkl-3.61876559869,-1.13497708174,-0.0350577916691/sample/sampleassembly.xml'
psi = -0.0015797816277634672
hkl2Q = array([[ -6.59203669e-01,   9.35385960e-01,  -7.77130021e-17],
       [  6.61417756e-01,   4.66127384e-01,  -8.09165116e-01],
       [ -6.61417756e-01,  -4.66127384e-01,  -8.09165116e-01]])
pp = array([ 1.45474505,  2.62368383, -0.63730184])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067572742050404488
Q = array([ 1.65799741, -3.89764504,  0.9467514 ])
E = -12.790745766648209
hkl_projection = array([-0.96015643, -0.07077327,  0.11955734])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
