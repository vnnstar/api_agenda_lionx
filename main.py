# Api Agenda Lionx
from src.routers.schedule.signature import RoutesSignature
from docs.api_specifications import DocsSpecifications

# Third party
from flask import Flask

app = Flask(__name__)

routes = RoutesSignature()
routes.init_routes(app)

specs = DocsSpecifications()
specs.init_spec(app)

if __name__ == "__main__":
    app.run(debug=True)
