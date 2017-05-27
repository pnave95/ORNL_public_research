#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-9.05282759787_hkl-0.36219801081,-0.948516055908,-0.16685924686/sample/sampleassembly.xml'
psi = 0.0018731004078398098
hkl2Q = array([[-0.66242951,  0.93310424,  0.        ],
       [ 0.65980433,  0.4684084 , -0.80916512],
       [-0.65980433, -0.4684084 , -0.80916512]])
pp = array([ 2.97723305,  0.3688948 , -0.47285114])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048529955486818332
Q = array([-0.2758099 , -0.70410311,  0.90252279])
E = -9.0528275978719961
hkl_projection = array([-0.7302485 ,  0.74075113, -0.37117678])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
