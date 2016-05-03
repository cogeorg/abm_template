#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Shock
#
# -------------------------------------------------------------------------


class BaseShock(object):

    @abc.abstractmethod
    def do_shock(self, environment, time, shock_type, step):
        pass
