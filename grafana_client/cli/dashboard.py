from grafana_client import cli

class DashboardCreate(cli.Command):
    def get_parser(self, prog_name):
        parser = super(DashboardShow, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DashboardUpdate(cli.Command):
    def get_parser(self, prog_name):
        parser = super(DashboardShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Update resource by name')
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Update body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DashboardShow(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(DashboardList, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DashboardList(cli.Lister):
    def get_parser(self, prog_name):
        parser = super(DashboardList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DashboardDelete(cli.Command):
    def get_parser(self, prog_name):
        parser = super(DashboardShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

