import uvicorn
from uvicorn import Config

from core import create_app
from core.configs import app as APP, log as LOG
from core.utils import env

app = create_app()

if __name__ == '__main__':
    config = Config(
        'main:app',
        host=env('APP_HOST', '0.0.0.0'),
        port=int(env('APP_PORT', 5000)),
        reload=True,
        reload_dirs=[str(APP.PROJECT_PATH / 'core')],
        debug=True,
        log_level='debug',
        log_config=LOG.LOGGING_CONFIG,
    )
    uvicorn.run(
        config.app,
        host=config.host,
        port=config.port,
        reload=config.reload,
        reload_dirs=config.reload_dirs,
        debug=config.debug,
        log_level=config.log_level,
        log_config=config.log_config,
    )
