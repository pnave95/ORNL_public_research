#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/notebooks/3-generate-samples-for-fitting/tmp.use_res_comps/E12.9818684844_hkl-0.656429792334,-0.493078362965,-0.0831954995442/sample/sampleassembly.xml'
psi = -0.0010985129776326563
hkl2Q = array([[-0.65965376,  0.9350686 ,  0.        ],
       [ 0.66119335,  0.46644565, -0.80916512],
       [-0.66119335, -0.46644565, -0.80916512]])
pp = array([ 2.99798014,  0.11006843, -0.06375814])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012001211206293619
Q = array([ 0.16200456, -0.80499496,  0.46630071])
E = 12.981868484371603
hkl_projection = array([0, 0, 1])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
