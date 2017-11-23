import json
import sys
import logging
import time
import threading
import ConfigParser
import os
import Queue
import datetime
from time import gmtime, strftime
from uptime import boottime
from threading import Lock

from liota.dccs.dcc import DataCenterComponent, RegistrationFailure
from liota.entities.metrics.metric import Metric
from liota.lib.utilities.utility import LiotaConfigPath, getUTCmillis, mkdir, read_liota_config
from liota.lib.utilities.si_unit import parse_unit
from liota.entities.metrics.registered_metric import RegisteredMetric
from liota.entities.registered_entity import RegisteredEntity
import logging
from liota.edge_component.rule_edge_component import RuleEdgeComponent

class Rule_Generator:

    def check_and_make_changes(self):
        log = logging.getLogger(__name__)
        config = ConfigParser.RawConfigParser()
        fullPath = LiotaConfigPath().get_path_gateway_devices_status_config()
        if fullPath != '':
            try:
                if config.read(fullPath) != []:
                    try:
                        # retrieve device info file storage directory
                        file_path1 = config.get('m1', 'interedge1')
                        file_path2 = config.get('m2', 'interedge2')
                        log.debug("_get_{0} file_path1:{1} file_path2:{2}".format('interedge', file_path1,file_path2))
                    except ConfigParser.ParsingError as err:
                        log.error('Could not open config file ' + err)
                        return None
                    if not os.path.exists(file_path1):
                        try:
                            os.makedirs(file_path1)
                        except OSError as exc:  # Python >2.5
                            if exc.errno == errno.EEXIST and os.path.isdir(file_path1):
                                pass
                            else:
                                log.error('Could not create file storage directory')
                                return None
                    if file_path1 == '' && file_path2 == '' :
                        config.set("DEFAULT","m2", "true")
                    return file_path1
                else:
                    log.error('Could not open config file ' + fullPath)
                    return None
            except IOError, err:
                log.error('Could not open config file')
                return None
        else:
            # missing config file
            log.warn('liota.conf file missing')
            return None

    def get_first_gateway_devices_status
        return True

    def get_second_gateway_devices_status
        return True


