#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E4.13980753933_hkl-2.41955239177,-0.455756784235,-0.0124646725572/sample/sampleassembly.xml'
psi = -0.0019559770034185786
hkl2Q = array([[-0.65885173,  0.93563388,  0.        ],
       [ 0.66159306,  0.46587853, -0.80916512],
       [-0.66159306, -0.46587853, -0.80916512]])
pp = array([ 2.14160236,  2.10084253, -0.32220036])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.007038843396617589
Q = array([ 1.3008473 , -2.47033548,  0.37886847])
E = 4.1398075393327289
hkl_projection = array([-0.1687299 , -0.47436838, -0.94590995])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
