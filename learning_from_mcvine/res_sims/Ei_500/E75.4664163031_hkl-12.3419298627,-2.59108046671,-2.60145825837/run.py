#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E75.4664163031_hkl-12.3419298627,-2.59108046671,-2.60145825837/sample/sampleassembly.xml'
psi = -0.003346135054033472
hkl2Q = array([[-0.65755042,  0.93654889,  0.        ],
       [ 0.66224007,  0.46495836, -0.80916512],
       [-0.66224007, -0.46495836, -0.80916512]])
pp = array([ 1.6311684 ,  2.5177946 , -0.91559835])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017368694474981733
Q = array([  8.12231374, -11.55399544,   4.2016212 ])
E = 75.466416303075107
hkl_projection = array([-0.98648671, -0.1718113 , -0.97888897])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
