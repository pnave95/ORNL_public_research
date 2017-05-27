#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E49.6200529711_hkl-2.12041981991,1.40193795992,-1.39275880167/sample/sampleassembly.xml'
psi = -0.021732862616062856
hkl2Q = array([[-0.64022017,  0.9484801 ,  0.        ],
       [ 0.67067671,  0.45270403, -0.80916512],
       [-0.67067671, -0.45270403, -0.80916512]])
pp = array([ 2.83770884,  0.97334914,  0.00969096])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0060931468302893761
Q = array([ 3.23187358, -0.74600553, -0.00742745])
E = 49.620052971122107
hkl_projection = array([ 0.60250097,  0.65200651,  0.64007856])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
