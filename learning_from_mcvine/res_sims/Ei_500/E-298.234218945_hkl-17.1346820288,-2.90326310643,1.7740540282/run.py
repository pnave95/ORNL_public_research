#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-298.234218945_hkl-17.1346820288,-2.90326310643,1.7740540282/sample/sampleassembly.xml'
psi = -0.0021393660489052147
hkl2Q = array([[-0.65868014,  0.93575469,  0.        ],
       [ 0.66167849,  0.46575719, -0.80916512],
       [-0.66167849, -0.46575719, -0.80916512]])
pp = array([ 1.13141923,  2.7784691 , -0.13939623])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016330676088393047
Q = array([  8.19139459, -18.21235323,   0.9137166 ])
E = -298.23421894548119
hkl_projection = array([ 0.4611986 , -0.20147192,  0.42319003])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
