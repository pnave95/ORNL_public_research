#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E12.4549424657_hkl-5.15526598039,-0.852641783285,0.226560504705/sample/sampleassembly.xml'
psi = -0.002433918936874252
hkl2Q = array([[-0.65840448,  0.93594867,  0.        ],
       [ 0.66181565,  0.46556227, -0.80916512],
       [-0.66181565, -0.46556227, -0.80916512]])
pp = array([ 2.07971319,  2.16212697, -0.20560117])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0034283407955583434
Q = array([ 2.68001725, -5.3275002 ,  0.50660313])
E = 12.454942465730113
hkl_projection = array([ 0.59149509, -0.25956739,  0.93128543])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
