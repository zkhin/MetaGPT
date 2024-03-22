#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Union

from metagpt.tools.tool_registry import register_tool


@register_tool(tags=["shell"])
async def execute(
    command: Union[List[str], str], cwd: str | Path = None, env: Dict = None, timeout: int = 600
) -> Tuple[str, str]:
    """
    Execute a command asynchronously and return its standard output and standard error.

    Args:
        command (Union[List[str], str]): The command to execute and its arguments. It can be provided either as a list
            of strings or as a single string.
        cwd (str | Path, optional): The current working directory for the command. Defaults to None.
        env (Dict, optional): Environment variables to set for the command. Defaults to None.
        timeout (int, optional): Timeout for the command execution in seconds. Defaults to 600.

    Returns:
        Tuple[str, str]: A tuple containing the standard output and standard error of the executed command, both as
         strings.

    Raises:
        ValueError: If the command times out, this error is raised. The error message contains both standard output and
         standard error of the timed-out process.

    Example:
        >>> # command is a list
        >>> stdout, stderr = await execute(command=["ls", "-l"], cwd="/home/user", env={"PATH": "/usr/bin"})
        >>> print(stdout)
        total 8
        -rw-r--r-- 1 user user    0 Mar 22 10:00 file1.txt
        -rw-r--r-- 1 user user    0 Mar 22 10:00 file2.txt
        ...

        >>> # command is a string of shell script
        >>> stdout, stderr = await execute(command="ls -l", cwd="/home/user", env={"PATH": "/usr/bin"})
        >>> print(stdout)
        total 8
        -rw-r--r-- 1 user user    0 Mar 22 10:00 file1.txt
        -rw-r--r-- 1 user user    0 Mar 22 10:00 file2.txt
        ...
    """
    cwd = str(cwd) if cwd else None
    shell = True if isinstance(command, str) else False
    process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, shell=shell)
    try:
        # Wait for the process to complete, with a timeout
        stdout, stderr = process.communicate(timeout=timeout)
        return stdout.decode("utf-8"), stderr.decode("utf-8")
    except subprocess.TimeoutExpired:
        process.kill()  # Kill the process if it times out
        stdout, stderr = process.communicate()
        raise ValueError(f"{stdout.decode('utf-8')}\n{stderr.decode('utf-8')}")
