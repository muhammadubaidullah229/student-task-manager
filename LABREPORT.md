# Lab Assignment 4 — Lab Report (Part G)

**Name:** Muhammad Ubaidullah
**Registration No.:** SP23-BSE-131
**Course:** CSC418 — DevOps for Cloud Computing
**Lab Assignment:** 4 — Student Task Manager
**Date:** 18 November 2026

## Q1. What is the difference between Git and GitHub? What is the purpose of `git add`, `git commit`, and `git push`?

Git and GitHub are not the same thing. Git is a tool that runs on my own
computer and keeps the history of my project — every change I save becomes
a commit I can go back to. GitHub is a website that stores that same Git
history online, so my code is backed up and other people can see it and
work on it with me. In short: Git is the version control system, GitHub
is the place where the repository lives on the internet.

`git add` picks which changed files I want to include in the next save —
it stages them. `git commit` actually saves that staged snapshot into the
local history, with a message saying what I changed and why. `git push`
sends my local commits up to GitHub, so the online repository matches
what I have on my computer.

## Q2. Why do we use branches and pull requests? What causes merge conflicts?

We use branches so that a new feature can be built separately from the
stable code on `main`. If the new feature breaks something, `main` is
still safe, and I can fix the branch without touching the working code.
In this project I used one branch per feature — `feature/addtask`,
`feature/completetask`, and `feature/deletetask` — and merged each one
back only after its tests passed.

A pull request is how a finished branch is reviewed before it is merged.
It shows all the changes in one place, lets a teammate check them, and
only then is the branch merged into `main`, closing the related Issue.

A merge conflict happens when two branches change the same lines of the
same file in different ways, and Git cannot decide which version is
right. In this project it happened on purpose: one branch set the README
status to "In Progress" and another set the same line to "Completed".
Git stopped the merge and asked me to choose, because both edits
touched the exact same line.

## Q3. What is the difference between `git fetch` and `git pull`? What is the difference between merge and rebase?

`git fetch` only downloads the new commits from GitHub into my local
repository — it does not change my working files. `git pull` does a
fetch and then merges those downloaded commits into my current branch,
so my files are updated too. So fetch is "look, but don't touch", and
pull is "download and apply".

Merge and rebase are two ways of combining branches. A merge keeps both
histories as they are and creates a new merge commit joining them, so
you can still see that the work happened on a separate branch. A rebase
moves my branch's commits on top of the other branch, one by one, so the
history looks like one straight line with no merge commit. I used merges
in this project, with `--no-ff`, because the merge commits clearly show
each pull request and keep the branch history visible.

## Q4. How do GitHub Issues and GitHub Actions help a team?

Issues are like a to-do list for the project that everyone can see. Each
issue describes one task or one bug, so work is not lost in chat messages.
In this project I created four issues — one for each feature and one for
the documentation — and each pull request said which issue it closed,
so you can trace a feature from the issue to the code that fixed it.

GitHub Actions runs jobs automatically when something happens on GitHub.
My workflow runs all the unit tests on every push and every pull request
to `main`. That means a broken change is caught by the server before it
is merged, instead of someone finding out later that the tests fail.
For a team, this saves time and stops broken code from reaching `main`.

## Q5. Describe one difficulty you faced during this lab and how you solved it.

The difficulty I faced was the merge conflict between the two status
branches. I had created `conflict/status-in-progress` and
`conflict/status-completed` from the same commit, and both changed the
same line of the README — one to "In Progress" and one to "Completed".
After merging the first branch, merging the second one failed with
"CONFLICT (content): Merge conflict in README.md", and Git left the file
with `<<<<<<<`, `=======`, and `>>>>>>>` markers in it.

At first the markers looked confusing, because the file had both versions
in it at once. I solved it by opening the README, reading both sides of
the conflict, and deciding which one was correct. "Completed" was wrong —
the project still had the workflow, the user guide, and this report left
to add — so I kept "In Progress" and added a line explaining the choice.
Then I ran `git add README.md` and committed the merge. I also saved the
conflicted file first, in `labevidence/conflict-readme-before.txt`, as
proof of the conflict. The lesson was simple: a conflict is not lost work,
it is Git asking a human to decide, and the decision should match the
real state of the project.
