
import sys

from cliff import app
from cliff import commandmanager

from grafana_client.utils import rest


class GrafanaclientShell(app.App):

    def __init__(self):
        super(GrafanaclientShell, self).__init__(
            description='grafana-client cli',
            version='0.1',
            command_manager=commandmanager.CommandManager('grafana_client'),
            deferred_help=True,
        )

    def build_option_parser(self, description, version, argparse_kwargs=None):
        self.LOG.debug('build_option_parser')
        parser = super(GrafanaclientShell, self).build_option_parser(
            description,
            version,
            argparse_kwargs)
#        parser.add_argument('-u',
#                            type=str,
#                            help='Username for authentication')
#        parser.add_argument('-p',
#                            type=str,
#                            help='Password for authentication')
        return parser

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')
        self.rest_manager = rest.RestManager(self.options)
        

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myshell = GrafanaclientShell()
    return myshell.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))