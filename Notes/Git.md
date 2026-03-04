# 📘 Git Notes

---

## Table of Contents

- [Basics](#basics)
- [Git Init](#git-init)
- [Git Status](#git-status)
- [Git Commit](#git-commit)
- [Git Log](#git-log)
- [Git Reset](#git-reset)
- [Git Revert](#git-revert)
- [Git Branches](#git-branches)
- [Git Merge](#git-merge)

---

## Basics

### `git init` — Initialize a Repository

Used to initialize a new Git repository in the current directory.

```bash
git init
```

- Creates a hidden `.git` folder in your project directory. This folder contains all the metadata and history Git needs to track your project.
- At this point, you have a **local Git repository** set up.
- The default branch created is typically named **`master`** or **`main`** depending on your Git version/config.

---

### `git status` — Check Repository Status

Shows the current state of the working directory and staging area.

```bash
git status
```

- Tells you whether Git is **aware** of your files or not.
- Shows which files are in the **staging area** (ready to be committed) and which are in the **working directory** (untracked or modified but not staged).
- Useful to always run before and after staging files to confirm what's happening.

---

### `git add` — Stage a File

Moves a file from the working directory to the **staging area**.

```bash
# Stage a specific file
git add filename.txt

# Stage all changed files
git add .
```

- After running `git add`, Git becomes **aware** of the file and captures its current content.
- However, Git is **not yet tracking** the file — it is simply staged and ready for a commit.
- Think of the staging area as a preparation zone before officially saving a snapshot.

---

### `git commit` — Save a Snapshot

Records the staged changes permanently into the repository's history. This is when Git truly **starts tracking** the file.

```bash
git commit -m "Your commit message here"
```

- Each commit is a snapshot of your staged files at that point in time.
- Git assigns a unique **SHA hash** to every commit for identification.
- The commit message should clearly describe what changes were made.
- After committing, the file is now being **tracked** by Git — any future changes will be detected by `git status`.

---

### `git log` — View Commit History

Displays the list of all commits made in the repository.

```bash
git log
```

- Shows details for each commit: the **SHA hash**, **author**, **date**, and **commit message**.
- The most recent commit appears at the top.
- Useful to review history and find specific commits.

```bash
# Compact one-line view
git log --oneline
```

---

## Git Init

### `rm -rf .git` — Remove Local Git Repository

Used to completely delete the Git repository from your project without affecting your actual project files.

```bash
rm -rf .git
```

- Removes the hidden `.git` folder entirely, which contains all Git history, commits, and metadata.
- After this, the directory is no longer a Git repository — `git status` will throw an error.
- Your actual project files remain untouched; only Git tracking is removed.
- Useful when you want to start fresh with a new Git history or accidentally initialized Git in the wrong folder.

---

### `git init --initial-branch` — Set Default Branch Name

Initializes a new Git repository with a custom default branch name instead of the default `master` or `main`.

```bash
git init --initial-branch=main
```

- By default, Git may create a branch named `master`. This flag lets you explicitly set the branch name at init time.
- Commonly used to align with modern conventions where `main` is the preferred default branch name.
- You can set any name you want:

```bash
git init --initial-branch=dev
```

- Alternatively, you can configure the default branch name globally so every new repo uses it automatically:

```bash
git config --global init.defaultBranch main
```

---

## Git Status

### Empty Folders Are Not Tracked

Git does **not track empty folders**. If a directory has no files in it, Git completely ignores it.

- This is because Git tracks **content**, not directories. A folder with no files has no content to snapshot.
- A common workaround is to place a placeholder file inside the empty folder, conventionally named `.gitkeep`:

```bash
touch foldername/.gitkeep
```

- This forces Git to become aware of the folder via the placeholder file.

---

### `git status -v` — Verbose Mode

Displays detailed information about the current state of the repository, including the actual diff of staged changes.

```bash
git status -v
```

- **`-v`** stands for **verbose**.
- In addition to showing which files are staged or untracked, it also shows the **line-by-line diff** of what has changed in staged files.
- Useful when you want a deeper look at exactly what will be committed.

---

### `git status -s` — Shorthand Mode

Displays a compact, minimal summary of the repository status.

```bash
git status -s
```

- **`-s`** stands for **shorthand**.
- Each file is shown on a single line with a two-character status code, for example:
  - `??` — Untracked file
  - `A ` — File added to staging area
  - `M ` — Modified file
- Great for a quick overview when you have many changed files.

---

### `git add .` — Stage All Files

Stages all changed and untracked files from the current directory and all its subdirectories.

```bash
git add .
```

- Moves all **non-empty** files and directories from the working area to the staging area in one go.
- Empty folders are still ignored, as Git does not track them.
- Use with caution — always run `git status` beforehand to make sure you're not accidentally staging unwanted files.

---

### `git rm --cached` — Unstage a File

Removes a file from the staging area and puts it back into the untracked/working area, without deleting the actual file from disk.

```bash
git rm --cached filename.txt

# Unstage multiple files
git rm --cached file1.txt file2.txt

# Unstage everything
git rm --cached -r .
```

- `--cached` means only remove from the **index (staging area)**, not from the filesystem.
- The file still exists in your project folder — Git simply stops being aware of it.
- Useful when you accidentally staged a file you didn't mean to, such as a `.env` or config file.

---

## Git Commit

### `git commit -m` — Create a Commit

Saves a snapshot of all staged files into the repository's history. Once committed, Git officially **starts tracking** the file.

```bash
git commit -m "Your commit message here"
```

- Files are only committed from the **staging area** — whatever was added via `git add`.
- Any creation, modification, or deletion of files happens in the **working (non-staging) area** first, and only moves forward with `git add`.

---

### The Commit Object

Every time you run `git commit`, Git creates a **Commit Object** and stores it in the `.git/objects` folder. Each commit object contains 4 key pieces of information:

- **Who** made the commit (author name and email)
- **When** the commit was made (timestamp)
- **Commit message** (the description you provided)
- **Snapshot** of all files in the staging area at that point in time

#### How the Snapshot Works — SHA1 Hashing

To create the snapshot, Git uses an encryption technique called **SHA1 (Secure Hashing Algorithm 1)**. The entire content of each file is converted into a unique **40-character alphanumeric hash**, for example:

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4
```

- Even a single character change in a file produces a completely different hash.
- This is how Git detects changes and ensures data integrity.

#### Where Are Commit Objects Stored?

Commit objects live inside the `.git` folder:

```
.git/
└── objects/
    └── e3/
        └── b0c44298fc1c149afbf4c8996fb924...
```

- The **first 2 characters** of the SHA1 hash become the **folder name**.
- The **remaining 38 characters** become the **file name** inside that folder.
- The content inside is **encrypted and not human-readable**.

#### Commit Chain — How Commits Reference Each Other

Each commit object also contains a reference to its **parent commit**, forming a chain:

```
C3 --> C2 --> C1
```

- The arrow points **backwards** — `C3` was made in reference to `C2`, and `C2` in reference to `C1`.
- This is how Git maintains a full, traceable history of all changes.

---

### Branch and HEAD

- A **branch** is automatically created on the **first commit**.
- At the same time, **HEAD** is created — a special pointer that generally points to the **latest commit** on the current branch.
- HEAD can be moved manually to point to any commit (e.g., during a checkout), which is how Git lets you navigate history.

```
HEAD --> main --> C3 --> C2 --> C1
```

---

### `git commit -a -m` — Skip Staging for Tracked Files

Allows you to commit modifications to already-tracked files directly, bypassing `git add`.

```bash
git commit -a -m "Your commit message"
```

- The `-a` flag only works on files that are **already being tracked** (previously committed).
- Brand new/untracked files still need to be staged with `git add` first.

---

### `git commit --amend` — Modify the Last Commit

Instead of creating a new commit object, amend lets you modify the most recent commit — updating its message or adding forgotten changes.

```bash
# Step 1: Stage the updated file
git add filename.txt

# Step 2a: Amend with a new message
git commit --amend -m "Updated commit message"

# Step 2b: Amend but keep the original message
git commit --amend --no-edit
```

- `--amend` rewrites the last commit object rather than creating a new one.
- `--no-edit` keeps the previous commit message as-is, only updating the content.
- Useful for fixing typos in commit messages or adding a file you forgot to stage.

> ⚠️ Avoid amending commits that have already been pushed to a remote repository, as it rewrites history.

---

### `git commit --allow-empty` — Create an Empty Commit

Creates a commit with no file changes at all.

```bash
git commit --allow-empty -m "Trigger CI pipeline"
```

- By default, Git prevents commits with no changes. This flag overrides that behavior.
- Primarily used to **trigger CI/CD pipelines** without making any actual code changes.

---

### `git commit -s` — Sign a Commit

Adds a **Signed-off-by** line to the commit message, certifying that you authored or have the right to submit the code.

```bash
git commit -s -m "Your commit message"
```

- The resulting commit message will include a line like:

```
Signed-off-by: Your Name <your@email.com>
```

- Commonly required in open-source projects (e.g., Linux kernel) to indicate agreement with the project's **Developer Certificate of Origin (DCO)**.
- The sign-off information is pulled from your Git config (`user.name` and `user.email`).

---

## Git Log

### `git log -n` — Limit Number of Commits Shown

By default, `git log` shows all commits. Use `-n` to limit the output to a specific number of recent commits.

```bash
# Show last 2 commits
git log -n 2

# Show last 5 commits
git log -n 5
```

---

### `git log --pretty` — Format the Output

The `--pretty` flag lets you control how much detail is shown per commit.

#### Built-in Formats

```bash
# Less output — shows commit hash and message only
git log --pretty=short

# Shows author, commit author, and message
git log --pretty=full

# Shows author, author date, commit, and commit date
git log --pretty=fuller

# Single line — commit ID and commit message
git log --pretty=oneline
```

#### Custom Format with `--pretty=format:`

| Placeholder | Description |
|-------------|-------------|
| `%h` | Abbreviated commit hash |
| `%s` | Commit message (subject) |
| `%an` | Author name |
| `%ae` | Author email |

```bash
# Show hash only
git log --pretty=format:"%h"

# Show hash and message
git log --pretty=format:"%h %s"

# Show hash, message, and author name
git log --pretty=format:"%h %s %an"

# Show hash, message, author name, and author email
git log --pretty=format:"%h %s %an %ae"
```

---

### `git log -p` — Show What Changed

Shows the **diff** (actual line-by-line changes) introduced by each commit compared to the previous one.

```bash
git log -p
```

- Lines prefixed with `+` are **additions** and lines with `-` are **deletions**.
- Very useful for a detailed code review of the history.

---

### `git log --since` / `--until` — Filter by Date

Filter commits based on when they were made using human-readable or date-formatted values.

```bash
# Commits from the last week
git log --since="1 week ago"

# Commits from yesterday
git log --since="yesterday"

# Commits from the last month
git log --since="1 month ago"

# Commits between two specific dates
git log --since="2024-01-01" --until="2024-06-30"
```

- `--since` sets the **start** of the date range.
- `--until` sets the **end** of the date range.
- Both can be combined for precise filtering.

---

### `git log --author` — Filter by Author

Shows only the commits made by a specific author.

```bash
git log --author="John"
```

- The value is matched as a **substring**, so partial names work too.
- Useful in team projects to review a specific person's contributions.

---

### `git log --grep` — Search by Commit Message

Filters commits whose messages contain a specific word or phrase.

```bash
git log --grep="fix"
git log --grep="feat"
git log --grep="refactor"
```

- Matches are **case-sensitive** by default. Add `-i` for case-insensitive search:

```bash
git log --grep="fix" -i
```

> 💡 **Best Practice:** This command is most powerful when your team follows a **commit message convention** — using dedicated keywords like `fix:`, `feat:`, `refactor:`, `chore:`, etc. With consistent naming, `--grep` becomes a reliable way to filter bug fixes, new features, or refactors out of a long history.

---

## Git Reset

### Overview

`git reset` is used to **undo changes** in your repository. It can unstage files, undo commits, or permanently delete changes depending on the mode used.

It comes in **3 modes** — soft, mixed, and hard — each differing in how aggressively they roll back changes.

```bash
git reset <mode> <commit-id>
```

To find the commit ID to reset to, use `git log --oneline`.

---

### `git reset --soft` — Undo Commit, Keep Changes Staged

Moves HEAD back to the specified commit. All changes made after that commit are preserved and placed in the **staging area**, ready to be recommitted.

```bash
git reset --soft <commit-id>
```

- Your files are **not touched** — only the commit history is rolled back.
- Changes are sitting in the staging area, as if you had just run `git add` on them.
- Useful when you want to **redo a commit** with a better message or combine multiple commits into one.

```
Before: C1 --> C2 --> C3  (HEAD)
After:  C1 --> C2          (HEAD)
C3's changes are now in the staging area
```

---

### `git reset --mixed` — Undo Commit, Keep Changes Unstaged

Moves HEAD back to the specified commit. All changes made after that commit are preserved but placed back in the **working (non-staging) area**.

```bash
git reset --mixed <commit-id>
```

- This is the **default mode** — running `git reset <commit-id>` without any flag uses `--mixed`.
- Your files are still intact, but you'll need to `git add` them again before committing.
- Useful when you want to **review and selectively re-stage** changes before recommitting.

```
Before: C1 --> C2 --> C3  (HEAD)
After:  C1 --> C2          (HEAD)
C3's changes are now in working area (unstaged)
```

---

### `git reset --hard` — Undo Commit and Delete Changes

Moves HEAD back to the specified commit and **permanently deletes** all changes made after that commit.

```bash
git reset --hard <commit-id>
```

- Files are **modified on disk** to match the state at the given commit — all newer changes are gone.
- This action is **irreversible** under normal circumstances.
- Use only when you are absolutely certain you want to discard all changes after the target commit.

```
Before: C1 --> C2 --> C3  (HEAD)
After:  C1 --> C2          (HEAD)
C3's changes are permanently deleted
```

> ⚠️ **Warning:** `--hard` is destructive. Always double-check the commit ID with `git log --oneline` before running this.

---

### Quick Comparison

| Mode | Commit Undone | Staging Area | Working Directory |
|------|--------------|--------------|-------------------|
| `--soft` | ✅ Yes | Changes kept here | Unchanged |
| `--mixed` | ✅ Yes | Cleared | Changes kept here |
| `--hard` | ✅ Yes | Cleared | Changes deleted |

---

## Git Revert

### Overview

`git revert` is used to **undo a specific commit** from history — but unlike `git reset`, it does so **safely** by creating a brand new commit that inverses the changes of the target commit. The original commit remains in history, fully preserved.

This makes `git revert` the preferred way to undo changes on **shared or remote branches** where rewriting history would cause problems for other collaborators.

---

### How It Works

When you revert a commit, Git:
1. Looks at the changes introduced by the target commit.
2. Creates a **new commit object** that applies the exact **opposite** of those changes.
3. Leaves all other commits in between completely untouched.

```
Before revert:
C1 --> C2 --> C3  (HEAD)

After: git revert <commit-id3>
C1 --> C2 --> C3 --> C4  (HEAD)
                     ↑
         New commit that undoes C3's changes
```

- C3 still exists in history — it is not deleted or modified.
- C4 is the revert commit, which cancels out C3's changes.

---

### `git revert` — Revert a Specific Commit

```bash
git revert <commit-id>
```

- Replace `<commit-id>` with the SHA hash of the commit you want to undo. Use `git log --oneline` to find it.
- Git will open your default text editor to write a message for the new revert commit.
- To skip the editor and use the default revert message automatically:

```bash
git revert <commit-id> --no-edit
```

#### Example

```bash
# Commit history (from git log --oneline)
# a1b2c3d  commit 3 - added unwanted feature
# e4f5g6h  commit 2 - fixed bug
# i7j8k9l  commit 1 - initial commit

git revert a1b2c3d
# Creates a new commit (C4) that undoes the changes from C3
# Commits 1 and 2 remain completely intact
```

---

### Git Reset vs Git Revert

| Feature | `git reset` | `git revert` |
|---------|------------|-------------|
| **Purpose** | Moves HEAD to a previous commit | Creates a new commit that undoes a specific commit |
| **History** | Rewrites/removes commits | Preserves all commits |
| **Safe for remote?** | ❌ No | ✅ Yes |
| **Creates new commit?** | ❌ No | ✅ Yes |
| **Affects working directory?** | ✅ Yes (depending on mode) | ❌ No |
| **Undoes specific commit?** | ❌ No — resets to a point in time | ✅ Yes — targets one commit precisely |
| **Risk level** | ⚠️ High (can lose work with `--hard`) | ✅ Low (non-destructive) |
| **Use case** | Local cleanup before pushing | Undoing pushed/shared commits |

---

## Git Branches

### Overview

A **branch** is created automatically when the first commit is made. Before any commit, no branch exists. The default branch is named either **`main`** or **`master`** depending on your Git configuration, and it is a **local branch** since it lives in your local environment.

- **HEAD** is a pointer that always points to the latest commit on the current branch. Its position can be changed using `git checkout`.
- You should **never work directly on the default branch**. Always create a new branch for your changes.

---

### How Branches Work

When you create a new branch, it is essentially a **duplicate copy of the branch where HEAD currently is**. The new branch inherits all the commits of its parent branch up to the point where HEAD is positioned at the time of creation.

```
main:   C1 --> C2 --> C3  (HEAD)
                          ↓
feature:                 C3  (new branch starts here)
```

- The new branch and the parent branch share the same commit history up to the point of branching.
- From this point, new commits on either branch are independent of each other.

---

### `git branch` — Create a Branch

Creates a new branch at the current HEAD position.

```bash
git branch <branch-name>
```

- This only **creates** the branch — it does not switch to it. Use `git checkout <branch-name>` to switch.

---

### Branch Sync Status

You can tell whether two branches are in sync by comparing their latest commit IDs using `git log --oneline`.

- **In sync** — Both parent and child branch point to the **same commit ID**.
- **Child is ahead** — The child branch has commits that the parent does not.
- **Child is behind** — The parent branch has commits that the child does not.

```
// In sync
main:    C1 --> C2 --> C3
feature: C1 --> C2 --> C3

// Feature is 1 commit ahead of main
main:    C1 --> C2 --> C3
feature: C1 --> C2 --> C3 --> C4

// Feature is 1 commit behind main
main:    C1 --> C2 --> C3 --> C4
feature: C1 --> C2 --> C3
```

---

### `git checkout` — Switch Between Branches or Commits

Toggles HEAD between branches or specific commits.

```bash
# Switch to a branch
git checkout <branch-name>

# Move HEAD to a specific commit
git checkout <commit-id>
```

---

### `git branch` — List Local Branches

When run without any arguments, `git branch` lists all **local branches** only. The currently active branch is highlighted with a `*`.

```bash
git branch
```

- Shows only branches present in your **local repository**.
- Does not show remote branches. Use `git branch -r` for remote branches or `git branch -a` for all.

---

### `git branch -d` — Delete a Branch

Deletes a local branch that has already been merged.

```bash
git branch -d <branch-name>
```

- Git will **refuse to delete** the branch if it has unmerged changes, protecting you from accidentally losing work.
- To force delete a branch regardless of its merge status, use `-D` (uppercase):

```bash
git branch -D <branch-name>
```

> ⚠️ Use `-D` with caution — it permanently deletes the branch and any unmerged commits on it.

---

## Git Merge

### `git switch` — Toggle Between Branches

Switches to a different branch, similar to `git checkout` but **exclusively for branches**.

```bash
git switch <branch-name>
```

- Unlike `git checkout`, which works with both branches and commit IDs, `git switch` is dedicated to branch switching only — making the intent clearer.
- Preferred in modern Git (v2.23+) when you only need to switch branches.

---

### `git merge` — Merge a Branch into Another

Used when you want the changes from one branch to be reflected in another.

```bash
# Switch to the destination branch first, then merge
git switch master
git merge <branch-name>
```

- `<branch-name>` is the branch whose changes you want to bring in.
- After merging, HEAD will point to the source branch's latest commit.

---

### Merge Scenario — Understanding What Gets Merged

#### Setup

```
Repository: my_app
Master branch has: f1, f2, f3

From master, two branches are created:
- feature1
- feature2
```

#### Step 1 — Work on feature branches

```
feature1: commits f1, f2, f3 + feature1_file  →  [f1, f2, f3, feature1_file]
feature2: commits f1, f2, f3 + feature2_file  →  [f1, f2, f3, feature2_file]
```

#### Step 2 — Merge feature1 into master

```bash
git switch master
git merge feature1
# master now has: [f1, f2, f3, feature1_file] ✅
```

#### Step 3 — Merge feature2 into master (naive approach ❌)

```bash
git switch master
git merge feature2
# Result: [f1, f2, f3, feature2_file] ❌ feature1_file is missing!
```

#### Why Does This Happen?

`feature2` was branched off from master when master only had `f1, f2, f3`. It has no knowledge of `feature1_file`. So when merged, `feature1_file` gets overwritten.

#### The Fix ✅

Before merging `feature2` into master, first **update `feature2`** with the latest changes from master:

```bash
git switch feature2
git merge master          # bring feature1_file into feature2

git switch master
git merge feature2        # now master gets all files ✅

# Final master: [f1, f2, f3, feature1_file, feature2_file] ✅
```