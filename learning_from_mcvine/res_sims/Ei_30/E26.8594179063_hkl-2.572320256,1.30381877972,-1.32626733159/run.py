#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E26.8594179063_hkl-2.572320256,1.30381877972,-1.32626733159/sample/sampleassembly.xml'
psi = -0.010656341886439945
hkl2Q = array([[-0.65068654,  0.94133065,  0.        ],
       [ 0.66562129,  0.46010487, -0.80916512],
       [-0.66562129, -0.46010487, -0.80916512]])
pp = array([ 0.92944567,  2.85239036, -0.04277469])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0094282328905468671
Q = array([ 3.42441548, -1.21128847,  0.01816459])
E = 26.85941790634439
hkl_projection = array([-0.68407201, -0.85796874, -0.74650114])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
