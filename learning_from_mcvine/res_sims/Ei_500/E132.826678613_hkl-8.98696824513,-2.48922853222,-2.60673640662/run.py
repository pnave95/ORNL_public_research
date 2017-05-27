#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E132.826678613_hkl-8.98696824513,-2.48922853222,-2.60673640662/sample/sampleassembly.xml'
psi = -0.0034077449118635533
hkl2Q = array([[-0.65749272,  0.9365894 ,  0.        ],
       [ 0.66226871,  0.46491756, -0.80916512],
       [-0.66226871, -0.46491756, -0.80916512]])
pp = array([ 2.26423334,  1.96805675, -0.97043566])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017645503903418968
Q = array([ 5.98668796, -8.36246769,  4.12347706])
E = 132.82667861300945
hkl_projection = array([-0.21375534,  0.77785443, -0.24776684])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
