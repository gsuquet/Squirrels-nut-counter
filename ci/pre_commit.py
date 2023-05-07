import sys

import anyio
import base
import dagger


async def run_pre_commit():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        python = (
            base.python_base(client, '3.11')
            .with_exec(['apk', 'add', 'git', 'libgcc'])
            .with_exec(['git', 'config', '--global', 'safe.directory', '*'])
            .with_exec(['git', 'add', '.pre-commit-config.yaml'])
            .with_exec(['pip', 'install', 'pre-commit'])
            .with_exec(['pre-commit', 'run', '--all-files'])
        )

        # execute
        await python.exit_code()

    print('Pre-commit passed')


def add_pre_commit_step(precedent_container: dagger.Container) -> dagger.Container:
    """Function add_pre_commit_step : adds a step to run pre-commit

    Parameters
    ----------
    precedent_container : Container
        The container to add the step to

    Returns
    -------
    Container
        Returns a container with the step to run pre-commit
    """
    pre_commit_step = (
        precedent_container.with_exec(['apk', 'add', 'git', 'libgcc'])
        .with_exec(['git', 'config', '--global', 'safe.directory', '*'])
        .with_exec(['git', 'add', '.pre-commit-config.yaml'])
        .with_exec(['pip', 'install', 'pre-commit'])
        .with_exec(['pre-commit', 'run', '--all-files'])
    )
    return pre_commit_step


if __name__ == '__main__':
    anyio.run(run_pre_commit)
