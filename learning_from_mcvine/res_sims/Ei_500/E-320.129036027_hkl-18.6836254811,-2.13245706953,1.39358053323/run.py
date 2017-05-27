#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-320.129036027_hkl-18.6836254811,-2.13245706953,1.39358053323/sample/sampleassembly.xml'
psi = -0.002478766224535257
hkl2Q = array([[-0.6583625 ,  0.9359782 ,  0.        ],
       [ 0.66183653,  0.46553259, -0.80916512],
       [-0.66183653, -0.46553259, -0.80916512]])
pp = array([ 0.8485117 ,  2.87750376, -0.08993604])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016296799327205035
Q = array([  9.96693798, -19.1289515 ,   0.59787312])
E = -320.12903602719314
hkl_projection = array([ 0.21155101, -0.26507354, -0.75191268])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
