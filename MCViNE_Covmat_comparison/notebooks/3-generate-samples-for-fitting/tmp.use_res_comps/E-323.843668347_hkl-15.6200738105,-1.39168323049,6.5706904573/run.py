#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E-323.843668347_hkl-15.6200738105,-1.39168323049,6.5706904573/sample/sampleassembly.xml'
psi = -0.0014992316159705744
hkl2Q = array([[-0.65927901,  0.93533286,  0.        ],
       [ 0.66138021,  0.46618066, -0.80916512],
       [-0.66138021, -0.46618066, -0.80916512]])
pp = array([ 2.04411857,  2.19580948,  0.50223672])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011733026791340101
Q = array([  5.03183047, -18.32187291,  -4.19067199])
E = -323.84366834704758
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
