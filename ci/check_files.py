import pre_commit
import tests
import base

import anyio
import sys
import dagger


async def check_files():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        pipeline = tests.add_all_tests_step(
            pre_commit.add_pre_commit_step(
                base.python_base(client, '3.11'),
            ),
        )

        # execute
        await pipeline.exit_code()


if __name__ == '__main__':
    anyio.run(check_files)
