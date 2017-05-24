#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E27.2393129733_hkl-2.58211735693,1.62221774393,-1.21962786664/sample/sampleassembly.xml'
psi = -0.01198004984203439
hkl2Q = array([[-0.64943993,  0.94219114,  0.        ],
       [ 0.66622975,  0.45922338, -0.80916512],
       [-0.66622975, -0.45922338, -0.80916512]])
pp = array([ 0.64642324,  2.92952846,  0.84618098])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.00981371223507959
Q = array([ 3.57025219, -1.12780617, -0.32576168])
E = 27.239312973322072
hkl_projection = array([ 0.04526074,  0.62050342, -0.72580267])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
