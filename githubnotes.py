Git
Definition:
Git is a local version control system that runs on your computer.
It helps you track changes, create versions (commits), and manage branches offline.

Key Point:
Git does not need the internet unless you want to sync with a remote server.


 GitHub
Definition:
GitHub is an online cloud platform where you can store Git repositories and share them with others.

Key Point:
GitHub requires the internet to upload (push) or download (pull) code.

Example:

After working locally, you upload your project to GitHub:



Example: Create and Commit a New Project
Scenario:
You are starting a new project called weather-app. You want to use Git to track its changes.

Step 1: Create the Project Folder

mkdir weather-app        # Create a new folder
cd weather-app           # Move into the folder
Step 2: Initialize Git

git init                 # Initialize an empty git repository
This creates a hidden .git folder that will store all version history.

Step 3: Configure Your Name & Email (One-Time Setup)

git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
These details will appear in your commit history.

Step 4: Add a File
Create a new file (for example, app.py):


echo "print('Hello Weather!')" > app.py
Check the status:

git status
You’ll see app.py listed as Untracked (not yet staged).

Step 5: Stage the File

git add app.py
Now, app.py is in the staging area, ready to be committed.

Step 6: Commit the File

git commit -m "Initial commit: Added app.py"
This saves a snapshot of app.py in the repository history.

Step 7: Check History

git log --oneline
You’ll see something like:


a1b2c3d Initial commit: Added app.py
Final Flow
The full sequence of commands is:


mkdir weather-app
cd weather-app
git init
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
echo "print('Hello Weather!')" > app.py
git status
git add app.py
git commit -m "Initial commit: Added app.py"
git log --oneline



Steps to Push Code to Remote
1. Create a Remote Repository
Go to GitHub (or GitLab, Bitbucket).

Click New Repository.

DO NOT initialize with README, .gitignore, etc. (since you already have a local repo).

Copy the repository URL (e.g., https://github.com/username/weather-app.git).

2. Add the Remote URL to Your Local Repo

git remote add origin https://github.com/username/weather-app.git
This tells Git that your remote repository is called origin.

3. Rename Your Local Branch (Optional but Recommended)

git branch -M main
This sets your current branch to main (GitHub default).

4. Push Your Code to GitHub

git push -u origin main
-u sets the default remote tracking branch, so future pushes can simply use git push.



mkdir weather-app
cd weather-app
git init
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
echo "print('Hello Weather!')" > app.py
git add app.py
git commit -m "Initial commit: Added app.py"
echo "# Weather App" > README.md
git add README.md
git commit -m "Added README.md"
# Add remote and push
git remote add origin https://github.com/username/weather-app.git
git branch -M main
git push -u origin main




🚀 Pushing & Pulling in Git
1. Pushing Code to Remote
What is git push?
Used to upload local commits to the remote repository.

Generally used after git commit.

Steps to Push Code
Add remote repository:


git remote add origin <repo_url>
Rename the default branch (if needed):


git branch -M main
Push code for the first time:


git push -u origin main
After the first push, you can just use:


git push
Example:

# Start with local repo
git init
git add .
git commit -m "Initial commit"

# Link and push
git remote add origin https://github.com/user/weather-app.git
git branch -M main
git push -u origin main
2. Pulling Code from Remote
What is git pull?
git pull is used to download new commits from the remote repository and merge them into your current branch.

Steps to Pull Changes

git pull origin main
origin – name of the remote repository.

main – branch from which changes will be pulled.

Example:
Scenario:
You cloned weather-app earlier, but your teammate pushed new updates.
To update your local repo:


git pull origin main
Now your local repository will have the latest files (e.g., forecast.py added by your teammate).

Shortcut:
If you are already on the branch and have origin set:

git pull
3. Push vs Pull (Quick Comparison)
Command	Purpose
git push	Uploads your local commits to remote
git pull	Fetches and merges remote commits to local

4. Common Workflow

# Make sure your local repo is up to date
git pull origin main

# Add and commit your new changes
git add .
git commit -m "Your changes"

# Push to remote
git push origin main



Before staging means the file is modified in your working directory but not yet added to the staging area using git add.

Example:
You edit file.txt.

The change is untracked by Git for commit (not yet staged).

If you run:


git diff
you will see your changes.

To discard these changes (go back to the last commit version):


git restore file.txt
# OR (older way)
git checkout file.txt


Undo staged changes

git restore --staged filename
Removes the file from the staging area but keeps the changes in the working directory.


View changes in the staged area

git diff --cached


The git diff <commit1> <commit2> command shows the differences (changes) between two commits in your Git history.

Example Scenario
Suppose you have the following commit history (from git log --oneline):


a1b2c3d (HEAD -> main)  Added new feature
e4f5g6h                Fixed bug in script
i7j8k9l                Initial commit
Now you want to compare the changes between the "Initial commit" (i7j8k9l) and "Fixed bug in script" (e4f5g6h).

You can run:


git diff i7j8k9l e4f5g6h
Git will show you the changes made between these two commits — i.e., all modifications from i7j8k9l up to e4f5g6h.



What is git revert HEAD?
git revert HEAD creates a new commit that undoes the changes made in the latest commit (HEAD).

It does not delete history; instead, it adds a new commit to "reverse" the changes.

Example Scenario
1. Commit History
Imagine your repository has the following commits:


a1b2c3d (HEAD -> main)   Added wrong text in file.txt
e4f5g6h                  Fixed bug in script
i7j8k9l                  Initial commit
Here, HEAD points to the latest commit (a1b2c3d).

2. Run git revert HEAD

git revert HEAD
Git will create a new commit that undoes the changes introduced by a1b2c3d.

The history will now look like this:


x9y8z7w (HEAD -> main)  Revert "Added wrong text in file.txt"
a1b2c3d                 Added wrong text in file.txt
e4f5g6h                 Fixed bug in script
i7j8k9l                 Initial commit
3. Why use git revert instead of git reset?
git revert is safe for shared repositories because it does not delete commit history.

git reset (especially --hard) removes commits, which can cause issues if other people are working on the same branch.

Example with a Specific Commit
To revert a specific commit, use:


git revert <commit_hash>
Example:


git revert e4f5g6h
This will undo changes from e4f5g6h by adding a new "revert" commit.



Imagine Your Project Timeline (Commits)
Think of Git commits as save points in a game.

Your commits are:


i7j8k9l   = Feature A (Initial commit)
e4f5g6h   = Feature B
a1b2c3d   = Feature C (Latest commit)
Currently, you are at Feature C (latest save point):


HEAD -> a1b2c3d (Feature C)
HEAD simply means “where you are now” in the timeline.

What Happens with git reset e4f5g6h?
When you run:


git reset e4f5g6h
Git moves your "current position" (HEAD) back to Feature B (e4f5g6h).

The work from Feature C is not deleted—it’s just moved out of staging and left as uncommitted changes in your working folder.

Visual:


HEAD -> e4f5g6h (Feature B)
(Feature C changes are unstaged but still in your files)
It’s like saying:
“Go back to the previous save point, but don’t lose my work—it’s still on my desk.”

What Happens with git reset --hard e4f5g6h?
When you run:


git reset --hard e4f5g6h
Git moves HEAD back to Feature B.

All work from Feature C is completely erased from both Git and your files.

Visual:


HEAD -> e4f5g6h (Feature B)
(Feature C is gone)



Git Branching and Merging – Quick Guide
What is a Branch in Git?
A branch is like a separate workspace where you can work on a new feature or bug fix without affecting the main project.

The main (or master) branch is your stable project line.

A new branch allows you to try new things safely.

Creating and Switching Branches
Step 1: See all branches

git branch -a
Output:

* main
The * indicates you’re currently on main.

Step 2: Create a new branch
t
git branch sprint1
Now you have:

main
sprint1
Step 3: Switch to the new branch

git checkout sprint1
# OR (new way)
git switch sprint1
You are now on sprint1.
Any new commits will only affect this branch, not main.

Step 4: Verify current branch

git branch
Output:


main
* sprint1
Step 5: Why Use Branches?
Suppose main has a stable version of your app.

You create sprint1 to add a new login feature.

If something breaks in sprint1, main stays safe and unaffected.

Merging Branches
1. Switch to main

git switch main
Merging always happens into the branch you are on.

2. Update main

git pull origin main
Ensures your local main is up-to-date with GitHub.

3. Merge your branch

git merge sprint1
Applies all commits from sprint1 into main.

If there are no conflicts, the merge happens automatically.

4. Push updated main to remote

git push origin main
This updates main on GitHub with the merged changes.

Quick Summary
Create a branch:


git switch -c sprint1
Merge into main:


git switch main
git merge sprint1
git push origin main



