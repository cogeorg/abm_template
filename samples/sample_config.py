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
from src.baseconfig import BaseConfig

# ============================================================================
#
# class Config
#
# ============================================================================


class Config(BaseConfig):

    identifier = ""
    static_parameters = {}
    variable_parameters = {}
    agents = []

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Config, self).set_identifier(_value)

    def get_static_parameters(self):
        return self.static_parameters

    def set_static_parameters(self, _value):
        super(Config, self).set_static_parameters(_value)

    def get_variable_parameters(self):
        return self.variable_parameters

    def set_variable_parameters(self, _value):
        super(Config, self).set_variable_parameters(_value)

    def __str__(self):
        super(Config, self).__str__()

    def __init__(self):
        self.identifier = ""
        self.static_parameters = {}
        self.variable_parameters = {}
        self.agents = []
        super(Config, self).__init__()

    def read_xml_config_file(self, config_file_name):
        super(Config, self).read_xml_config_file(config_file_name)

    def __getattr__(self, attr):
        return super(Config, self).__getattr__(attr)

    def add_static_parameter(self, name, value):
        super(Config, self).add_static_parameter(name, value)

    def add_variable_parameter(self, name, range_from, range_to):
        super(Config, self).add_variable_parameter(name, range_from, range_to)

    def agents_generator(self):
        return super(Config, self).agents_generator()

    def check_global_transaction_balance(self, type_):
        super(Config, self).check_global_transaction_balance(type_)

    def get_agent_by_id(self, ident):
        return super(Config, self).get_agent_by_id(ident)

    def print_parameters(self):
        super(Config, self).print_parameters()

    def write_environment_file(self,  file_name):
        super(Config, self).write_environment_file(file_name)

    def accrue_interests(self):
        super(Config, self).accrue_interests()

    assets = {}
    shocks = []

    def get_assets(self):
        return self.assets

    def set_assets(self, value):
        super(Config, self).set_assets(value)

    def get_shocks(self):
        return self.shocks

    def set_shocks(self, value):
        super(Config, self).set_shocks(value)

    def add_shock(self, shock):
        super(Config, self).add_shock(shock)

    def update_asset_returns(self):
        super(Config, self).update_asset_returns()
