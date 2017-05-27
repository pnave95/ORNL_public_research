#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E9.6673129909_hkl-2.50949893347,-0.438985775378,-0.661967420071/sample/sampleassembly.xml'
psi = -0.002976676264092911
hkl2Q = array([[-0.65789639,  0.93630589,  0.        ],
       [ 0.66206824,  0.465203  , -0.80916512],
       [-0.66206824, -0.465203  , -0.80916512]])
pp = array([ 2.00643211,  2.23029823, -0.88465377])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0072653496831406091
Q = array([ 1.79861936, -2.24592689,  0.89085292])
E = 9.6673129908988855
hkl_projection = array([-0.81246938,  0.99127251,  0.92883422])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
