#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E126.019115915_hkl-12.9823555106,-2.06241552734,0.985877812741/sample/sampleassembly.xml'
psi = -0.002626834354900053
hkl2Q = array([[-0.65822391,  0.93607567,  0.        ],
       [ 0.66190545,  0.46543459, -0.80916512],
       [-0.66190545, -0.46543459, -0.80916512]])
pp = array([ 2.26090133,  1.97188367, -0.12656916])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012137273851839387
Q = array([  6.52761481, -13.57124827,   0.87109677])
E = 126.01911591531325
hkl_projection = array([ 0.89009059,  0.66244025,  0.3574276 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
