# 🐙 Git Notes

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
- [Merge Conflicts](#merge-conflicts)
- [Git Cherry-Pick](#git-cherry-pick)
- [Remote Repository](#remote-repository)
- [.gitignore](#gitignore)

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

---

## Merge Conflicts

### What is a Merge Conflict?

A merge conflict occurs when Git encounters **competing changes in the same part of the same file** across two different branches. Git is excellent at merging files automatically, but it draws the line when it can't logically determine which change should take precedence.

#### Common Reasons for Occurrence

- **Parallel Editing** — Two people (or you, on two different branches) edit the exact same line in a file.
- **File Deletion vs. Edit** — One person deletes a file while another is modifying it.
- **Overlapping Context** — Changes are made so close to each other that Git can't cleanly stitch the file back together.

---

### Behind the Scenes — The Three-Way Merge

To understand a conflict, you need to understand the **Three-Way Merge algorithm** Git uses.

When you merge `Branch B` into `Branch A`, Git looks at three points:
1. The tip of **Branch A** (destination)
2. The tip of **Branch B** (source)
3. The **Common Ancestor** — the last point where both branches were identical

#### The Logic

- If a line changed in `Branch B` but stayed the same as the ancestor in `Branch A` → Git **automatically takes** the change from `Branch B`. No conflict.
- If a line is **different in both** `Branch A` and `Branch B` compared to the ancestor → Git realizes both paths diverged from the original "truth." Since it doesn't know which one is the "new truth," it **pauses the merge** and marks the file as unmerged. This is a conflict.

```
Common Ancestor:  "Hello World"
Branch A:         "Hello Git"       // changed
Branch B:         "Hello Everyone"  // also changed
→ CONFLICT: Git doesn't know which to keep
```

---

### How to Resolve a Conflict

When a conflict occurs, Git pauses the merge and waits for you to clean it up manually.

#### Step 1 — Identify the Conflicted Files

```bash
git status
```

Files with conflicts will be listed under **"Unmerged paths"**.

#### Step 2 — Open the Affected File

Open the file in a text editor. Git will have inserted **conflict markers** that look like this:

```
<<<<<<< HEAD
This is the version of the code in your current branch (e.g., main).
=======
This is the version of the code from the branch being merged (e.g., feature-branch).
>>>>>>> feature-branch
```

- Everything between `<<<<<<< HEAD` and `=======` is **your current branch's version**.
- Everything between `=======` and `>>>>>>> feature-branch` is **the incoming branch's version**.

#### Step 3 — Manually Fix the Conflict

Decide what the final code should look like. You can:
- Keep **your changes** (`HEAD`)
- Keep **their changes** (`feature-branch`)
- **Combine** both
- **Rewrite** the section entirely

> ⚠️ **Critical:** You **must delete** the `<<<<<<<`, `=======`, and `>>>>>>>` markers after resolving. If left in, they will be saved literally into your code and likely cause a crash.

#### Step 4 — Finalize the Merge

Once the file is cleaned up:

```bash
# Tell Git the conflict is resolved
git add <filename>

# Commit the resolution
git commit -m "Resolved merge conflict in <filename>"
```

---

### Pro Tips for Prevention

While conflicts are inevitable in large teams, these habits can minimize them significantly:

- **Pull Often** — Constantly merge the main branch into your feature branch to catch small conflicts early before they snowball.
- **Small Commits** — Large, sweeping changes across many files are conflict magnets. Keep commits focused and atomic.
- **Communicate** — If you're going to refactor a core file, let your team know in advance.
- **Use a GUI Tool** — If the markers are confusing, tools like **VS Code's Merge Editor**, **Meld**, or **KDiff3** provide a side-by-side visual interface that makes choosing between changes much easier.

> 💡 **Tip — Abort a Merge:** If things get too messy and you want to start over, you can abort the entire merge and return to the state before it:
> ```bash
> git merge --abort
> ```

---

## Git Cherry-Pick

### What is Git Cherry-Pick?

Cherry-picking is the **"surgical" alternative to merging**. While a merge brings in an entire branch's history, a cherry-pick allows you to reach into another branch and grab a **single, specific commit**.

Instead of taking the whole "tree" (the branch), you are just picking one "cherry" (the commit) off it and placing it on yours. Git applies the changes from that commit onto your current branch and creates a **brand-new commit** with a new hash.

---

### Why is it Needed?

Cherry-picking is a power-user move — you don't use it for standard workflows, but it's a lifesaver in these scenarios:

- **Hotfixes** — You fix a critical bug in `main`, but you also need that exact fix in your ongoing `feature` branch without merging all of production's other unrelated updates.
- **Recovering Misplaced Work** — You accidentally committed code to the wrong branch. Cherry-pick it onto the correct branch, then delete it from the wrong one.
- **Collaborative Snippets** — A teammate has a specific helper function in their branch that you need, but their branch is 200 commits ahead and full of experimental code you don't want yet.

---

### How it Works

To cherry-pick, you need the **commit hash** of the commit you want to grab. Use `git log --oneline` to find it.

```bash
# Step 1: Find the hash on the source branch
git log --oneline
# Example output: a1b2c3d "Fixed the login button bug"

# Step 2: Switch to your target branch
git checkout feature-branch

# Step 3: Perform the pick
git cherry-pick a1b2c3d
```

Git applies the changes from `a1b2c3d` to your current code and creates a **new commit with a new hash**. Even though the code change is identical, Git treats it as a brand-new event in your branch's timeline.

---

### The Snapshot vs. Patch — How Cherry-Pick Really Works

A common point of confusion: *"If a commit is a full snapshot of all files, wouldn't cherry-picking bring everything with it?"*

The answer lies in how Git actually operates behind the scenes.

#### Snapshots vs. Diffs

Technically, Git stores data as **snapshots** — when you commit, Git records the full state of your files at that moment. However, when performing operations like `cherry-pick`, `merge`, or `rebase`, Git doesn't just look at the final snapshot. It **calculates the diff** — the difference between that commit and its immediate parent.

#### How the Helper Function Gets "Extracted"

Imagine your teammate's branch has 200 commits and you want Commit #200 which adds a `get_user_data()` helper function:

```
Commit #199: helper function doesn't exist yet
Commit #200: teammate adds get_user_data() — 10 lines of code

git cherry-pick #200
→ Git asks: "What is the difference between #199 and #200?"
→ Answer: Only those 10 lines for the helper function
→ Git applies ONLY that delta to your branch ✅
```

The 199 previous commits are completely ignored.

#### The Patch Analogy

Think of it this way:
- **The Snapshot (Storage):** A photo of the entire room.
- **The Patch (Operation):** An instruction that says *"Add a blue vase to the table."*

When you cherry-pick, you aren't grabbing the photo of your teammate's room (with all their experimental furniture). You are grabbing just the instruction — *"Add a blue vase"* — and following it in your own room.

#### What if the Commit Depends on Earlier Commits?

If the helper function uses a variable defined in Commit #150 (which you don't have), Git will try to apply the patch but realize the context is missing. It will stop and flag a **merge conflict**. In that case, you would either fix the conflict manually or cherry-pick Commit #150 first.

---

### Git Merge vs. Git Cherry-Pick

```
🔀 GIT MERGE                         🍒 GIT CHERRY-PICK
──────────────────────────────────   ──────────────────────────────────
📦 Takes the whole branch            🎯 Takes one specific commit
🕰️  Full history comes along          ✨ Brand-new independent commit
🔗 Creates a merge commit            🆕 Creates a fresh commit
🛠️  Routine feature integration       🚑 Hotfixes & special recoveries
🌿 Can get messy w/ divergence       🧹 Keeps history clean & neat
```

> 🔀 **Merge** when you want everything. 🍒 **Cherry-pick** when you want just one thing.

---

### Concept Summary Table

| Concept | How it Feels | What Git Actually Does |
|---------|-------------|------------------------|
| **Commit** | A full folder of files | A snapshot (stored) + a delta (calculated) |
| **Cherry-pick** | Copying a file | Applying a diff/patch to your current state |
| **Independence** | Branch-dependent | Commit #200 only knows what it changed from #199 |

---

### Aborting a Cherry-Pick

If a cherry-pick causes a mess and you want to bail out entirely:

```bash
git cherry-pick --abort
```

This returns your branch to its state before the cherry-pick was attempted.

---

## Remote Repository

### What is a Remote Repository?

So far, everything we've done — commits, branches, merges — has happened on your **local machine**. A **remote repository** is a version of your project hosted on the **internet or a network**, allowing you and your team to collaborate, back up work, and share code.

Think of it this way:

```
Local Repository  ←——— push/pull ———→  Remote Repository
(your machine)                         (GitHub / GitLab / Bitbucket)
```

- The remote is not on your computer — it lives on a server.
- The most popular remote hosting platforms are **GitHub**, **GitLab**, and **Bitbucket**.
- You can have multiple remotes for a single local repository.

---

### Why Do We Need It?

- **Collaboration** — Multiple developers can work on the same codebase from different machines.
- **Backup** — Your code is safe even if your local machine crashes.
- **Open Source** — Share your code with the world.
- **CI/CD Integration** — Remote platforms trigger automated testing and deployment pipelines on every push.

---

### `git remote` — Manage Remote Connections

A remote connection is essentially a **bookmark** with a name pointing to a URL. The default name Git gives to the primary remote is **`origin`**.

```bash
# List all remotes (names only)
git remote

# List all remotes with their URLs
git remote -v
```

#### Adding a Remote

```bash
git remote add <name> <url>

# Example
git remote add origin https://github.com/username/my-repo.git
```

- `origin` is just a conventional name — you can name it anything.
- After this, Git knows where to push and pull from.

#### Removing a Remote

```bash
git remote remove <name>

# Example
git remote remove origin
```

#### Renaming a Remote

```bash
git remote rename <old-name> <new-name>

# Example
git remote rename origin upstream
```

#### Updating a Remote URL

Used when the remote repository has moved or been renamed.

```bash
git remote set-url <name> <new-url>

# Example
git remote set-url origin https://github.com/username/new-repo-name.git
```

- Useful when you transfer a repo, change platforms, or switch from HTTPS to SSH.

#### Inspecting a Remote

Get detailed info about a specific remote — including which branches are tracked and their push/pull configuration:

```bash
git remote show <name>

# Example
git remote show origin
```

Output includes the remote URL, all tracked remote branches, and push/pull configuration.

---

### Tracking Remote Branches

When you clone or fetch a repository, Git creates **remote-tracking references** — local read-only pointers that represent the state of branches on the remote at the time of your last fetch.

```bash
# View all remote-tracking branches
git branch -r

# View all local AND remote-tracking branches
git branch -a
```

Remote-tracking branches are named in the format `origin/<branch-name>`, for example `origin/main`.

#### Creating a Local Branch from a Remote Branch

If a teammate pushed a new branch to the remote and you want to work on it locally:

```bash
git checkout -b <local-branch-name> origin/<remote-branch-name>

# Shorthand — Git auto-detects the remote branch
git checkout <branch-name>
```

Git automatically sets up upstream tracking when you do this.

---

### `git push` — Upload Local Changes to Remote

Sends your committed local changes to the remote repository.

```bash
git push <remote-name> <branch-name>

# Example — push main branch to origin
git push origin main
```

- Only **committed** changes are pushed — staged or unstaged changes are not included.
- The first time you push a new branch, use `-u` to set the upstream tracking reference:

```bash
git push -u origin main
```

After setting upstream once, you can simply run `git push` for future pushes on the same branch.

---

### `git push -u` — Set Upstream Tracking

The `-u` flag (short for `--set-upstream`) links your local branch to a remote branch. Once set, Git knows where to push and pull from automatically.

```bash
# First-time push — sets the upstream tracking reference
git push -u origin <branch-name>

# Example
git push -u origin main
git push -u origin feature-branch
```

- After running this once, all future pushes on the same branch can simply use:

```bash
git push
git pull
```

> 💡 **Tip:** You only need `-u` once per branch — the tracking information is saved in `.git/config`.

#### What is "Upstream"?

The **upstream** of a local branch is the remote branch it is linked to. You can check what upstream is set for your current branch:

```bash
git branch -vv
```

Output example:

```
* main     a1b2c3d [origin/main] Latest commit message
  feature  e4f5g6h [origin/feature] Another commit
```

The part in `[ ]` shows the upstream tracking branch.

---

### `git push --force` — Force Push

Overwrites the remote branch with your local branch, regardless of conflicts.

```bash
git push --force origin <branch-name>

# Safer alternative
git push --force-with-lease origin <branch-name>
```

- Regular `--force` is dangerous — it can overwrite teammates' commits without warning.
- `--force-with-lease` is the safer option — it only force pushes if nobody else has pushed to the remote branch since your last fetch. If someone else has pushed, it will abort.

> ⚠️ **Warning:** Never force push to `main` or `master` on a shared repository. It rewrites history and can permanently lose others' work.

---

### `git push --delete` — Delete a Remote Branch

Removes a branch from the remote repository.

```bash
git push origin --delete <branch-name>

# Example
git push origin --delete feature-branch
```

- This only deletes the branch on the **remote** — your local branch still exists.
- To delete the local branch as well, follow up with `git branch -d <branch-name>`.

---

### `git pull` — Download Remote Changes to Local

Fetches changes from the remote repository and **immediately merges** them into your current local branch.

```bash
git pull <remote-name> <branch-name>

# Example
git pull origin main
```

- `git pull` is essentially a combination of two commands:

```bash
git fetch    # downloads changes from remote
git merge    # merges them into your current branch
```

> ⚠️ If your local branch has uncommitted changes that conflict with the incoming changes, a merge conflict can occur. Always commit or stash your work before pulling.

---

### `git fetch` — Download Without Merging

Downloads all changes from the remote but does **not** merge them into your working branch. It just updates your remote-tracking references.

```bash
git fetch <remote-name>

# Example
git fetch origin
```

- Safe to run at any time — it never touches your working files.
- Useful when you want to **see what's changed** on the remote before deciding to merge.
- After fetching, you can inspect the changes with `git log origin/main` and then merge manually.

---

### `git clone` — Copy a Remote Repository Locally

Creates a complete local copy of a remote repository, including all commits, branches, and history.

```bash
git clone <url>

# Example
git clone https://github.com/username/my-repo.git
```

- Automatically sets up `origin` pointing to the cloned URL.
- The cloned folder name matches the repository name by default. You can specify a custom name:

```bash
git clone <url> my-custom-folder
```

---

### `git clone` vs `git pull` vs `git fetch` — What's the Difference?

These three commands all bring code from a remote repository to your machine, but they serve very different purposes and are used at completely different stages.

```
┌─────────────────────────────────────────────────────────────┐
│                    REMOTE REPOSITORY                        │
│                   (GitHub / GitLab)                         │
└──────────────┬──────────────┬──────────────────────────────┘
               │              │                │
           git clone      git fetch        git pull
               │              │                │
               ▼              ▼                ▼
        Creates a new   Downloads but    Downloads AND
        local copy      does NOT merge   auto-merges
        from scratch
```

#### `git clone` — Start from Nothing

Use this when you **don't have the repository locally at all**.

```bash
git clone https://github.com/username/repo.git
```

- Only ever done **once per project** on a given machine.
- Automatically sets up `origin` pointing to the remote URL.
- After cloning, use `pull` and `fetch` to stay updated — never `clone` again.

```
Before: No local repo exists
After:  Full local copy created ✅
```

#### `git fetch` — Look Before You Leap

Use this when you want to **see what has changed on the remote** without affecting your local working files.

```bash
git fetch origin
git log origin/main        # see what's new on the remote
git diff main origin/main  # compare your branch with remote
git merge origin/main      # merge only when you're ready
```

```
Before: local/main = C1→C2→C3   remote/main = C1→C2→C3→C4
After fetch:
  local/main (your branch)      = C1→C2→C3       ← unchanged
  origin/main (tracking ref)    = C1→C2→C3→C4    ← updated
```

#### `git pull` — Fetch + Merge in One Shot

Use this when you want to **immediately sync your local branch** with the remote.

```bash
git pull origin main
```

```
Before: local/main = C1→C2→C3   remote/main = C1→C2→C3→C4
After pull:
  local/main = C1→C2→C3→C4  ← updated and merged ✅
```

#### Side-by-Side Comparison

| | `git clone` | `git fetch` | `git pull` |
|---|---|---|---|
| **When to use** | First time only | Check for changes safely | Update your branch now |
| **Needs local repo** | ❌ No | ✅ Yes | ✅ Yes |
| **Touches working files** | Creates new folder | ❌ Never | ✅ Yes |
| **Auto-merges** | N/A | ❌ No | ✅ Yes |
| **Risk of conflicts** | ❌ None | ❌ None | ⚠️ Possible |
| **Frequency** | Once | Often | Often |

> 💡 **Rule of thumb:** Use `git fetch` when you want to be careful and review changes first. Use `git pull` when you trust the remote and just want to sync up fast. Use `git clone` only once when setting up a project for the first time.

---

### Local vs Remote — The Full Picture

```
Your Machine                        Remote (GitHub)
─────────────────────               ─────────────────────
Working Directory
      ↓  git add
Staging Area
      ↓  git commit
Local Repository  ──git push──→    Remote Repository
                  ←──git pull──    Remote Repository
                  ←──git fetch──   Remote Repository
                                   (no auto-merge)
```

> 💡 **Best Practice:** Always `git pull` before you `git push` to make sure your local branch is up to date with the remote. This avoids unnecessary merge conflicts and rejected pushes.

---

## .gitignore

### What is .gitignore?

When you run `git status`, Git shows you every untracked file in your project. But not every file *should* be tracked — things like build outputs, dependency folders, environment secrets, and OS-generated files have no business being in your repository.

A **`.gitignore`** file is a plain text file placed at the root of your repository that tells Git which files and folders to **completely ignore** — as if they don't exist.

```
Without .gitignore:          With .gitignore:
git status shows:            git status shows:
  node_modules/ (1200 files)   src/index.js
  .env                         README.md
  dist/
  .DS_Store
  src/index.js
  README.md
```

---

### Why Do We Need It?

- **Security** — Prevent secrets like API keys, passwords, and `.env` files from being accidentally pushed to a public repository.
- **Cleanliness** — Keep the repo free of generated files that can be recreated locally (e.g. `node_modules`, `dist`, `build`).
- **Performance** — Fewer tracked files means faster `git status`, `git add`, and `git diff` operations.
- **Collaboration** — Avoid polluting teammates' machines with files that are environment-specific (e.g. IDE settings, OS files like `.DS_Store`).

---

### Creating a .gitignore File

Simply create a file named `.gitignore` at the root of your project:

```bash
touch .gitignore
```

Then open it and add patterns — one per line. Git will ignore any file or folder that matches a pattern.

---

### Pattern Syntax

The `.gitignore` file uses a simple pattern-matching syntax:

```
# This is a comment — lines starting with # are ignored

# Ignore a specific file
.env
secret.txt

# Ignore all files with a specific extension
*.log
*.tmp
*.class

# Ignore an entire folder
node_modules/
dist/
build/
.cache/

# Ignore files in any subdirectory with a pattern
**/*.log

# Ignore a file only in the root directory (not subdirectories)
/config.json

# Ignore everything inside a folder but keep the folder itself
logs/*
!logs/.gitkeep

# Re-include (un-ignore) a specific file after a wildcard rule
*.env
!.env.example
```

#### Pattern Rules at a Glance

| Pattern | What It Ignores |
|---------|----------------|
| `*.log` | All `.log` files anywhere |
| `build/` | The entire `build` folder |
| `/config.js` | Only `config.js` in the root |
| `**/*.tmp` | All `.tmp` files in any folder |
| `!important.log` | Un-ignores `important.log` (exception) |
| `doc/*.txt` | `.txt` files directly inside `doc/` |

---

### Common .gitignore Patterns by Project Type

#### Node.js / JavaScript

```
node_modules/
dist/
build/
.env
.env.local
npm-debug.log*
yarn-error.log
.DS_Store
```

#### Python

```
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
.env
dist/
build/
*.log
```

#### Java

```
*.class
*.jar
*.war
target/
.idea/
*.iml
.DS_Store
```

#### General (any project)

```
# OS files
.DS_Store         # macOS
Thumbs.db         # Windows
desktop.ini

# Editor/IDE settings
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
logs/

# Environment secrets
.env
.env.*
!.env.example
```

---

### Important Behaviors to Know

#### .gitignore Only Works on Untracked Files

If a file has **already been committed** to the repository, adding it to `.gitignore` will **not** remove it from tracking. Git will continue tracking it.

To stop tracking a file that was already committed:

```bash
# Remove from tracking but keep the file locally
git rm --cached <filename>

# Then commit the change
git commit -m "Stop tracking <filename>"
```

#### .gitignore is Itself Tracked

The `.gitignore` file should be committed to the repository so all team members share the same ignore rules:

```bash
git add .gitignore
git commit -m "Add .gitignore"
```

#### Global .gitignore

You can set up a global `.gitignore` that applies to **all repositories** on your machine:

```bash
# Create a global gitignore file
touch ~/.gitignore_global

# Tell Git to use it
git config --global core.excludesFile ~/.gitignore_global
```

---

### Checking if a File is Ignored

Not sure if a file is being ignored? Use `git check-ignore` to find out:

```bash
git check-ignore -v <filename>

# Example
git check-ignore -v node_modules/
# Output: .gitignore:1:node_modules/    node_modules/
# Shows: which file, which line, which pattern matched
```

---

### .gitignore vs .gitkeep

These two are often confused but serve opposite purposes:

| | `.gitignore` | `.gitkeep` |
|---|---|---|
| **Purpose** | Tell Git what to **ignore** | Force Git to **track** an empty folder |
| **Contents** | List of patterns | Empty file (no content needed) |
| **Committed?** | ✅ Yes | ✅ Yes |

> 💡 **Tip:** Use [gitignore.io](https://gitignore.io) or GitHub's `.gitignore` templates to generate a ready-made `.gitignore` for your tech stack in seconds.