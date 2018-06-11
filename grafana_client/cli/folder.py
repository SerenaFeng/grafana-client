from grafana_client import cli

class FolderCreate(cli.Command):
    def get_parser(self, prog_name):
        parser = super(FolderShow, self).get_parser(prog_name)
#        parser.add_argument('body',
#                            type=json.loads,
#                            help='Create body')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class FolderUpdate(cli.Command):
    def get_parser(self, prog_name):
        parser = super(FolderShow, self).get_parser(prog_name)
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

class FolderShow(cli.Shower):
    def get_parser(self, prog_name):
        parser = super(FolderList, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            help='Show Resource by name')
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class FolderList(cli.Lister):
    def get_parser(self, prog_name):
        parser = super(FolderList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        suites = []
        columns = []
        return self.format_output(columns, suites)

class FolderDelete(cli.Command):
    def get_parser(self, prog_name):
        parser = super(FolderShow, self).get_parser(prog_name)
#        parser.add_argument('name',
#                            type=str,
#                            help='Delete resource by name')
        return parser

    def take_action(self, parsed_args):
        return 'deleted'

