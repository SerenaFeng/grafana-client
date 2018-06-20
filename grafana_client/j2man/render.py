import ast
import json
import logging

from jinja2 import Environment, TemplateNotFound
from jinja2 import PackageLoader

LOG = logging.getLogger(__file__)

class Render(object):
    def __init__(self):
        self.env = Environment(loader=PackageLoader('grafana_client',
                                                    package_path='j2man/templates'))
        self.env.filters['jsonify'] = json.dumps

    def render(self, db):
        LOG.debug('begin to render dashboard: {}'.format(json.dumps(db)))
        dashjson = self._render('dashboard.json.j2', db)
        if 'rows' in db:
            dashjson['dashboard']['rows'] = list()
            for row in db.get('rows'):
                dashjson['dashboard']['rows'].append(self._render_row(row))
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
        LOG.debug('begin to render panel: {}'.format(json.dumps(panel)))

        tfile = '{}.json.j2'.format(panel.get('type'))
        return self._render(tfile, panel)

    def _render(self, j2, data):
        try:
            template = self.env.get_template(j2)
        except TemplateNotFound:
            raise Exception('Unsupported template {}'.format(j2))
        except Exception as err:
            raise Exception('load template {} failed with {}'.format(j2, err))

        return ast.literal_eval(template.render(conf=data))

