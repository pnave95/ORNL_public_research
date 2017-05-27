#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-43.7040742017_hkl-10.4079870101,0.683460083527,-0.820966777154/sample/sampleassembly.xml'
psi = -0.004190218355101834
hkl2Q = array([[-0.65675966,  0.93710358,  0.        ],
       [ 0.6626323 ,  0.46439921, -0.80916512],
       [-0.6626323 , -0.46439921, -0.80916512]])
pp = array([-0.00926983,  2.99998568, -0.03686428])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003309976281469694
Q = array([ 7.83242783, -9.05470725,  0.11126562])
E = -43.704074201719322
hkl_projection = array([-0.76710753, -0.86904786,  0.99890101])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
