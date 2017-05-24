#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-361.794455188_hkl-20.102272655,-6.81086336863,-1.06742327042/sample/sampleassembly.xml'
psi = -0.002397712847287472
hkl2Q = array([[-0.65843837,  0.93592483,  0.        ],
       [ 0.66179879,  0.46558623, -0.80916512],
       [-0.66179879, -0.46558623, -0.80916512]])
pp = array([ 1.52219708,  2.58513366, -0.76692028])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011740300927334643
Q = array([  9.43510584, -21.48828278,   6.37483473])
E = -361.79445518833825
hkl_projection = array([ 0.62387482, -0.14084256,  0.12081751])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
