#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E334.320428386_hkl-13.3427291074,-1.66027736485,-2.26212971505/sample/sampleassembly.xml'
psi = -0.004097707796187072
hkl2Q = array([[-0.65684635,  0.93704282,  0.        ],
       [ 0.66258933,  0.46446051, -0.80916512],
       [-0.66258933, -0.46446051, -0.80916512]])
pp = array([ 2.17967992,  2.06130916, -0.53524058])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012507985951546209
Q = array([  9.16290384, -12.22317186,   3.17387498])
E = 334.32042838583766
hkl_projection = array([ 0.76105485,  0.13333376, -0.48511145])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
