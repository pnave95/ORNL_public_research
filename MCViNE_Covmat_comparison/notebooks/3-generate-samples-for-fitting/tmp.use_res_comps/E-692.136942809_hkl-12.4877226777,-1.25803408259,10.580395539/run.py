#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-692.136942809_hkl-12.4877226777,-1.25803408259,10.580395539/sample/sampleassembly.xml'
psi = -0.00013539500147639275
hkl2Q = array([[-0.66055404,  0.93443284,  0.        ],
       [ 0.6607438 ,  0.46708224, -0.80916512],
       [-0.6607438 , -0.46708224, -0.80916512]])
pp = array([ 2.34950146,  1.8654337 ,  0.81818853])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.001155226472491835
Q = array([  0.42664671, -17.1984584 ,  -7.54332969])
E = -692.13694280867367
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
