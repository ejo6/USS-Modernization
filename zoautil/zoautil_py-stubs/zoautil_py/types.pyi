from typing import Optional

class DatasetDefinition:
    def __init__(
        self,
        dataset_name: str,
        disposition: str = ...,
        type: Optional[str] = ...,
        primary_space: Optional[int] = ...,
        secondary_space: Optional[int] = ...,
        block_size: Optional[int] = ...,
        record_format: Optional[str] = ...,
        record_length: Optional[int] = ...,
        directory_blocks: Optional[int] = ...,
        volumes: Optional[str] = ...,
    ) -> None: ...

class FileDefinition:
    def __init__(
        self,
        path_name: str,
        disposition: str = ...,
        file_type: Optional[str] = ...,
    ) -> None: ...

class DDStatement:
    def __init__(
        self,
        name: str,
        definition: DatasetDefinition | FileDefinition,
    ) -> None: ...

class Job:
    job_id: str
    name: str
    owner: str
    status: str
    return_code: Optional[str]
    cpu_time: Optional[int]

    def refresh(self) -> None: ...
