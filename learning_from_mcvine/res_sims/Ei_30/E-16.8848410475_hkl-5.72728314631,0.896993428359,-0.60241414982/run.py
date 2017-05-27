#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-16.8848410475_hkl-5.72728314631,0.896993428359,-0.60241414982/sample/sampleassembly.xml'
psi = -0.0037898611620797436
hkl2Q = array([[-0.65713478,  0.93684057,  0.        ],
       [ 0.66244632,  0.46466446, -0.80916512],
       [-0.66244632, -0.46466446, -0.80916512]])
pp = array([-0.59076916,  2.94125684,  0.15016346])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0066887114617282615
Q = array([ 4.756874  , -4.66882978, -0.23836328])
E = -16.884841047467056
hkl_projection = array([ 0.38157448, -0.07854206, -0.86013037])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
