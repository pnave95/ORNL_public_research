#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E11.108004675_hkl-5.24152604552,0.762919358264,1.58270996022/sample/sampleassembly.xml'
psi = -0.002660307363797548
hkl2Q = array([[-0.65819258,  0.9360977 ,  0.        ],
       [ 0.66192103,  0.46541243, -0.80916512],
       [-0.66192103, -0.46541243, -0.80916512]])
pp = array([ 2.03839076,  2.20112769,  0.79002415])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.003444854419959838
Q = array([ 2.90729689, -5.28812122, -1.89800142])
E = 11.108004675020453
hkl_projection = array([-0.99773047,  0.57527404,  0.2580921 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
