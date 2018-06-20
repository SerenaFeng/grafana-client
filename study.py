from jinja2 import  Environment, PackageLoader
import json
import ast


env = Environment(loader=PackageLoader('grafana_client',
                                       package_path='j2man/templates'))
env.filters['jsonify'] = json.dumps

render = [{"type": "timeserie", "target": "upper_25"},
          {"type": "timeserie", "target": "upper_50"}]

template = env.get_template('helper.j2')
content = template.render(conf=render)
print type(content), content
dict_content = ast.literal_eval(content)
print type(dict_content), dict_content

