from typing import List, Tuple, Union
import subprocess
from pathlib import Path
import re
import logging


def run(command: Union[str, List[str]], **kwargs) -> str:
    """Run a command and return standard out, throwing an exception on failures."""
    if isinstance(command, list):
        args = command
    elif isinstance(command, str):
        args = command.split()
    else:
        raise RuntimeError(f"run command is invalid: {command}")

    logging.info(f"Running {args}")
    return (
        subprocess.run(args, stdout=subprocess.PIPE, **{**dict(check=True), **kwargs})
        .stdout.decode()
        .strip()
    )


def get_repository_root():
    """Get the repository that the command is currently in."""
    return Path(run("git rev-parse --show-toplevel"))
