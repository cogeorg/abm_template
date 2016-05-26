#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Sample implementation of the abm_template
The description of the model implemented
is presented in the README.md file
This script needs to be ran with the
runner config file as parameter.

Author: Pawel Fiedor (pawel@fiedor.eu)
        Co-Pierre Georg (cogeorg@gmail.com)

Date of last update: 20-11-2015 (Cape Town)

"""
if __name__ == '__main__':
    import sys
    from samples.sample_config import Config
    from samples.sample_runner import Runner

    args = sys.argv

    if len(args) != 2:
        print "Usage: ./sample runner_config_file_path.xml"
        sys.exit()

    config = Config()
    config.read_xml_config_file(str(args[1]))
    runner = Runner(config)
    runner.do_run()
