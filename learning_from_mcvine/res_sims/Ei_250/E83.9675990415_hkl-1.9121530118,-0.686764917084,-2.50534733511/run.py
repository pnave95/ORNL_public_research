#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E83.9675990415_hkl-1.9121530118,-0.686764917084,-2.50534733511/sample/sampleassembly.xml'
psi = -0.00928189498417172
hkl2Q = array([[-0.65197974,  0.94043543,  0.        ],
       [ 0.66498827,  0.46101929, -0.80916512],
       [-0.66498827, -0.46101929, -0.80916512]])
pp = array([ 2.98134739,  0.33401754, -0.89883302])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025205568078672772
Q = array([ 2.45602099, -0.95985485,  2.58294588])
E = 83.967599041504002
hkl_projection = array([-0.70777102,  0.78937443,  0.70184816])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
