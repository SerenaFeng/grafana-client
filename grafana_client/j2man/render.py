import ast
import json
import logging

from jinja2 import Environment
from jinja2 import PackageLoader

LOG = logging.getLogger(__file__)

class Render(object):
    def __init__(self):
        self.env = Environment(loader=PackageLoader('grafana_client',
                                                    package_path='j2man/templates'))
        self.env.filters['jsonify'] = json.dumps

    def render(self, db):
        LOG.debug('begin to render dashboard: {}'.format(db))
        dashjson = self._render('dashboard.json.j2', db)
        if 'rows' in db:
            dashjson['rows'] = list()
            for row in db.get('rows'):
                dashjson['rows'].append(self._render_row(row))
        return dashjson

    def _render_row(self, row):
        LOG.debug('begin to render row: {}'.format(row))

        rowjson = self._render('row.json.j2', row)
        if 'panels' in row:
            rowjson['panels'] = list()
            for panel in row.get('panels'):
                rowjson['panels'].append(self._render_panel(panel))
        return rowjson

    def _render_panel(self, panel):
        LOG.debug('begin to render panel: {}'.format(panel))

        if panel.get('type') == 'text':
            return self._render('text.json.j2', panel)
        else:
            raise Exception("Not Support Panel Type [{}]".format(
                panel.get('type')))

    def _render(self, j2, data):
        template = self.env.get_template(j2)
        return ast.literal_eval(template.render(conf=data))