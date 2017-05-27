#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_1000_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_1000/E46.5702935597_hkl-2.19605076783,-1.71442758891,-0.662582668092/sample/sampleassembly.xml'
psi = -0.001613097209360343
hkl2Q = array([[-0.65917251,  0.93540792,  0.        ],
       [ 0.66143328,  0.46610535, -0.80916512],
       [-0.66143328, -0.46610535, -0.80916512]])
pp = array([ 2.97889171,  0.35525225, -0.26853881])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0012047038009146164
Q = array([ 0.75185105, -2.54447383,  1.92339378])
E = 46.570293559689844
hkl_projection = array([-0.81438305, -0.63795535, -0.80582691])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
