#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-87.368794902_hkl-4.21333167365,-2.90651425046,1.70241265798/sample/sampleassembly.xml'
psi = 0.00020652096429408048
hkl2Q = array([[-0.6608735 ,  0.93420693,  0.        ],
       [ 0.66058406,  0.46730813, -0.80916512],
       [-0.66058406, -0.46730813, -0.80916512]])
pp = array([ 2.39407388,  1.80787452, -0.28923943])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032552545206094353
Q = array([-0.26010439, -6.08991268,  0.97431701])
E = -87.368794902008943
hkl_projection = array([-0.22476191, -0.44796964, -0.54898719])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
