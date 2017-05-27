#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E12.2329070169_hkl-1.56384609069,-0.225045384412,-0.570247069728/sample/sampleassembly.xml'
psi = -0.003582653984321345
hkl2Q = array([[-0.65732889,  0.93670438,  0.        ],
       [ 0.66235002,  0.46480171, -0.80916512],
       [-0.66235002, -0.46480171, -0.80916512]])
pp = array([ 2.67354725,  1.36093538, -0.67140878])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0073452258877858157
Q = array([ 1.25660556, -1.30441115,  0.64352291])
E = 12.232907016867941
hkl_projection = array([ 0.42414034, -0.90641502, -0.08378185])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
