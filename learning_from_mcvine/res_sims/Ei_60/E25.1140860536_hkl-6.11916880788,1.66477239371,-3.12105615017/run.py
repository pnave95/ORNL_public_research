#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E25.1140860536_hkl-6.11916880788,1.66477239371,-3.12105615017/sample/sampleassembly.xml'
psi = -0.009746396779289006
hkl2Q = array([[-0.65154283,  0.94073817,  0.        ],
       [ 0.66520234,  0.46071036, -0.80916512],
       [-0.66520234, -0.46071036, -0.80916512]])
pp = array([-1.33427265,  2.68695301, -0.89148177])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.005222445797189377
Q = array([ 7.17044493, -3.5516549 ,  1.17837402])
E = 25.114086053645224
hkl_projection = array([ 0.86071214, -0.95315812,  0.14902131])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
