#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-39.838416356_hkl-8.46453614013,1.01514217998,-1.79476225931/sample/sampleassembly.xml'
psi = -0.005356096786217452
hkl2Q = array([[-0.65566666,  0.93786865,  0.        ],
       [ 0.66317328,  0.46362634, -0.80916512],
       [-0.66317328, -0.46362634, -0.80916512]])
pp = array([-0.86832273,  2.87158765, -0.27298821])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047081707532915899
Q = array([ 7.41336772, -6.63587732,  0.63084137])
E = -39.838416356024752
hkl_projection = array([-0.21290381,  0.7507973 ,  0.26415465])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
