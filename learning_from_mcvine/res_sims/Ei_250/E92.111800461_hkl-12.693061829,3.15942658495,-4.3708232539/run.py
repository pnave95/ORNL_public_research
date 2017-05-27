#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E92.111800461_hkl-12.693061829,3.15942658495,-4.3708232539/sample/sampleassembly.xml'
psi = -0.005694743765698101
hkl2Q = array([[-0.65534902,  0.93809063,  0.        ],
       [ 0.66333025,  0.46340174, -0.80916512],
       [-0.66333025, -0.46340174, -0.80916512]])
pp = array([-0.78751831,  2.894791  , -0.33709065])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0025140534067942112
Q = array([ 13.31342812,  -8.41771153,   0.98021993])
E = 92.111800461032715
hkl_projection = array([ 0.73456468, -0.09520588,  0.20689067])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
