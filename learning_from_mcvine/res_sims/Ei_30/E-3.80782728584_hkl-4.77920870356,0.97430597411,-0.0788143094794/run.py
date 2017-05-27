#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-3.80782728584_hkl-4.77920870356,0.97430597411,-0.0788143094794/sample/sampleassembly.xml'
psi = -0.003580758892155478
hkl2Q = array([[-0.65733066,  0.93670314,  0.        ],
       [ 0.66234914,  0.46480297, -0.80916512],
       [-0.66234914, -0.46480297, -0.80916512]])
pp = array([-0.01500457,  2.99996248,  0.5451874 ])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.006883145284006415
Q = array([ 3.83905375, -3.98720636, -0.72460062])
E = -3.8078272858411353
hkl_projection = array([-0.68383732,  0.97315648, -0.35618905])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
