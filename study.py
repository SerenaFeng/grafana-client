from jinja2 import  Environment, PackageLoader
import json
import ast


env = Environment(loader=PackageLoader('grafana_client'))
env.filters['jsonify'] = json.dumps

db = {
    'uid': 'test',
    'title': 'test',
    'tags':['yaml', 'test']
}

template = env.get_template('dashboard.json.j2')
dashstr = template.render(conf=db)
print type(dashstr), dashstr
dashast = ast.literal_eval(dashstr)
print type(dashast), dashast

dashjson = json.loads((dashstr))
print type(dashjson), dashjson

# print dash.get('uid')
