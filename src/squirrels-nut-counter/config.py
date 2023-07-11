from typing import Any

from pydantic import BaseSettings, PostgresDsn, root_validator

from constants import Environment

from setup import __version__ as app_version


class Config(BaseSettings):
    DATABASE_URL: PostgresDsn

    SITE_DOMAIN: str = 'myapp.com'

    ENVIRONMENT: Environment = Environment.PRODUCTION

    SENTRY_DSN: str | None

    CORS_ORIGINS: list[str]
    CORS_ORIGINS_REGEX: str | None
    CORS_HEADERS: list[str]

    APP_VERSION: str = '1'

    @root_validator(skip_on_failure=True)
    def validate_sentry_non_local(cls, data: dict[str, Any]) -> dict[str, Any]:
        if data['ENVIRONMENT'].is_deployed and not data['SENTRY_DSN']:
            raise ValueError('Sentry is not set')

        return data


settings = Config()

app_configs: dict[str, Any] = {
    'title': 'Squirrels Nut Counter',
    'description': 'A simple API to manage your personal finances',
    'version': app_version,
    'license_info': {
        'name': 'MIT',
        'url': 'https://opensource.org/licenses/MIT',
    },
}

if settings.ENVIRONMENT.is_deployed:
    app_configs['root_path'] = f'/v{settings.APP_VERSION}'

if not settings.ENVIRONMENT.is_debug:
    app_configs['openapi_url'] = None  # hide docs
