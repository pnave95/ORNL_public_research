#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-26.6958263763_hkl-4.59837452082,-3.19873548048,-0.573304240571/sample/sampleassembly.xml'
psi = -0.0008428508677647597
hkl2Q = array([[-0.6598928 ,  0.93489992,  0.        ],
       [ 0.66107407,  0.46661468, -0.80916512],
       [-0.66107407, -0.46661468, -0.80916512]])
pp = array([ 2.60851359,  1.48177489, -0.81871983])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023938957503829689
Q = array([ 1.29882974, -5.52408472,  3.05220296])
E = -26.695826376330615
hkl_projection = array([-0.59918002, -0.36369995,  0.46656589])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
