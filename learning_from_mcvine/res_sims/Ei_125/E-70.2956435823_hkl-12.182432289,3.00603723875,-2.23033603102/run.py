#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-70.2956435823_hkl-12.182432289,3.00603723875,-2.23033603102/sample/sampleassembly.xml'
psi = -0.0061725330550715055
hkl2Q = array([[-0.65490074,  0.93840364,  0.        ],
       [ 0.66355158,  0.46308475, -0.80916512],
       [-0.66355158, -0.46308475, -0.80916512]])
pp = array([-1.12629058,  2.78055202,  0.19376487])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032740611223464338
Q = array([ 11.45288763,  -9.00715423,  -0.62767036])
E = -70.295643582345377
hkl_projection = array([-0.53283261, -0.24684754,  0.15829603])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
