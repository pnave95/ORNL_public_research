#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E33.2675120992_hkl-9.41415553151,-0.363052917038,-0.0635126596282/sample/sampleassembly.xml'
psi = -0.002404903515184563
hkl2Q = array([[-0.65843164,  0.93592957,  0.        ],
       [ 0.66180214,  0.46558148, -0.80916512],
       [-0.66180214, -0.46558148, -0.80916512]])
pp = array([ 1.46821839,  2.61616795, -0.10088901])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0024321023126056313
Q = array([ 6.00034145, -8.95044689,  0.34516198])
E = 33.267512099160626
hkl_projection = array([-0.17019071,  0.83127331,  0.93338216])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
