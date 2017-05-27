#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-41.0683203991_hkl-14.359456217,2.6901435781,-0.917275426291/sample/sampleassembly.xml'
psi = -0.0036073304592851942
hkl2Q = array([[-0.65730577,  0.9367206 ,  0.        ],
       [ 0.66236149,  0.46478537, -0.80916512],
       [-0.66236149, -0.46478537, -0.80916512]])
pp = array([-0.20451958,  2.9930205 ,  0.36466553])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0023716034466596948
Q = array([ 11.82796892, -11.77412293,  -1.43454306])
E = -41.06832039906601
hkl_projection = array([ 0.9448291 , -0.27264728, -0.46796285])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
