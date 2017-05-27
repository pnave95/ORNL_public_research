#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_500_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_500/E27.5423210033_hkl0.665529126927,0.942904506251,-0.46921869007/sample/sampleassembly.xml'
psi = 0.0018206112800823583
hkl2Q = array([[-0.66238053,  0.93313901,  0.        ],
       [ 0.65982892,  0.46837377, -0.80916512],
       [-0.65982892, -0.46837377, -0.80916512]])
pp = array([ 2.98926235, -0.25359532,  0.07579389])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0017048343961774868
Q = array([ 0.49092618,  1.28243265, -0.38329004])
E = 27.542321003308075
hkl_projection = array([ 0.63571708,  0.07235797, -0.93895745])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
