import yaml

from grafana_client.j2man.render import Render
from grafana_client.utils import command
from grafana_client.yamlman import builder

DB_URL = 'api/dashboards/db'


class DashboardCreate(command.Command):
    def get_parser(self, prog_name):
       parser = super(DashboardCreate, self).get_parser(prog_name)
       parser.add_argument('-p', '--path',
                           help='dashboard config path')
       return parser

    def take_action(self, parsed_args):
        dbs = []
        if parsed_args.path:
            dbs = builder.Builder().build(parsed_args.path)
        dbjsons = [Render().render(db) for db in dbs]
        for dbjson in dbjsons:
            self.log.debug('Begin to create dashboard: \n {}'.format(
                yaml.dump(dbjson)))
            self._create(dbjson)

    def _create(self, dbjson):
        try:
            self.app.rest_manager.post(DB_URL, dbjson)
        except Exception as err:
            self.log.warning('Dashboard [{}] create failed, Reason: {}'.format(
                dbjson.get('dashboard').get('title'),
                err
            ))


class DashboardShow(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(DashboardShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


class DashboardList(command.Lister):
    def get_parser(self, prog_name):
        parser = super(DashboardList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class DashboardDelete(command.Command):
    def get_parser(self, prog_name):
        parser = super(DashboardDelete, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

