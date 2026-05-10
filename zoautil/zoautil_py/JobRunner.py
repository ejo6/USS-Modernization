from zoautil_py import jobs
from typing import Dict
import time


class JobRunner:
    """ Runs to be imported and abstract the process of running z/OS jobs (1..*)

    Attributes:
    """

    def __init__(self, dataset_path: str, poll_interval: int=1):
        self.dataset_path = dataset_path
        self.results: Dict[str, str] = {} 
        self.outputs: Dict[str, Dict[str:str]] = {} # {stepname:{ddname:output}}
        self.POLL_INTERVAL = poll_interval


    def submit(self):
        job = jobs.submit(self.dataset_path)
        while job.status not in ("OUTPUT", "ABEND", "CC"):
            time.sleep(self.POLL_INTERVAL)
            job.refresh()
        
        # Populate results
        self.results = {
            "name": job.name,
            "status": job.status,
            "rc": job.return_code or "",
            "cpu_time": job.cpu_time or 0,
        }

        # Populate outputs
        for dd in jobs.list_dds(job.job_id):
            step = dd["step_name"]
            ddname = dd["dd_name"]
            if step not in self.outputs:
                self.outputs[step] = {}
            self.outputs[step][ddname] = jobs.read_output(job.job_id, step_name=step)

# -- Testing --
jobRunner = JobRunner("Z55033.JCL(ADDAMT)")
jobRunner.submit()
print(f"Outputs: {jobRunner.outputs}\n Results: {jobRunner.results}")