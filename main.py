from job_scanner import scan_jobs, save_jobs, load_jobs
from bot_notifier import send_notification
from config import JOB_SEARCH_PARAMS

def main():
    old_jobs = load_jobs()
    old_job_links = {job['link'] for job in old_jobs}
    
    new_jobs = scan_jobs(JOB_SEARCH_PARAMS)
    new_job_links = {job['link'] for job in new_jobs}

    fresh_jobs = [job for job in new_jobs if job['link'] not in old_job_links]

    for job in fresh_jobs:
        send_notification(job)

    if fresh_jobs:
        save_jobs(new_jobs)

if __name__ == "__main__":
    main()