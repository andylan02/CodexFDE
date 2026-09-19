"""Normalize Git-related environment variables before any subprocesses are spawned.

Some execution environments inject partial `GIT_CONFIG_*` variables without a
matching key/value pair set. Git treats that as malformed command-line config and
refuses every repo operation (`fatal: unable to parse command-line config`).
Strip the entire Git config override block so Git falls back to the normal
user/global/local config chain instead of crashing.
"""

from __future__ import annotations

import os

for key in list(os.environ):
    if key.startswith("GIT_CONFIG"):
        os.environ.pop(key, None)
