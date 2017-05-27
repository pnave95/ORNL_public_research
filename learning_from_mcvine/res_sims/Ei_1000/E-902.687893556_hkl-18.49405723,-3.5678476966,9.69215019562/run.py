#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-902.687893556_hkl-18.49405723,-3.5678476966,9.69215019562/sample/sampleassembly.xml'
psi = -0.0007995902653752844
hkl2Q = array([[-0.65993325,  0.93487137,  0.        ],
       [ 0.66105389,  0.46664327, -0.80916512],
       [-0.66105389, -0.46664327, -0.80916512]])
pp = array([ 1.86595447,  2.34908789,  0.4958448 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011418738025111444
Q = array([  3.43927013, -23.47725347,  -4.95557194])
E = -902.68789355621789
hkl_projection = array([-0.78812457, -0.02358559, -0.83728177])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
