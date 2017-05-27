#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-19.1211691449_hkl0.359735325736,-0.20887756677,0.625311848337/sample/sampleassembly.xml'
psi = 0.05094502202893175
hkl2Q = array([[ -7.07402930e-01,   8.99487335e-01,   8.08145354e-17],
       [  6.36033594e-01,   5.00209409e-01,  -8.09165116e-01],
       [ -6.36033594e-01,  -5.00209409e-01,  -8.09165116e-01]])
pp = array([ 2.99965661,  0.04538945,  0.1632435 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047903105135179442
Q = array([-0.78505032, -0.09369202, -0.33696409])
E = -19.121169144913132
hkl_projection = array([ 0.90503828, -0.47119242, -0.82693587])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
