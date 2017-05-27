#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E14.869705082_hkl-11.1698535814,1.29033666591,0.533091025915/sample/sampleassembly.xml'
psi = -0.0027882925486070057
hkl2Q = array([[-0.65807276,  0.93618193,  0.        ],
       [ 0.66198059,  0.46532771, -0.80916512],
       [-0.66198059, -0.46532771, -0.80916512]])
pp = array([ 0.89840026,  2.86232021,  0.41794847])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024177651599289842
Q = array([  7.85185833, -10.10464772,  -1.47545408])
E = 14.869705081976008
hkl_projection = array([-0.14027772, -0.92519052,  0.83544979])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
