from setuptools import setup

__version__ = '0.0.0'

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='squirrels nut counter',
    version=__version__,
    package_dir={'': 'src/squirrels-nut-counter'},
    install_requires=required,
    extras_require={
        'test': [
            'pytest',
            'pytest-mock',
        ],
        'dev': [
            'pytest',
            'pytest-mock',
            'dagger.io',
            'pre-commit',
        ],
    },
)
