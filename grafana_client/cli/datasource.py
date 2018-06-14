from grafana_client.utils import command


class DatasourceCreate(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(DatasourceCreate, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


class DatasourceShow(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(DatasourceShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


class DatasourceList(command.Lister):
    def get_parser(self, prog_name):
        parser = super(DatasourceList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class DatasourceDelete(command.Command):
    def get_parser(self, prog_name):
        parser = super(DatasourceDelete, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

