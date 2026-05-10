"""
Stubs for zoautil_py.datasets — IBM Z Open Automation Utilities (ZOAU) 1.3.x
Sources: IBM docs (403'd), GitHub zoau-samples, ibm_zos_core Ansible collection
"""

from typing import List, Optional

def create(
    dataset_name: str,
    type: str = ...,
    primary_space: Optional[int] = ...,
    secondary_space: Optional[int] = ...,
    block_size: Optional[int] = ...,
    record_format: Optional[str] = ...,
    record_length: Optional[int] = ...,
    directory_blocks: Optional[int] = ...,
    volumes: Optional[str] = ...,
) -> bool: ...

def delete(dataset_name: str) -> bool: ...

def exists(dataset_name: str) -> bool: ...

def copy(
    source: str,
    target: str,
    replace: bool = ...,
) -> bool: ...

def rename(source: str, target: str) -> bool: ...

def read(dataset_name: str) -> str: ...

def write(
    dataset_name: str,
    data: str,
    append: bool = ...,
) -> bool: ...

def list(
    pattern: str = ...,
    volume: Optional[str] = ...,
) -> List[str]: ...

def list_members(dataset_name: str) -> List[str]: ...

def hlq() -> str: ...

def tmp_name(high_level_qualifier: Optional[str] = ...) -> str: ...
