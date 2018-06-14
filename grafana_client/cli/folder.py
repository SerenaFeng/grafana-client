from grafana_client.utils import command


class FolderCreate(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(FolderCreate, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


class FolderShow(command.ShowOne):
    def get_parser(self, prog_name):
        parser = super(FolderShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        return self.format_output({})


class FolderList(command.Lister):
    def get_parser(self, prog_name):
        parser = super(FolderList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)


class FolderDelete(command.Command):
    def get_parser(self, prog_name):
        parser = super(FolderDelete, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

