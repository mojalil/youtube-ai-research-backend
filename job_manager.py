from dataclasses import dataclass
from threading import Lock
from typing import Dict, List
from datetime import datetime

# define classes

@dataclass
class Event:
    timestamp: datetime
    data: str

@dataclass
class Job:
    status: str
    events: List[Event]
    result: str

jobs_lock = Lock()
jobs = Dict[str, 'Job'] = {}

# function to append an event to the event queue
def appent_event(job_id: str, event_data: str):
    with jobs_lock:
        if job_id not in jobs:
            jobs[job_id] = Job(
                status='STARTED',
                events=[],
                result=''
            )
        else:
            print(f'Appending event to job {job_id}')
            jobs[job_id].events.append(Event(
                timestamp=datetime.now(),
                data=event_data
            ))

            