#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-19.9031641574_hkl-12.0568541218,-0.820085040379,-1.47366031617/sample/sampleassembly.xml'
psi = -0.002733710727911097
hkl2Q = array([[-0.65812386,  0.93614601,  0.        ],
       [ 0.66195519,  0.46536384, -0.80916512],
       [-0.66195519, -0.46536384, -0.80916512]])
pp = array([ 0.70513827,  2.91595268, -0.49277508])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002389547345208571
Q = array([  8.36754093, -10.9828256 ,   1.85601873])
E = -19.903164157364188
hkl_projection = array([-0.12413167, -0.08192767, -0.52616797])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
