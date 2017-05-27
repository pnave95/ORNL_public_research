#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E-231.786078966_hkl-1.24858181672,-0.360407607302,5.60668099821/sample/sampleassembly.xml'
psi = 0.0028126272662375557
hkl2Q = array([[-0.66330589,  0.93248145,  0.        ],
       [ 0.65936396,  0.4690281 , -0.80916512],
       [-0.65936396, -0.4690281 , -0.80916512]])
pp = array([ 2.88853652,  0.81015849,  0.86782611])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0022925508214477887
Q = array([-3.10629149, -3.96301159, -4.24510142])
E = -231.78607896581428
hkl_projection = array([ 0.39172517,  0.91954442,  0.0104227 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
