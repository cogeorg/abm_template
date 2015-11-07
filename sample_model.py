#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import math

from basemodel import BaseModel

from config import Config
from agent import Agent


class Model(BaseModel):
    """
    Class variables: identifier, model_parameters, agents, interactions, steps_per_state_variable, par_keys, par_lower, par_upper, par_current, par_step, precision
    """
    identifier = ""
    model_parameters = {}
    agents = []
    interactions = None

    def __init__(self, model_config):
        super(Model, self).__init__(model_config)

    def get_identifier(self):
        return self.identifier
    def set_identifier(self, _value):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        super(Model, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters
    def set_model_parameters(self, _value):
        """
        Class variables: model_parameters
        Local variables: _params
        """
        super(Model, self).set_model_parameters(_value)

    def get_agents(self):
        return self.agents
    def set_agents(self, _value):
        """
        Class variables: agents
        Local variables: _agents
        """
        super(Model, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions
    def set_interactions(self, _value):
        """
        Class variables: interactions
        Local variables: _interactions
        """
        super(Model, self).set_interactions(_value)

    def __str__(self):
        return super(Model, self).__str__()


    def initialize_agents(self):
        super(Model, self).initialize_agents()

    def get_agent_by_id(self, _id):
        """
        Class variables: agents
        Local variables: _id, agent_iterator
        """
        for agent_iterator in self.agents:
            if agent_iterator.identifier == _id:
                return agent_iterator

    def check_agent_homogeneity(self):
        """
        Class variables: agents
        Local variables: parameter_iterator, temp_parameter, agent_iterator, temp_state_variable
        """
        for parameter_iterator in self.agents[0].parameters:
            temp_parameter = self.agents[0].parameters[parameter_iterator]
            for agent_iterator in self.agents:
                if agent_iterator.parameters[parameter_iterator] != temp_parameter:
                    return False
                temp_parameter = agent_iterator.parameters[parameter_iterator]
        for parameter_iterator in self.agents[0].state_variables:
            temp_state_variable = self.agents[0].state_variables[parameter_iterator]
            for agent_iterator in self.agents:
                if agent_iterator.state_variables[parameter_iterator] != temp_state_variable:
                    return False
                temp_state_variable == agent_iterator.state_variables[parameter_iterator]
        return True

    # TODO this code is fairly general and should be generalized further and then moved to the BaseAgent class
    def compute_equilibrium_recursive(self, agentA, agentB):
        """
        Class variables: par_keys, par_lower, par_upper, par_current, par_step, steps_per_state_variable, precision
        Local variables: agentA, agentB, state_key, state_var
        """
        self.par_keys = []
        self.par_lower = []
        self.par_upper = []
        self.par_step  = []
        self.par_current = []
        for state_key, state_var in agentA.state_variables:
            self.par_keys.append(str(state_key))
            self.par_lower.append(float(state_var[0]))
            self.par_upper.append(float(state_var[1]))
            self.par_step.append((self.par_upper[-1] - self.par_lower[-1]) / self.steps_per_state_variable)
        
        self.precision = 0.01
        self.par_current = self.par_lower
        self.loop_over_dimension(0, agentA, agentB)

    # TODO this code is fairly general and should be generalized further and then moved to the BaseAgent class
    def loop_over_dimension(self, recursion_level, agentA, agentB):
        """
        Class variables: par_current, par_upper, par_lower
        Local variables: agentA, agentB, recursion_level
        """
        while self.par_current[recursion_level] <= self.par_upper[recursion_level]:
            if (recursion_level+1) < len(self.par_upper):
                self.par_current[recursion_level+1] = self.par_lower[recursion_level+1]
                self.loop_over_dimension(recursion_level+1, agentA, agentB)
            elif (recursion_level+1) == len(self.par_upper):
                self.check_fixed_point(agentA, agentB)
            self.par_current[recursion_level] += self.par_step[recursion_level]

    # TODO this code is fairly general and should be generalized further and then moved to the BaseAgent class
    def check_fixed_point(self, agentA, agentB):
        """
        Class variables: par_keys, par_current
        Local variables: agentA, agentB, state_iterator, ret_B, ret_A, i, x, y
        """
        for state_iterator in range(0,len(self.par_keys)):
                    agentA.state_variables[self.par_keys[state_iterator]] = self.par_current[state_iterator]

                # then get the best response of B given the current portfolio choice of A
                ret_B = agentB.get_best_response(self.par_current)

                # and then get the best response of A given the best response of B
                ret_A = agentA.get_best_response(ret_B)

                # check if we have a fixed point
                if all(i < self.precision for i in [abs(x) - y for x, y in zip(ret_A, self.par_current)]):
                    # here we have to write out the results
                    pass

    def do_update(self):
        """
        Class variables: agents, steps_per_state_variable, model_parameters
        Local variables: agentA, agentB
        """
        # equilibrium is found by iterating over all possible variable choices for agent A, communicating them to
        # agent B, obtaining B's best response by iterating over all possible variable choices for B, communicating
        # B's best response back to A, and computing A's best response. Any fixed point of this procedure is an
        # equilibrium
        agentA = self.agents[0]
        agentB = self.agents[1]

        self.steps_per_state_variable = math.pow(float(self.model_parameters['num_sweeps']),1.0/len(agentA.state_variables))
        self.compute_equilibrium_recursive(agentA, agentB)

        # we need the stepwidth
        #print self.model_parameters
        #print agentA.state_variables.keys(), agentA.state_variables
