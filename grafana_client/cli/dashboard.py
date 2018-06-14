from grafana_client.utils import command


class DashboardCreate(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(DashboardCreate, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


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

