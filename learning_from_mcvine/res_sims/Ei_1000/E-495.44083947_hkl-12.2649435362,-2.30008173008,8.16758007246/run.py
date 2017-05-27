#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-495.44083947_hkl-12.2649435362,-2.30008173008,8.16758007246/sample/sampleassembly.xml'
psi = -0.0003942270896921733
hkl2Q = array([[-0.66031216,  0.93460378,  0.        ],
       [ 0.66086467,  0.4669112 , -0.80916512],
       [-0.66086467, -0.4669112 , -0.80916512]])
pp = array([ 2.36315537,  1.84810625,  0.53664923])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011624793384180862
Q = array([  1.18098343, -16.35033117,  -4.74777498])
E = -495.44083947020789
hkl_projection = array([ 0.95041429,  0.89247323, -0.47894138])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
