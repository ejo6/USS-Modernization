"""
Stubs for zoautil_py.mvscmd — IBM Z Open Automation Utilities (ZOAU) 1.3.x
"""

from typing import List, Optional
from zoautil_py.types import DDStatement

class MVSCmdResponse:
    rc: int
    stdout: str
    stderr: str

def execute(
    pgm: str,
    dds: Optional[List[DDStatement]] = ...,
    parms: Optional[str] = ...,
) -> MVSCmdResponse: ...

def execute_authorized(
    pgm: str,
    dds: Optional[List[DDStatement]] = ...,
    parms: Optional[str] = ...,
) -> MVSCmdResponse: ...
