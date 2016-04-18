#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Runner
#
# -------------------------------------------------------------------------


class BaseRunner(object):
    """
    Class variables: __metaclass__, identifier, num_sweeps
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_identifier(self):
        return
    @abc.abstractmethod
    def set_identifier(self, _identifier):
        """
        Class variables: identifier
        Local variables: _identifier
        """
        if not isinstance(_identifier, str):
            raise TypeError
        else:
            self.identifier = _identifier
        return
    identifier = abc.abstractproperty(get_identifier, set_identifier)

    @abc.abstractmethod
    def get_num_sweeps(self):
        return
    @abc.abstractmethod
    def set_num_sweeps(self, _num_sweeps):
        """
        Class variables: num_sweeps
        Local variables: _num_sweeps
        """
        if not isinstance(_num_sweeps, int):
            raise TypeError
        else:
            self.num_sweeps = _num_sweeps
        return
    num_sweeps = abc.abstractproperty(get_num_sweeps, set_num_sweeps)

    @abc.abstractmethod
    def __init__(self, model_config):
        """
        Class variables:
        Local variables: _params, model_config
        """
        _num_sweeps = model_config.get_model_parameters()['num_sweeps']

        self.set_identifier(model_config.identifier)
        self.set_num_sweeps(_num_sweeps)

    @abc.abstractmethod
    def do_run(self):
        pass
