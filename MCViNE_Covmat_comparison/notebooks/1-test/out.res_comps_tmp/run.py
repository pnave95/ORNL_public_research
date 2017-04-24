#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/lj7/simulations/ARCS/resolution-fit-covmat/debug-Ricky/1-test/out.res_comps_tmp/sample/sampleassembly.xml'
psi = -0.08725694187870671
hkl2Q = array([[-0.57674248,  0.98836455,  0.        ],
       [ 0.69887928,  0.40781852, -0.80916512],
       [-0.69887928, -0.40781852, -0.80916512]])
pp = array([ 2.44150988,  1.74328124,  0.        ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0050371160063350257
Q = array([ 1.59000154, -2.7247883 ,  0.        ])
E = 15.0
hkl_projection = array([1, 0, 0])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=1000)