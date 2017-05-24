#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E6.79354947752_hkl-0.425327603929,-0.22727780655,-0.612236685591/sample/sampleassembly.xml'
psi = -0.009001878525486397
hkl2Q = array([[-0.65224305,  0.94025282,  0.        ],
       [ 0.66485915,  0.46120548, -0.80916512],
       [-0.66485915, -0.46120548, -0.80916512]])
pp = array([ 2.99315321,  0.20256814, -0.61881331])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0071349669208207959
Q = array([ 0.53336041, -0.22237034,  0.67930584])
E = 6.7935494775180985
hkl_projection = array([ 0.56167858,  0.25629721, -0.34635688])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
