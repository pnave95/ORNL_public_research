#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E13.0724269115_hkl-2.27953741074,0.352543434449,-0.00847633441195/sample/sampleassembly.xml'
psi = -0.003285406415996954
hkl2Q = array([[ -6.57607293e-01,   9.36508953e-01,   7.76198144e-17],
       [  6.62211831e-01,   4.64998576e-01,  -8.09165116e-01],
       [ -6.62211831e-01,  -4.64998576e-01,  -8.09165116e-01]])
pp = array([ 2.18023118,  2.06072609,  0.29168285])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073521372340241298
Q = array([ 1.73811199, -1.96693352, -0.2784071 ])
E = 13.072426911541008
hkl_projection = array([ 0.01890195,  0.56932004, -0.72255902])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
