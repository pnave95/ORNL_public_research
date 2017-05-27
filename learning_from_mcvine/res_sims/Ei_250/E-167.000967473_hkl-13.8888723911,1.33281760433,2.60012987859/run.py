#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-167.000967473_hkl-13.8888723911,1.33281760433,2.60012987859/sample/sampleassembly.xml'
psi = -0.0021934381969626565
hkl2Q = array([[-0.65862954,  0.93579031,  0.        ],
       [ 0.66170367,  0.46572141, -0.80916512],
       [-0.66170367, -0.46572141, -0.80916512]])
pp = array([ 0.58770796,  2.94187004,  0.68904256])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023117470545611098
Q = array([  8.30903643, -13.58728665,  -3.18240391])
E = -167.00096747285014
hkl_projection = array([-0.85496848, -0.94704642, -0.56456943])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
