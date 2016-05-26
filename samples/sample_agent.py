#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:150]
# -*- coding: utf-8 -*-

"""
abm_template is a multi-agent simulator template for financial  analysis
Copyright (C) 2016 Co-Pierre Georg (co-pierre.georg@uct.ac.za)
Pawel Fiedor (pawel.fiedor@uct.ac.za)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

# import logging
# import math
from src.baseagent import BaseAgent

# ============================================================================
#
# class Agent
#
# ============================================================================


class Agent(BaseAgent):

    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Agent, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        super(Agent, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        super(Agent, self).set_state_variables(_value)

    def __str__(self):
        return super(Agent, self).__str__()

    def __init__(self, _identifier, _params, _variables):
        self.identifier = ""
        self.parameters = {}
        self.state_variables = {}
        self.accounts = []
        super(Agent, self).__init__(_identifier, _params, _variables)

    def __getattr__(self, attr):
        return super(Agent, self).__getattr__(attr)

    def append_parameters(self, value):
        super(Agent, self).append_parameters(value)

    def append_state_variables(self, value):
        super(Agent, self).append_state_variables(value)

    def check_consistency(self):
        assets = []
        liabilities = []
        return super(Agent, self).check_consistency(assets, liabilities)

    def clear_accounts(self):
        super(Agent, self).clear_accounts()

    def get_account(self,  type_):
        return super(Agent, self).get_account(type_)

    def get_account_num_transactions(self,  type_):
        return super(Agent, self).get_account_num_transactions(type_)

    def get_parameters_from_file(self,  bank_filename, environment):
        super(Agent, self).get_parameters_from_file(bank_filename, environment)

    def get_transactions_from_file(self, filename, environment):
        super(Agent, self).get_transactions_from_file(filename, environment)

    def purge_accounts(self, environment):
        super(Agent, self).purge_accounts(environment)

    def add_transaction(self, type_, asset,  from_id,  to_id,  amount,  interest,  maturity, time_of_default, environment):
        from sample.sample_transaction import Transaction
        transaction = Transaction()
        transaction.this_transaction(type_, asset, from_id,  to_id,  amount,  interest,  maturity,  time_of_default)
        transaction.add_transaction(environment)
