#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_125_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_125/E-28.9960109738_hkl0.449754603396,-1.66837113469,-1.37782319976/sample/sampleassembly.xml'
psi = -0.00821512172940238
hkl2Q = array([[-0.6529826 ,  0.93973938,  0.        ],
       [ 0.66449609,  0.46172842, -0.80916512],
       [-0.66449609, -0.46172842, -0.80916512]])
pp = array([ 2.99818554, -0.10432389, -0.89132466])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0033580889864459522
Q = array([-0.4867499 ,  0.28849787,  2.46487419])
E = -28.996010973815032
hkl_projection = array([ 0.66874012,  0.48318344, -0.23497107])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
