#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import logging

__author__ = """Paweł Fiedor (pawel.fiedor@uct.ac.za)"""

# ============================================================================
#
# class BaseMeasurement
#
# ============================================================================


class BaseMeasurement(object):
    #
    # VARIABLES
    #

    # identifier for usual purposes
    identifier = ""
    # Now we set up a config for the measurements
    # see notes on the xml config file in the method below
    config = {}
    # environment for access
    environment = type('', (), {})()
    # filename for the output csv
    # runner for access
    runner = type('', (), {})()
    filename = ""
    # and the file we're writing to
    file = None
    # plus the csv writer
    csv_writer = None

    #
    # METHODS
    #

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
    # identifier of the specific environment used for distinguishing them / logging
    # identifier should be a string

    @abc.abstractmethod
    def get_config(self):
        return
    @abc.abstractmethod
    def set_config(self, _config):
        """
        Class variables: config
        Local variables: _config
        """
        if not isinstance(_config, dict):
            raise TypeError
        else:
            self.config = _config
        return
    config = abc.abstractproperty(get_config, set_config)
    # config used to model the output file
    # config should be a dictionary

    @abc.abstractmethod
    def get_filename(self):
        return
    @abc.abstractmethod
    def set_filename(self, _filename):
        """
        Class variables: filename
        Local variables: _filename
        """
        if not isinstance(_filename, str):
            raise TypeError
        else:
            self.filename = _filename
        return
    filename = abc.abstractproperty(get_filename, set_filename)
    # filename used to specify the name of the output file
    # filename should be a string

    @abc.abstractmethod
    def get_file(self):
        return
    @abc.abstractmethod
    def set_file(self, _file):
        """
        Class variables: file
        Local variables: _file
        """
        if not hasattr(_file, "read"):
            raise TypeError
        else:
            self.file = _file
        return
    file = abc.abstractproperty(get_file, set_file)
    # file used to contain an open file
    # file should be an open file

    @abc.abstractmethod
    def get_csv_writer(self):
        return
    @abc.abstractmethod
    def set_csv_writer(self, _csv_writer):
        """
        Class variables: csv_writer
        Local variables: _csv_writer
        """
        if not hasattr(_csv_writer, "writerows"):
            raise TypeError
        else:
            self.csv_writer = _csv_writer
        return
    csv_writer = abc.abstractproperty(get_csv_writer, set_csv_writer)
    # csv_writer used to contain a writer object
    # csv_writer should be a Writer Object

    @abc.abstractmethod
    def get_environment(self):
        return
    @abc.abstractmethod
    def set_environment(self, _environment):
        """
        Class variables: environment
        Local variables: _environment
        """
        if not hasattr(_environment, '__class__'):
            raise TypeError
        else:
            self.environment = _environment
        return
    environment = abc.abstractproperty(get_environment, set_environment)
    # environment used to keep reference to the environment
    # environment should be a class

    @abc.abstractmethod
    def get_runner(self):
        return
    @abc.abstractmethod
    def set_runner(self, _runner):
        """
        Class variables: runner
        Local variables: _runner
        """
        if not hasattr(_runner, '__class__'):
            raise TypeError
        else:
            self.runner = _runner
        return
    runner = abc.abstractproperty(get_runner, set_runner)
    # runner used to keep reference to the runner
    # runner should be a class

    # -------------------------------------------------------------------------
    # __init__(self, environment, runner)
    # Initialises the Measurements object and reads the config
    # -------------------------------------------------------------------------
    @abc.abstractmethod
    def __init__(self, environment, runner):
        # log that we've started measuring stuff
        logging.info("  measurement started...")
        # We move the variables to class variables
        # so that they are visible to other methods easily
        self.read_xml_config_file(environment.measurement_config)
        self.environment = environment
        self.runner = runner

    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # open_file(self)
    # Opens the file and writes the headers
    # -------------------------------------------------------------------------
    @abc.abstractmethod
    def open_file(self):
        # Import the library for csv handling
        import csv
        # Open the file for writing
        # If there are multiple simulations we add a unique identifier
        if self.environment.num_simulations > 1:
            # And split the name into two parts, before .csv and .csv if it exists
            # Then add a unique identifier in the middle
            # (assuming the script does not run faster than a milisecond)
            import datetime
            import time
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H_%M_%S_%f')
            self.filename = self.filename.split(".csv")[0] + timestamp + ".csv"
            # SWITCH: uncomment the below 2 line, and comment the 4 above
            # to switch from unique names based on unix timestamp to uuid4
            # import uuid
            # self.filename = self.filename.split(".csv")[0] + str(uuid.uuid4()) + ".csv"
        self.file = open(self.filename, 'w')
        # Create an object for writing within the file
        # The file will be delimited with \n (not particularly relevant:)
        # That should be simple enough to change in vim in output if needed
        self.csv_writer = csv.writer(self.file, lineterminator='\n')
        # We write the headers first
        headers = []
        # We go through all things in the config
        # But not in the order within the config itself
        # But by the column number, or linearly with respect to output not input
        for i in range(0, len(self.config)):
            # We append the headers with the appropriate value from config
            headers.append(self.config[i+1][0])
        # And finally we write the headers to the file
        self.csv_writer.writerow(headers)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # write_to_file(self)
    # Writes a row of values for to store the state of the system
    # at the time of calling this method
    # -------------------------------------------------------------------------
    @abc.abstractmethod
    def write_to_file(self):
        # We create an empty row
        out_row = []
        # And go through the config, again in the order of output columns
        for i in range(0, len(self.config)):
            # If the value we want is static (a value to read)
            if self.config[i+1][1] == "static":
                # We append the row with the appropriate value
                out_row.append(eval(self.config[i+1][2]))
            # If the value we want is dynamic (a method to call)
            elif self.config[i+1][1] == "dynamic":
                # We append the row with the appropriate value
                out_row.append(eval(self.config[i+1][2])(*self.config[i+1][3]))
            # If the config states something else, raise an error
            else:
                raise LookupError("Measurement outputs should be static or dynamic.")
        # Finally we write the line to the output file
        self.csv_writer.writerow(out_row)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # close_file(self, filename)
    # Closes the file so we don't have issues with the disk and the file
    # -------------------------------------------------------------------------
    @abc.abstractmethod
    def close_file(self):
        # And we close the file just in case
        self.file.close()
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # read_xml_config_file(self, config_file_name)
    # Read the xml config file specifying the config file
    # which is a list of lists
    # For static input, that is a variable gotten from somewhere we need
    # -The number of the output column
    # -Header used for this column
    # -Designation that it is static, i.e. a string "static"
    # -The full variable name as string, e.g. "self.environment.household[0].identifier"
    # For dynamic input, that is a variable gotten from a method we need
    # -The number of the output column
    # -Header used for this column
    # -Designation that it is dynamic, i.e. a string "dynamic"
    # -The full method name as string, e.g. "self.environment.household[0].identifier"
    # NOTE: Both variable and method string above must be reachable from Measurement class
    # NOTE: That is why we have access to environment and runner (mostly for updater and step)
    # -A list of arguments for the above method
    # Thus:
    # {column_number: [header,static/dynamic, variable / method, list_of_arguments],...:[...]]
    # [int: [string, string, string / method, list],...:[...]]
    #
    # Now we pass this on to the Measurement class through an xml file
    # which should look like this
    #
    # <measurement identifier='test_output'>
    #     <parameter type='filename' value='TestMeasurement.csv'></parameter>
    #     <parameter type='static' column='1' header='Step' value='self.runner.current_step'></parameter>
    #     <parameter type='dynamic' column='2' header='Deposits' method='self.environment.households[0].get_account' arguments='["deposits"]'></parameter>
    # </measurement>
    #
    # -------------------------------------------------------------------------
    @abc.abstractmethod
    def read_xml_config_file(self, config_file_name):
        from xml.etree import ElementTree
        xmlText = open(config_file_name).read()
        element = ElementTree.XML(xmlText)
        self.identifier = element.attrib['identifier']

        # loop over all entries in the xml file
        for subelement in element:
            if subelement.attrib['type'] == 'filename':
                value = str(subelement.attrib['value'])
                self.filename = value

            if subelement.attrib['type'] == 'static':
                self.config[int(subelement.attrib['column'])] = [str(subelement.attrib['header']), 'static', str(subelement.attrib['value'])]

            if subelement.attrib['type'] == 'dynamic':
                self.config[int(subelement.attrib['column'])] = [str(subelement.attrib['header']), 'dynamic', str(subelement.attrib['method']), eval(str(subelement.attrib['arguments']))]
        logging.info("  measurement config file have been read")
    # -------------------------------------------------------------------------
