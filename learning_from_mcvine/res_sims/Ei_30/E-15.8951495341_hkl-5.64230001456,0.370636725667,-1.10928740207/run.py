#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-15.8951495341_hkl-5.64230001456,0.370636725667,-1.10928740207/sample/sampleassembly.xml'
psi = -0.003792392568296756
hkl2Q = array([[-0.65713241,  0.93684223,  0.        ],
       [ 0.66244749,  0.46466278, -0.80916512],
       [-0.66244749, -0.46466278, -0.80916512]])
pp = array([-0.55708957,  2.94782143, -0.38316169])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067063303551788038
Q = array([ 4.68811025, -4.59827927,  0.59769036])
E = -15.895149534080312
hkl_projection = array([-0.84126943, -0.3596737 , -0.67439041])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
