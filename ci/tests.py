import sys

import anyio
import base
import dagger


async def run_all_tests():
    """Function run_tests : runs all the automated tests"""
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        python = (
            base.python_base(client, '3.11')
            .with_exec(['pip', 'install', '-e', '.[test]'])
            .with_exec(['pytest', 'tests'])
        )

        # execute
        await python.exit_code()

    print('Tests succeeded!')


def add_all_tests_step(precedent_container: dagger.Container) -> dagger.Container:
    """Function add_all_tests_step : adds a step to run all the automated tests

    Parameters
    ----------
    precedent_container : Container
        The container to add the step to

    Returns
    -------
    Container
        Returns a container with the step to run all the automated tests
    """
    tests_step = precedent_container.with_exec(
        ['pip', 'install', '-e', '.[test]'],
    ).with_exec(['pytest', 'tests'])
    return tests_step


if __name__ == '__main__':
    anyio.run(run_all_tests)
