import os
from app import create_app

# Get config name from environment variable, default to 'development'
config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()