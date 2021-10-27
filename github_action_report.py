#!/usr/bin/env python3.9

from github import Github
import os
import datetime

g = Github(os.environ.get('TF_VAR_github_token'))

repos = g.get_organization('fifthsun').get_repos()

start_date = datetime.datetime.now() - datetime.timedelta(30)

for repo in repos:
    total_time = 0
    runs = 0
    for run in repo.get_workflow_runs():
        if run.status == 'completed':
            if run.created_at > start_date:
                try:
                    runs += 1
                    total_time += run.timing().run_duration_ms/1000.0
                except:
                    pass
            else:
                break

        if runs > 0:
            print(repo.name, runs, total_time, total_time / runs)
