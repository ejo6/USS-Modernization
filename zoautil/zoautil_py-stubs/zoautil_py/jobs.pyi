"""
Stubs for zoautil_py.jobs — IBM Z Open Automation Utilities (ZOAU) 1.3.x
Sources: IBM docs (403'd), GitHub zoau-samples, kalebporter.medium.com/z-os-job-management-with-python
"""

from typing import Dict, List, Optional
from zoautil_py.types import Job

def submit(
    dataset_name: str,
    timeout: int = ...,
) -> Job: ...

def list(
    owner: Optional[str] = ...,
    prefix: Optional[str] = ...,
    job_id: Optional[str] = ...,
) -> List[Dict[str, str]]: ...

def cancel(job_id: str, purge: bool = ...) -> bool: ...

def read_output(job_id: str, step_name: Optional[str] = ...) -> str: ...

def list_dds(job_id: str) -> List[Dict[str, str]]: ...

def listing(filter: str = ...) -> List[Dict[str, str]]: ...
