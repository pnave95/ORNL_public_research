#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E116.431672356_hkl-3.06220777499,3.11263944565,-2.58647258395/sample/sampleassembly.xml'
psi = -0.06963700201217037
hkl2Q = array([[-0.59406698,  0.97804949,  0.        ],
       [ 0.69158542,  0.42006879, -0.80916512],
       [-0.69158542, -0.42006879, -0.80916512]])
pp = array([ 2.87815997,  0.84628315,  0.59954577])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050203261426795959
Q = array([ 5.76057933, -0.60097166, -0.42575587])
E = 116.43167235559372
hkl_projection = array([ 0.30217583,  0.92236806,  0.90642883])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
