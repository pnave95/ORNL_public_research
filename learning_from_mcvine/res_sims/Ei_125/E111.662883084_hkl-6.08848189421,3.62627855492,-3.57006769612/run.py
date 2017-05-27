#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E111.662883084_hkl-6.08848189421,3.62627855492,-3.57006769612/sample/sampleassembly.xml'
psi = -0.017570401780956355
hkl2Q = array([[-0.64416263,  0.945807  ,  0.        ],
       [ 0.66878654,  0.45549176, -0.80916512],
       [-0.66878654, -0.45549176, -0.80916512]])
pp = array([-1.05346784,  2.80895096,  0.05150337])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0045822095548913502
Q = array([ 8.73479203, -2.48065236, -0.04548387])
E = 111.6628830837449
hkl_projection = array([-0.12108926,  0.10252468, -0.5300537 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
