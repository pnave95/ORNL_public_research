#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_60_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_60/E-52.9352981982_hkl-8.66491686381,3.0403285783,-0.242607371186/sample/sampleassembly.xml'
psi = -0.005702911091236439
hkl2Q = array([[-0.65534136,  0.93809598,  0.        ],
       [ 0.66333403,  0.46339632, -0.80916512],
       [-0.66333403, -0.46339632, -0.80916512]])
pp = array([-1.04278857,  2.81293299,  0.96378906])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0046970519010522934
Q = array([ 7.85616153, -6.60722328, -2.26381841])
E = -52.935298198210063
hkl_projection = array([-0.98498315,  0.6583036 , -0.10372339])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
