import yaml

from grafana_client.j2man.render import Render
from grafana_client.utils import command
from grafana_client.utils import rest
from grafana_client.yamlman import builder

url = 'http://localhost:3000/api/dashboards/db'

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
        results = filter(self._create, dbjsons)
        return results

    @staticmethod
    def _create(dashboard):
        return rest.RestManager().post(url, dashboard)

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

