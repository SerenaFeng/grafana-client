import io
import logging
import os

from six.moves import StringIO
from six.moves import configparser

LOG = logging.getLogger(__name__)
DEFAULT_CONF = """
[grafana]
url = http://localhost:3000
authorization = 
"""


def get_config_file(options):
    # Initialize with the global fallback location for the config.
    conf = '/etc/grafana_client/grafana_client.ini'
    if options.conf:
        conf = options.conf
    else:
        # Allow a script directory config to override.
        localconf = os.path.join(os.path.dirname(__file__),
                                 'grafana_client.ini')
        if os.path.isfile(localconf):
            conf = localconf
        # Allow a user directory config to override.
        userconf = os.path.join(os.path.expanduser('~'), '.config',
                                'grafana_client', 'grafana_client.ini')
        if os.path.isfile(userconf):
            conf = userconf
    return conf


def setup_config_settings(options):

    conf = get_config_file(options)
    config = configparser.ConfigParser()
    # Load default config always
    config.readfp(StringIO(DEFAULT_CONF))
    if os.path.isfile(conf):
        options.conf = conf  # remember file we read from
        LOG.debug("Reading config from {0}".format(conf))
        conffp = io.open(conf, 'r', encoding='utf-8')
        config.readfp(conffp)
    # else:
    #     raise Exception(
    #         "A valid configuration file is required"
    #         "\n{0} is not a valid .ini file".format(conf))

    return config

