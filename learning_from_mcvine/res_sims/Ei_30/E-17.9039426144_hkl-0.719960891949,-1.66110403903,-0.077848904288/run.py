#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-17.9039426144_hkl-0.719960891949,-1.66110403903,-0.077848904288/sample/sampleassembly.xml'
psi = 0.0014932740971750865
hkl2Q = array([[-0.66207504,  0.93335578,  0.        ],
       [ 0.6599822 ,  0.46815775, -0.80916512],
       [-0.6599822 , -0.46815775, -0.80916512]])
pp = array([ 2.85552222,  0.91977871, -0.91581323])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067218650370538839
Q = array([-0.56825207, -1.41319283,  1.40710006])
E = -17.903942614406411
hkl_projection = array([ 0.01894735,  0.07264656, -0.77105478])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
