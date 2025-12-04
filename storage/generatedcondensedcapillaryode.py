# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.4.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 9
VARIABLE_COUNT = 59


class VariableType(Enum):
    VARIABLE_OF_INTEGRATION = 0
    STATE = 1
    CONSTANT = 2
    COMPUTED_CONSTANT = 3
    ALGEBRAIC = 4


VOI_INFO = {"name": "t", "units": "second", "component": "complete_capillary", "type": VariableType.VARIABLE_OF_INTEGRATION}

STATE_INFO = [
    {"name": "v_input_vessel", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_input_vessel", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_d_input_vessel", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "v_out_pericyte_0", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_pericyte_0", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "v_out_pericyte_1", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_pericyte_1", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_capillary_0", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE},
    {"name": "q_C_capillary_1", "units": "m3", "component": "complete_capillary", "type": VariableType.STATE}
]

VARIABLE_INFO = [
    {"name": "r_input_vessel", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "d_vessel", "units": "per_m", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "c_vessel", "units": "dimensionless", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "b_vessel", "units": "per_m", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "a_vessel", "units": "dimensionless", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "h_input_vessel", "units": "metre", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "l_input_vessel", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "rho", "units": "Js2_per_m5", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "I_input_vessel", "units": "Js2_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "E_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "C_input_vessel", "units": "m6_per_J", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "mu", "units": "Js_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "R_input_vessel", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_v_input_vessel", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "theta_input_vessel", "units": "dimensionless", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "g", "units": "m_per_s2", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "beta_g", "units": "dimensionless", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "u_d_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "u_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "v_in_input_vessel", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "u_ext_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "u_C_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "v_out_2_input_vessel", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "v_out_1_input_vessel", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "u_C_d_input_vessel", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "R_pericyte_0", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "u_pericyte_0", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "u_ext_pericyte_0", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "C_pericyte_0", "units": "m6_per_J", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "R_pericyte_1", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "u_pericyte_1", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "u_ext_pericyte_1", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "C_pericyte_1", "units": "m6_per_J", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "r_capillary_0", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "h_capillary_0", "units": "metre", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "l_capillary_0", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "I_capillary_0", "units": "Js2_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "E_capillary_0", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "C_capillary_0", "units": "m6_per_J", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_capillary_0", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_capillary_0", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "v_out_2_capillary_0", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "v_out_1_capillary_0", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "v_out_total_capillary_0", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_ext_capillary_0", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "r_capillary_1", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "h_capillary_1", "units": "metre", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "I_capillary_1", "units": "Js2_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "E_capillary_1", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "l_capillary_1", "units": "metre", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "C_capillary_1", "units": "m6_per_J", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "R_capillary_1", "units": "Js_per_m6", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_capillary_1", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.ALGEBRAIC},
    {"name": "v_out_2_capillary_1", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "v_out_1_capillary_1", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "v_out_total_capillary_1", "units": "m3_per_s", "component": "complete_capillary", "type": VariableType.COMPUTED_CONSTANT},
    {"name": "u_ext_capillary_1", "units": "J_per_m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "q_C_init_capillary_0", "units": "m3", "component": "complete_capillary", "type": VariableType.CONSTANT},
    {"name": "q_C_init_capillary_1", "units": "m3", "component": "complete_capillary", "type": VariableType.CONSTANT}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_variables_array():
    return [nan]*VARIABLE_COUNT


def initialise_variables(states, rates, variables):
    variables[0] = 4.0e-06
    variables[1] = -11.14
    variables[2] = 0.1324
    variables[3] = -505.3
    variables[4] = 0.2802
    variables[6] = 2.0e-05
    variables[7] = 1050.0
    variables[9] = 400000.0
    variables[11] = 0.004
    variables[14] = 0.0
    variables[15] = 9.81
    variables[16] = 0.0
    variables[19] = 1.0e-07
    variables[20] = 0.0
    variables[25] = 1.0
    variables[27] = 0.0
    variables[28] = 1.0
    variables[29] = 1.0
    variables[31] = 0.0
    variables[32] = 1.0
    variables[33] = 2.0e-06
    variables[35] = 2.0e-05
    variables[37] = 400000.0
    variables[41] = 0.25e-7
    variables[42] = 0.25e-7
    variables[44] = 0.0
    variables[45] = 2.0e-06
    variables[48] = 400000.0
    variables[49] = 2.0e-05
    variables[53] = 0.25e-7
    variables[54] = 0.25e-7
    variables[56] = 0.0
    variables[57] = 1.0e-18
    variables[58] = 1.0e-18
    states[0] = 0.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    states[6] = 0.0
    states[7] = variables[57]
    states[8] = variables[58]


def compute_computed_constants(variables):
    variables[5] = variables[0]*(variables[4]*exp(variables[3]*variables[0])+variables[2]*exp(variables[1]*variables[0]))
    variables[8] = variables[7]*variables[6]/(3.14159265358979*pow(variables[0], 2.0))
    variables[10] = 2.0*3.14159265358979*pow(variables[0], 3.0)*variables[6]/(variables[9]*variables[5])
    variables[12] = 8.0*variables[11]*variables[6]/(3.14159265358979*pow(variables[0], 4.0))
    variables[13] = 0.01/variables[10]
    variables[34] = variables[33]*(variables[4]*exp(variables[3]*variables[33])+variables[2]*exp(variables[1]*variables[33]))
    variables[36] = variables[7]*variables[35]/(3.14159265358979*pow(variables[33], 2.0))
    variables[38] = 2.0*3.14159265358979*pow(variables[33], 3.0)*variables[35]/(variables[37]*variables[34])
    variables[39] = 8.0*variables[11]*variables[35]/(3.14159265358979*pow(variables[33], 4.0))
    variables[43] = variables[42]+variables[41]
    variables[46] = variables[45]*(variables[4]*exp(variables[3]*variables[45])+variables[2]*exp(variables[1]*variables[45]))
    variables[47] = variables[7]*variables[35]/(3.14159265358979*pow(variables[33], 2.0))
    variables[50] = 2.0*3.14159265358979*pow(variables[45], 3.0)*variables[49]/(variables[48]*variables[46])
    variables[51] = 8.0*variables[11]*variables[49]/(3.14159265358979*pow(variables[45], 4.0))
    variables[55] = variables[54]+variables[53]


def compute_rates(voi, states, rates, variables):
    variables[21] = states[1]/(variables[10]/2.0)+variables[20]
    variables[18] = variables[21]
    variables[24] = states[2]/(variables[10]/2.0)+variables[20]
    variables[26] = states[4]/variables[28]+variables[27]
    variables[17] = (variables[24]+2.0*variables[13]*(states[0]+variables[26]/variables[25]))/(1.0+2.0*variables[13]*1.0/variables[25])
    rates[0] = (variables[18]-variables[17]-variables[12]*states[0]-variables[16]*variables[7]*variables[15]*variables[6]*cos(variables[14]*3.14159265358979/180.0))/variables[8]
    rates[1] = variables[19]-states[0]
    variables[30] = states[6]/variables[32]+variables[31]
    variables[22] = (variables[17]-variables[30])/variables[29]
    variables[23] = (variables[17]-variables[26])/variables[25]
    rates[2] = states[0]-variables[23]-variables[22]
    rates[4] = variables[23]-states[3]
    rates[6] = variables[22]-states[5]
    variables[40] = states[7]/variables[38]+variables[44]
    rates[3] = (variables[26]-variables[40]-variables[39]*states[3])/variables[36]
    rates[7] = states[3]-variables[43]
    variables[52] = states[8]/variables[50]+variables[56]
    rates[5] = (variables[30]-variables[52]-variables[51]*states[5])/variables[47]
    rates[8] = states[5]-variables[55]


def compute_variables(voi, states, rates, variables):
    variables[21] = states[1]/(variables[10]/2.0)+variables[20]
    variables[24] = states[2]/(variables[10]/2.0)+variables[20]
    variables[18] = variables[21]
    variables[26] = states[4]/variables[28]+variables[27]
    variables[17] = (variables[24]+2.0*variables[13]*(states[0]+variables[26]/variables[25]))/(1.0+2.0*variables[13]*1.0/variables[25])
    variables[23] = (variables[17]-variables[26])/variables[25]
    variables[30] = states[6]/variables[32]+variables[31]
    variables[22] = (variables[17]-variables[30])/variables[29]
    variables[40] = states[7]/variables[38]+variables[44]
    variables[52] = states[8]/variables[50]+variables[56]
