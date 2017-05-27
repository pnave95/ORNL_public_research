#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-111.276626796_hkl-0.646376114907,0.0475637157633,3.34596741064/sample/sampleassembly.xml'
psi = 0.002914183070175637
hkl2Q = array([[-0.66340059,  0.93241409,  0.        ],
       [ 0.65931632,  0.46909506, -0.80916512],
       [-0.65931632, -0.46909506, -0.80916512]])
pp = array([ 2.95836103,  0.49809637,  0.6361697 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023358269008955171
Q = array([-1.7458851 , -2.14995506, -2.74592701])
E = -111.2766267960792
hkl_projection = array([-0.77077493, -0.63356976,  0.41317041])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
