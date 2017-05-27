#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E-148.027567402_hkl-20.6217456984,3.26217103625,-0.458421674674/sample/sampleassembly.xml'
psi = -0.004332555358570254
hkl2Q = array([[-0.65662627,  0.93719705,  0.        ],
       [ 0.66269839,  0.46430489, -0.80916512],
       [-0.66269839, -0.46430489, -0.80916512]])
pp = array([-0.06795825,  2.99923018,  0.38662902])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0016614329677824896
Q = array([ 16.00641073, -17.59914991,  -2.26869618])
E = -148.02756740172072
hkl_projection = array([ 0.10929823, -0.83652932, -0.51163858])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
