# coding=utf-8

"""
Author： jinshuai_qiao
Date： 2019/10/21
Desc：
"""
import datetime

from github import Github

gg = Github('q356970306@163.com', 'q58106513').get_user()

print(gg)

for repo in gg.get_repos():

    repo = gg.get_repo(repo.name)
    commits = repo.get_commits(
        sha='master',
        since=datetime.datetime.now() -
        datetime.timedelta(
            days=37),
        until=datetime.datetime.now())
    for cm in commits:
        print(repo.name, cm.commit.author, cm.commit.message)
