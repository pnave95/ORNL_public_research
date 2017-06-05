#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/6-check-simple-cases-1/out.res_comps_tmp/sample/sampleassembly.xml'
psi = 0.11772611892360563
hkl2Q = array([[-0.73798758,  6.23969486,  0.        ],
       [ 0.        ,  0.        ,  6.28318531],
       [ 6.23969486,  0.73798758,  0.        ]])
pp = array([ 2.29795884,  1.92857076,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032978277287488969
Q = array([ 0.70472623, -5.95846968,  0.        ])
E = -51.80304616018887
hkl_projection = array([ 1.,  0.,  0.])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
