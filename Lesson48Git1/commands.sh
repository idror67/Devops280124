# Description: Commands to create a new git repository
git init

# To see the status type in git bash:
git status

# To make  file to be tracked by git use:
git add 

# To add file to git repository
git add commands.sh

# To commit the file to the repository
git commit -m "First commit"

# to see the difference between the file and the repository
git diff

# to restore the file to the last commit
git restore commands.sh

# to see the log of the commits
git log
# to see the full log
git log -p
# to see the log of the commits in one line
git log --oneline

# to reset the staging area
git reset