# ! NOT RELATED TO THE GUIDE, ITS FOR THE WORKFLOW ! #
#
#
#
#
#
#
#
#
#
#

import datetime
import os
from git import Repo

repo_path = os.getcwd()

repo = Repo(repo_path)
commit = repo.head.commit
commit_message = commit.message.strip()
commit_date = commit.committed_datetime.strftime("%d-%b-%Y")
updates_file_path = os.path.join(repo_path, 'updates.md')
update_entry = f"| {commit_date} | {commit_message} |\n"
with open(updates_file_path, 'a') as f:
    f.write(update_entry)
print("Update logged successfully!")
