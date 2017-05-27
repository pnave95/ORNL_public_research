#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E936.107645829_hkl-14.4954944032,7.84611117553,-9.89013114292/sample/sampleassembly.xml'
psi = -0.021086004864630577
hkl2Q = array([[-0.64083357,  0.94806577,  0.        ],
       [ 0.67038374,  0.45313776, -0.80916512],
       [-0.67038374, -0.45313776, -0.80916512]])
pp = array([ 0.47183923,  2.96266227, -0.85880371])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0018076482408971107
Q = array([ 21.17928782,  -5.70572089,   1.65394965])
E = 936.10764582940328
hkl_projection = array([ 0.29326554,  0.01070717,  0.69660488])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
