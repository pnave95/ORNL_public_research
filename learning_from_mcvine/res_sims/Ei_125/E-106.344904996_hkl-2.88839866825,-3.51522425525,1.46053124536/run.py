#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-106.344904996_hkl-2.88839866825,-3.51522425525,1.46053124536/sample/sampleassembly.xml'
psi = 0.0013208461022916733
hkl2Q = array([[-0.6619141 ,  0.93346992,  0.        ],
       [ 0.66006291,  0.46804395, -0.80916512],
       [-0.66006291, -0.46804395, -0.80916512]])
pp = array([ 2.63132911,  1.44087026, -0.47672045])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032391663637242386
Q = array([-1.37243987, -5.02510553,  1.66258591])
E = -106.34490499604225
hkl_projection = array([-0.7282838 , -0.80433982,  0.98558659])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
