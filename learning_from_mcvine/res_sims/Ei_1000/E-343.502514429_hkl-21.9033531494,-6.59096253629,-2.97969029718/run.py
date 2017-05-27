#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-343.502514429_hkl-21.9033531494,-6.59096253629,-2.97969029718/sample/sampleassembly.xml'
psi = -0.0029589965167898
hkl2Q = array([[-0.65791294,  0.93629425,  0.        ],
       [ 0.66206002,  0.4652147 , -0.80916512],
       [-0.66206002, -0.4652147 , -0.80916512]])
pp = array([ 1.23966534,  2.73189126, -0.95350715])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011785095688330472
Q = array([ 12.01962059, -22.18800064,   7.74423841])
E = -343.50251442920114
hkl_projection = array([ 0.12679389, -0.53467042, -0.29893044])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
