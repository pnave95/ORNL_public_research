#!/usr/bin/env python
import mcvine.cli
from numpy import array
from mcvine_workflow.singlextal.resolution import use_res_comps as urc
beam_neutrons_path = '/SNS/users/p63/ORNL_public_research/MCViNE_Covmat_comparison/mcvine_resolution/beams/beam_30_1e9/out/neutrons'
instrument = urc.instrument('ARCS', '3.*meter', '13.6*meter', '-0.15*meter')
samplexmlpath = '/SNS/users/p63/ORNL_public_research/learning_from_mcvine/res_sims/Ei_30/E-12.9888592651_hkl-4.54456745718,0.801291654068,0.855568834471/sample/sampleassembly.xml'
psi = -0.002566579495103484
hkl2Q = array([[-0.65828031,  0.93603601,  0.        ],
       [ 0.66187741,  0.46547447, -0.80916512],
       [-0.66187741, -0.46547447, -0.80916512]])
pp = array([ 0.59337504,  2.94073223,  0.92134383])
pixel = urc.pixel('0.5*inch', 'meter/128', '10*atm', position=(pp[1], pp[2], pp[0]))
t_m2p = 0.0067796346040948467
Q = array([ 2.95567444, -4.27914341, -1.34067371])
E = -12.988859265069774
hkl_projection = array([-0.49791622, -0.59554849,  0.13641943])
urc.run(
    beam_neutrons_path, instrument, samplexmlpath, psi, hkl2Q, pixel, t_m2p,
    Q, E, hkl_projection, Nbuffer=100000)
