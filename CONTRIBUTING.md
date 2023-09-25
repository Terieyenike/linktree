# Contributing Guide

Please feel free to contribute to the quality of this content by submitting PR's for improvements to code snippets, explanations, etc. If there's any doubt or if you think that a word/phrase is used confusingly, before submitting a PR, open an issue to ask about it.

## Table of Contents

- [Contributing Guide](#contributing-guide)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [1. Fork the repository](#1-fork-the-repository)
    - [2. Clone the repository in your local machine](#2-clone-the-repository-in-your-local-machine)
      - [On GitHub](#on-github)
      - [On your local machine](#on-your-local-machine)
    - [3. Create a branch](#3-create-a-branch)
    - [4. Add your changes](#4-add-your-changes)
    - [5. Commit your changes](#5-commit-your-changes)
    - [6. Push your changes](#6-push-your-changes)
    - [8. Create a pull request (PR)](#8-create-a-pull-request-pr)
  - [Resolve merge conflicts](#resolve-merge-conflicts)
  - [Where to seek for help?](#where-to-seek-for-help)
  - [Where to report bugs?](#where-to-report-bugs)
  - [Where to submit feature requests?](#where-to-submit-feature-requests)
  - [Contributing](#contributing)
  - [Improving the documentation](#improving-the-documentation)

## Getting Started
We recommend you work on the changes in your local environment because most of the contribution process requires you to do so rather than directly on GitHub.

### 1. Fork the repository

Click the `fork` button at the top of the front page. <br>
Forking is a process to create a copy of this repository in your GitHub account. You always want to remember to fork a repository before cloning it.

### 2. Clone the repository in your local machine

Clone a repository means copying the remote repository into your local machine.

#### On GitHub

1. Click your profile picture on the right top.
2. Click "Your repositories".
3. Open the forked repo by clicking on it.
4. Click the green `<> Code` button.
5. Click the copy icon to copy the HTTPS URL.

#### On your local machine

1. In your terminal, run this command to create a copy of the forked repository in your local machine:

   ```bash
   git clone https_url
   ```

   Change the `https_url` with the HTTPS link that you've copied.

2. Navigate to the directory where your local repository lives.

   ```bash
   cd linktree
   ```

Remember that you always want to work on and push your changes into the forked repository, not the original one.

### 3. Create a branch

A branch is an isolated environment to work on and save your changes. Later on, you will push this branch to the remote repository after you finish working on your changes.

Run the following command to create a branch:

```bash
git checkout -b working-branch-name
```

You can name the branch anything you want — for example, `feature-add-text`.

### 4. Add your changes

After you finish working on your changes, you must add them first. Adding changes means moving them into the staging area, where they will be ready to be saved (committed).

Run this command in your terminal:

```bash
git add .
```

This command will add all files with changes to the staging area.

### 5. Commit your changes

Now, it's time to commit the changes. Committing changes means saving your changes.

Run the following command:

```bash
git commit -m "Your message"
```

Change `Your message` into your own message. For example:

```bash
git commit -m "Feat add a new background to profile"
```

### 6. Push your changes

You want to push your changes to your remote (forked) repository. Run this command in your terminal:

```bash
git push -u origin your-branch-name
```

Change `your-branch-name` with the name of your working branch. For example:

```bash
git push -u origin feature-add-text
```

### 8. Create a pull request (PR)

1. Go to your forked repository on GitHub. <br> To ensure you're on the forked repo, look at the repo name on the top left beside the GitHub logo. It should have your GitHub username in the beginning: `your-username / repository-name`.
2. Click the `Compare & pull request` green button on the top.
3. Fill in the pull request form.
4. Click the green `Create pull request` button on the bottom.

And that's it! Congratulations on your first contribution to this repo! 🎉

## Resolve merge conflicts

You might encounter merge conflicts. When you encounter merge conflicts, you need to resolve them before your pull request can be merged into the `main` branch to avoid collision.

Merge conflicts usually occur when changes are on the same line(s), in the same file(s), from 2 different branches. It is common to encounter merge conflicts when contributing to open source.

[Back to TOC](#table-of-contents)

## Where to seek for help?

You may contact the contributor by opening a ticket. And if you are interested in seeking clarification about the
product, contact me on [Twitter](https://twitter.com/terieyenike)

[Back to TOC](#table-of-contents)

## Where to report bugs?

Feel free to [submit an issue](https://github.com/Terieyenike/linktree/issues/new/choose) on the GitHub repository, we
would be grateful to hear about it! Please make sure that you respect the GitHub issue template, and include:

1. A summary of the issue
2. A list of steps to help reproduce the issue
3. The configuration or the parts that are relevant to your issue

If you wish, you are more than welcome to propose a patch to fix the issue! See
the [Submit a patch](#submitting-a-patch) section for more information on how to best do so.

[Back to TOC](#table-of-contents)

## Where to submit feature requests?

You can [submit an issue](https://github.com/Terieyenike/linktree/issues/new/choose) for feature requests. Please make
sure to add as much detail as you can when doing so.

You are also welcome to propose patches adding new features.

[Back to TOC](#table-of-contents)

## Contributing

We welcome contributions of all kinds, there is no need to do code to be helpful! All of the following tasks are noble
and worthy contributions that you can make without coding:

- Reporting a bug (see the [report bugs](#where-to-report-bugs) section)
- Fixing a typo in the code
- Fixing a typo in the [documentation](https://github.com/Terieyenike/linktree/blob/main/README.md) (see the
  documentation contribution section)
- Providing your feedback on the proposed features and designs
- Reviewing Pull Requests If you wish to contribute code (features or bug fixes), see
  the [Submitting a patch](#submitting-a-patch) section.

[Back to TOC](#table-of-contents)

## Improving the documentation

The [documentation](https://github.com/Terieyenike/linktree/blob/main/README.md) is open-source and built with Nuxt.
You are very welcome to propose changes to it (correct typos, add examples or clarifications...) and contribute to the
Blog for Programming Nomads

The repository is also hosted on GitHub at: https://github.com/Terieyenike/linktree

[Back to TOC](#table-of-contents)
