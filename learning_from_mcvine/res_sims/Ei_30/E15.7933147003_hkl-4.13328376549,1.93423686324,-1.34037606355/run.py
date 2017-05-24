#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E15.7933147003_hkl-4.13328376549,1.93423686324,-1.34037606355/sample/sampleassembly.xml'
psi = -0.007700315736997315
hkl2Q = array([[-0.6534663 ,  0.93940309,  0.        ],
       [ 0.6642583 ,  0.46207045, -0.80916512],
       [-0.6642583 , -0.46207045, -0.80916512]])
pp = array([-1.22211314,  2.73978822,  0.55557436])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0075244340451703275
Q = array([ 4.87615044, -2.36971769, -0.48053144])
E = 15.793314700263352
hkl_projection = array([ 0.54559687, -0.07093974,  0.78111153])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
