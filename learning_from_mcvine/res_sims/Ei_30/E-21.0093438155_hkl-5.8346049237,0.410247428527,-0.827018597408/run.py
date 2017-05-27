#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-21.0093438155_hkl-5.8346049237,0.410247428527,-0.827018597408/sample/sampleassembly.xml'
psi = -0.0035400440941426555
hkl2Q = array([[-0.6573688 ,  0.93667637,  0.        ],
       [ 0.66233022,  0.46482994, -0.80916512],
       [-0.66233022, -0.46482994, -0.80916512]])
pp = array([-0.50546132,  2.95711157, -0.20393513])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066486028102334966
Q = array([ 4.65496592, -4.8900183 ,  0.33723669])
E = -21.00934381553952
hkl_projection = array([ 0.37890794,  0.51545431, -0.26404766])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
