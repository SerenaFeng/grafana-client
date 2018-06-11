from grafana_client import cli

class DatasourceCreate(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(DatasourceCreate, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DatasourceUpdate(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(DatasourceUpdate, self).get_parser(prog_name)
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

class DatasourceShow(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(DatasourceShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DatasourceList(cli.Lister):
    def get_parser(self, prog_name):
        parser = super(DatasourceList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class DatasourceDelete(cli.Command):
    def get_parser(self, prog_name):
        parser = super(DatasourceDelete, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

