#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-7.22959305427_hkl-2.48262161293,-1.32912940956,-0.231972796101/sample/sampleassembly.xml'
psi = -0.0011952045335984808
hkl2Q = array([[-0.65956335,  0.93513238,  0.        ],
       [ 0.66123844,  0.46638172, -0.80916512],
       [-0.66123844, -0.46638172, -0.80916512]])
pp = array([ 2.14844179,  2.09384762, -0.93352304])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006861900024904795
Q = array([ 0.91196409, -2.83327363,  1.26318945])
E = -7.2295930542744635
hkl_projection = array([ 0.54157156, -0.26103183, -0.6142437 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
