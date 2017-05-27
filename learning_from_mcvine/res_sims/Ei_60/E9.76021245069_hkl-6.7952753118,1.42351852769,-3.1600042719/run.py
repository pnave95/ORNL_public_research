#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E9.76021245069_hkl-6.7952753118,1.42351852769,-3.1600042719/sample/sampleassembly.xml'
psi = -0.008435899520011555
hkl2Q = array([[-0.65277511,  0.93988352,  0.        ],
       [ 0.66459801,  0.46158171, -0.80916512],
       [-0.66459801, -0.46158171, -0.80916512]])
pp = array([-1.31105467,  2.69835795, -0.88770466])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050242889807445776
Q = array([ 7.48198671, -4.27109699,  1.40510369])
E = 9.7602124506911565
hkl_projection = array([-0.39091009, -0.92527716,  0.78519618])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
