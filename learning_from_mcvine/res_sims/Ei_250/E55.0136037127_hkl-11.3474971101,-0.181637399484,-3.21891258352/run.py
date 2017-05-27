#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_250_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_250/E55.0136037127_hkl-11.3474971101,-0.181637399484,-3.21891258352/sample/sampleassembly.xml'
psi = -0.0036890920535482398
hkl2Q = array([[-0.65722918,  0.93677434,  0.        ],
       [ 0.66239949,  0.46473121, -0.80916512],
       [-0.66239949, -0.46473121, -0.80916512]])
pp = array([ 0.49856671,  2.9582818 , -0.88300731])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.002477544564506347
Q = array([ 9.4697958 , -9.21852758,  2.75160642])
E = 55.013603712726308
hkl_projection = array([ 0.7729431 ,  0.22273083,  0.0913941 ])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
