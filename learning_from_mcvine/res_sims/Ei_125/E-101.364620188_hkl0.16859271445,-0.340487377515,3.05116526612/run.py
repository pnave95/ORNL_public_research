#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-101.364620188_hkl0.16859271445,-0.340487377515,3.05116526612/sample/sampleassembly.xml'
psi = 0.007881027114224724
hkl2Q = array([[-0.66802354,  0.92910759,  0.        ],
       [ 0.65697828,  0.47236398, -0.80916512],
       [-0.65697828, -0.47236398, -0.80916512]])
pp = array([ 2.97000717,  0.42315177,  0.64210643])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032487154848104063
Q = array([-2.34086602, -1.44545376, -2.19338599])
E = -101.36462018807278
hkl_projection = array([-0.98030687,  0.19504856,  0.03892382])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
