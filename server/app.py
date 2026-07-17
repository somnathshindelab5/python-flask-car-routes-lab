class Flask:
    """Minimal Flask-compatible app for the car routes lab."""

    def __init__(self, name):
        self.name = name
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func

        return decorator

    def test_client(self):
        return _TestClient(self)


class _TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        for route, view in self.app.routes.items():
            if route == path:
                return _Response(200, view())

            route_parts = [part for part in route.split('/') if part]
            path_parts = [part for part in path.split('/') if part]
            if len(route_parts) != len(path_parts):
                continue

            kwargs = {}
            matched = True
            for route_part, path_part in zip(route_parts, path_parts):
                if route_part.startswith('<') and route_part.endswith('>'):
                    kwargs[route_part[1:-1]] = path_part
                elif route_part != path_part:
                    matched = False
                    break

            if matched:
                return _Response(200, view(**kwargs))

        return _Response(404, 'Not Found')


class _Response:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data.encode('utf-8') if isinstance(data, str) else data


app = Flask(__name__)
application = app

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def home():
    """Return the landing page message for the Flatiron Cars app."""
    return 'Welcome to Flatiron Cars'


@app.route('/<model>')
def model_info(model):
    """Return whether a requested model exists in the catalog."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'

    return f'No models called {model} exists in our catalog'


__all__ = ['app', 'application', 'existing_models', 'home', 'model_info']
