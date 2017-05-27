#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-807.105117896_hkl-23.8773574287,-6.55861837289,2.73874264704/sample/sampleassembly.xml'
psi = -0.001961130533177951
hkl2Q = array([[ -6.58846912e-01,   9.35637279e-01,  -7.76921279e-17],
       [  6.61595465e-01,   4.65875119e-01,  -8.09165116e-01],
       [ -6.61595465e-01,  -4.65875119e-01,  -8.09165116e-01]])
pp = array([ 1.27372588,  2.7161779 , -0.3147674 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011446984178908129
Q = array([  9.58043133, -26.67195491,   3.09091019])
E = -807.1051178958628
hkl_projection = array([-0.13076571, -0.49283985,  0.30719024])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
