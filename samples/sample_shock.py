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

from src.baseshock import BaseShock
import random
import logging

# -------------------------------------------------------------------------
#  class Shock
# -------------------------------------------------------------------------


class Shock(BaseShock):
    #
    #
    # VARIABLES
    #
    #

    #
    #
    # METHODS
    #
    #

    # -------------------------------------------------------------------------
    # do_shock(environment, time, step)
    # This is the main wrapper function for the shocks
    # Here we specify what shocks are doing to the environment at the
    # beginning and the end (step) of the affected sweeps
    # Shocks are distinguished by the shock_type saved in the environment's
    # variables, these are strings for our purposes.
    # -------------------------------------------------------------------------
    def do_shock(self, environment, time, shock_type, step):
        super(Shock, self).do_shock(environment, time, shock_type, step)
    # -------------------------------------------------------------------------
