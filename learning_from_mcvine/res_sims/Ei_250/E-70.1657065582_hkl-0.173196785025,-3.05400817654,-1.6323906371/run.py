#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-70.1657065582_hkl-0.173196785025,-3.05400817654,-1.6323906371/sample/sampleassembly.xml'
psi = 0.003560265875087647
hkl2Q = array([[-0.66400287,  0.93198528,  0.        ],
       [ 0.65901311,  0.46952093, -0.80916512],
       [-0.65901311, -0.46952093, -0.80916512]])
pp = array([ 2.99268171,  0.20941862, -0.95805762])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023691327059465971
Q = array([-0.82186144, -0.82889604,  3.79207044])
E = -70.165706558158433
hkl_projection = array([-0.28694895, -0.57350049, -0.10048017])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
