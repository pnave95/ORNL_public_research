#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-21.1372167529_hkl-5.29118216953,0.0709740361943,0.0955461948387/sample/sampleassembly.xml'
psi = -0.0025949034821079794
hkl2Q = array([[-0.6582538 ,  0.93605465,  0.        ],
       [ 0.66189059,  0.46545572, -0.80916512],
       [-0.66189059, -0.46545572, -0.80916512]])
pp = array([ 0.21244796,  2.99246819,  0.08122282])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066455483891351098
Q = array([ 3.46667668, -4.96427293, -0.13474236])
E = -21.137216752934627
hkl_projection = array([ 0.81394989,  0.21162175, -0.39567168])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
