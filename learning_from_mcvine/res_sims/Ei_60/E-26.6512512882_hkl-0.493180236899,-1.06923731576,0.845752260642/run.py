#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-26.6512512882_hkl-0.493180236899,-1.06923731576,0.845752260642/sample/sampleassembly.xml'
psi = 0.0032932036039049787
hkl2Q = array([[-0.66375395,  0.93216258,  0.        ],
       [ 0.65913848,  0.46934492, -0.80916512],
       [-0.65913848, -0.46934492, -0.80916512]])
pp = array([ 2.93344665,  0.62840335, -0.08364881])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0047555479932389639
Q = array([-0.93489299, -1.35851478,  0.18083631])
E = -26.651251288217736
hkl_projection = array([ 0.74629224,  0.06414976,  0.80686526])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
