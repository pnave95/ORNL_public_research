#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-15.7825490975_hkl-0.395869951479,-0.0502135059027,1.34672168337/sample/sampleassembly.xml'
psi = 0.002390676730678419
hkl2Q = array([[-0.66291237,  0.93276125,  0.        ],
       [ 0.65956181,  0.46874983, -0.80916512],
       [-0.65956181, -0.46874983, -0.80916512]])
pp = array([ 2.92450299,  0.66879164,  0.68513413])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067253967870093629
Q = array([-0.65893801, -1.02406529, -1.04908919])
E = -15.782549097543983
hkl_projection = array([-0.57622765,  0.70235825,  0.48643169])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
