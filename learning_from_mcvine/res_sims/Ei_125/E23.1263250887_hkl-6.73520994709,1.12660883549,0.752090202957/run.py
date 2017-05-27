#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E23.1263250887_hkl-6.73520994709,1.12660883549,0.752090202957/sample/sampleassembly.xml'
psi = -0.0036893484665506144
hkl2Q = array([[-0.65722894,  0.93677451,  0.        ],
       [ 0.66239961,  0.46473104, -0.80916512],
       [-0.66239961, -0.46473104, -0.80916512]])
pp = array([ 1.36324742,  2.67236908,  0.66214545])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034755570685769247
Q = array([ 4.67465592, -6.13532258, -1.52017773])
E = 23.126325088666334
hkl_projection = array([ 0.8923445 ,  0.1386769 , -0.94554028])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
