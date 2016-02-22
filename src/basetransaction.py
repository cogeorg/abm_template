#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# -------------------------------------------------------------------------
#
#  class Transaction
#
# -------------------------------------------------------------------------


class BaseTransaction(object):
    """
    Class variables: __metaclass__
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_transaction_type(self):
        return
    @abc.abstractmethod
    def set_transaction_type(self, _type):
        """
        Class variables: transaction_type
        Local variables: _type
        """
        if not isinstance(_type, str):
            raise TypeError
        else:
            self.transaction_type = _type
        return
    transaction_type = abc.abstractproperty(get_transaction_type, set_transaction_type)

    @abc.abstractmethod
    def get_transaction_asset(self):
        return
    @abc.abstractmethod
    def set_transaction_asset(self, _asset):
        """
        Class variables: transaction_asset
        Local variables: _asset
        """
        if not isinstance(_asset, str):
            raise TypeError
        else:
            self.transaction_asset = _asset
        return
    transaction_asset = abc.abstractproperty(get_transaction_asset, set_transaction_asset)

    @abc.abstractmethod
    def get_transaction_from(self):
        return
    @abc.abstractmethod
    def set_transaction_from(self, _from):
        """
        Class variables: transaction_from
        Local variables: _from
        """
        self.transaction_from = _from
        return
    transaction_from = abc.abstractproperty(get_transaction_from, set_transaction_from)

    @abc.abstractmethod
    def get_transaction_to(self):
        return
    @abc.abstractmethod
    def set_transaction_to(self, _to):
        """
        Class variables: transaction_to
        Local variables: _to
        """
        self.transaction_to = _to
        return
    transaction_to = abc.abstractproperty(get_transaction_to, set_transaction_to)

    @abc.abstractmethod
    def get_transaction_value(self):
        return
    @abc.abstractmethod
    def set_transaction_value(self, _value):
        """
        Class variables: transaction_value
        Local variables: _value
        """
        if not isinstance(_value, float) or isinstance(_value, int):
            raise TypeError
        else:
            self.transaction_value = float(_value)
        return
    transaction_value = abc.abstractproperty(get_transaction_value, set_transaction_value)

    @abc.abstractmethod
    def get_transaction_interest(self):
        return
    @abc.abstractmethod
    def set_transaction_interest(self, _interest):
        """
        Class variables: transaction_interest
        Local variables: _interest
        """
        if not isinstance(_interest, float) or isinstance(_interest, int):
            raise TypeError
        else:
            self.transaction_interest = float(_interest)
        return
    transaction_interest = abc.abstractproperty(get_transaction_interest, set_transaction_interest)

    @abc.abstractmethod
    def get_transaction_maturity(self):
        return
    @abc.abstractmethod
    def set_transaction_maturity(self, _maturity):
        """
        Class variables: transaction_maturity
        Local variables: _maturity
        """
        if not isinstance(_maturity, float) or isinstance(_maturity, int):
            raise TypeError
        else:
            self.transaction_maturity = int(_maturity)
        return
    transaction_maturity = abc.abstractproperty(get_transaction_maturity, set_transaction_maturity)

    @abc.abstractmethod
    def get_transaction_time_of_default(self):
        return
    @abc.abstractmethod
    def set_transaction_time_of_default(self, _time_of_default):
        """
        Class variables: transaction_time_of_default
        Local variables: _time_of_default
        """
        if not isinstance(_time_of_default, float) or isinstance(_time_of_default, int):
            raise TypeError
        else:
            self.transaction_time_of_default = int(_time_of_default)
        return
    transaction_time_of_default = abc.abstractproperty(get_transaction_time_of_default, set_transaction_time_of_default)

    @abc.abstractmethod
    def this_transaction(self, transaction_type, transaction_asset, transaction_from, transaction_to, transaction_value,  transaction_interest,  transaction_maturity, transaction_time_of_default):
        self.transaction_type = transaction_type
        # if transactionType == "I":
        self.transaction_asset = transaction_asset
        # the convention used is that values are positive
        if transaction_value >= 0:
            self.transaction_from = transaction_from
            self.transaction_to = transaction_to
        else:  # negative values reverse direction and delete sign
            self.transaction_from = transaction_to
            self.transaction_to = transaction_from
            transaction_value = abs(transaction_value)
        self.transaction_value = transaction_value
        self.transaction_interest = transaction_interest
        self.transaction_maturity = transaction_maturity
        self.transaction_time_of_default = transaction_time_of_default

    @abc.abstractmethod
    def print_transaction(self):
        print "        <transaction type='" + self.transaction_type + "'>"
        if self.transaction_asset != "":
            print "        <transaction asset='" + self.transaction_asset + "'>"
        if hasattr(self.transaction_from, "identifier"):
            print "            <property type='from' value='" + str(self.transaction_from.identifier) + "'></property>"
        else:
            print "            <property type='from' value='" + str(self.transaction_from) + "'></property>"
        if hasattr(self.transaction_to, "identifier"):
            print "            <property type='to' value='" + str(self.transaction_to.identifier) + "'></property>"
        else:
            print "            <property type='to' value='" + str(self.transaction_to) + "'></property>"
        print "            <property type='value' value='" + str(self.transaction_value) + "'></property>"
        print "            <property type='interest' value='" + str(self.transaction_interest) + "'></property>"
        print "            <property type='maturity' value='" + str(self.transaction_maturity) + "'></property>"
        print "            <property type='time_of_default' value='" + str(self.transaction_time_of_default) + "'></property>"
        print "        </transaction>"

    @abc.abstractmethod
    def write_transaction(self):
        text = "        <transaction type='" + self.transaction_type + "'>\n"
        if self.transaction_asset != "":
            text += "        <transaction asset='" + self.transaction_asset + "'>\n"
        if hasattr(self.transaction_from, "identifier"):
            text += "            <property type='from' value='" + str(self.transaction_from.identifier) + "'></property>\n"
        else:
            text += "            <property type='from' value='" + str(self.transaction_from) + "'></property>\n"
        if hasattr(self.transaction_to, "identifier"):
            text += "            <property type='to' value='" + str(self.transaction_to.identifier) + "'></property>\n"
        else:
            text += "            <property type='to' value='" + str(self.transaction_to) + "'></property>\n"
        text += "            <property type='value' value='" + str(self.transaction_value) + "'></property>\n"
        text += "            <property type='interest' value='" + str(self.transaction_interest) + "'></property>\n"
        text += "            <property type='maturity' value='" + str(self.transaction_maturity) + "'></property>\n"
        text += "            <property type='time_of_default' value='" + str(self.transaction_time_of_default) + "'></property>\n"
        text += "        </transaction>\n"

        return text
