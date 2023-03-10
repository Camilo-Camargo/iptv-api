from ariadne import make_executable_schema
from ariadne.asgi import GraphQL

from schema import types, type_defs
from resolver import resolvers


schema = make_executable_schema(types, resolvers)
app = GraphQL(schema, debug=True)
