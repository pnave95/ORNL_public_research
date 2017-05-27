#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-15.0712940708_hkl-3.95235579473,0.0684848015073,1.08888023538/sample/sampleassembly.xml'
psi = -0.0017176973430312187
hkl2Q = array([[-0.65907466,  0.93547687,  0.        ],
       [ 0.66148204,  0.46603616, -0.80916512],
       [-0.66148204, -0.46603616, -0.80916512]])
pp = array([ 1.23729532,  2.73296548,  0.61334652])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067283511040316032
Q = array([ 1.92992429, -4.17287858, -0.93649941])
E = -15.071294070833451
hkl_projection = array([ 0.33034548,  0.99734862,  0.08845009])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
