#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E-677.441426594_hkl-31.4782295424,-0.498512293937,-2.83060173817/sample/sampleassembly.xml'
psi = -0.0042741139548945544
hkl2Q = array([[-0.65668104,  0.93715868,  0.        ],
       [ 0.66267126,  0.46434362, -0.80916512],
       [-0.66267126, -0.46434362, -0.80916512]])
pp = array([-0.01357333,  2.99996929, -0.28438145])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0011506262467689391
Q = array([ 22.2165651 , -28.4172051 ,   2.69380294])
E = -677.44142659422846
hkl_projection = array([ 0.08974629, -0.00154554, -0.18552013])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
