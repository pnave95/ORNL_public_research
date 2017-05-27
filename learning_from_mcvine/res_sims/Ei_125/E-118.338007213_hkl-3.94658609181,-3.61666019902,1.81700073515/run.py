#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-118.338007213_hkl-3.94658609181,-3.61666019902,1.81700073515/sample/sampleassembly.xml'
psi = 0.000759321339374451
hkl2Q = array([[-0.66138983,  0.93384146,  0.        ],
       [ 0.66032563,  0.46767323, -0.80916512],
       [-0.66032563, -0.46767323, -0.80916512]])
pp = array([ 2.44729291,  1.73515343, -0.40579807])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0032263502774006608
Q = array([-0.97775367, -6.22666348,  1.45622166])
E = -118.33800721344537
hkl_projection = array([ 0.70433681, -0.58030258,  0.38156121])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
