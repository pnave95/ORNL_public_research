#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-8.07554582894_hkl-7.27022428026,1.00311118187,-1.52866819221/sample/sampleassembly.xml'
psi = -0.005474242103887786
hkl2Q = array([[-0.65555586,  0.9379461 ,  0.        ],
       [ 0.66322805,  0.46354799, -0.80916512],
       [-0.66322805, -0.46354799, -0.80916512]])
pp = array([-0.54270154,  2.9505042 , -0.22225552])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0048509465964134257
Q = array([ 6.44518519, -5.64547729,  0.4252624 ])
E = -8.0755458289412942
hkl_projection = array([ 0.94322254, -0.2283439 ,  0.24828847])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
