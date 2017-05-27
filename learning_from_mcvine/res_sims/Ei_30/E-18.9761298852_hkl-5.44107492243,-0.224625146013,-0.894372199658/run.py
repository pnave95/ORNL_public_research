#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-18.9761298852_hkl-5.44107492243,-0.224625146013,-0.894372199658/sample/sampleassembly.xml'
psi = -0.003125887913206709
hkl2Q = array([[-0.65775668,  0.93640404,  0.        ],
       [ 0.66213765,  0.46510421, -0.80916512],
       [-0.66213765, -0.46510421, -0.80916512]])
pp = array([-0.12735758,  2.99729546, -0.56734357])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066833234565256026
Q = array([ 4.02236809, -4.78354237,  0.90545362])
E = -18.97612988524989
hkl_projection = array([-0.38229434, -0.064384  , -0.18013342])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
