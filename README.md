# burendo-handbook-public
This repository contains all the public content for the Burendo Handbook.


## Adding content

### Structure

In `docs` there are a number of subfolders. This structure will represent the side menu on the handbook. 

When you add new content, consider the structure and the menu and ensure you add new folders if necessary and put your new documents in a relevant folder.

**Do not put new content in to the root of the project or the root of `docs`, ensure they go in to one of the subfolders**

When you have made any changes, ensure you create a Pull Request on GitHub with all your changes in and get the PR approved by the Engineering community.

Each Practice should have their own folder in `docs/` and all subfolder sit beneath that, e.g.

```
└── docs
    └── Engineering
        ├── Labs
        ├── Misc
        ├── Procedures
        ├── Templates
        ├── Tooling
        └── Ways of working
```

### Branching

What is branching?  To quote directly from the [GitHub Quickstart](https://docs.github.com/en/get-started/quickstart/hello-world#creating-a-branch) guide:

>Branching lets you have different versions of a repository at one time.

>By default, your repository has one branch named main that is considered to be the definitive branch. You can create additional branches off of main in your repository. You can use branches to have different versions of a project at one time. This is helpful when you want to add new features to a project without changing the main source of code. The work done on different branches will not show up on the main branch until you merge it, which we will cover later in this guide. You can use branches to experiment and make edits before committing them to main.

>When you create a branch off the main branch, you're making a copy, or snapshot, of main as it was at that point in time. If someone else made changes to the main branch while you were working on your branch, you could pull in those updates.

### Create a branch

1. Click the Code tab of this repository.
2. Click the drop down at the top of the file list that says `main`.

3. Type a branch name, into the text box.  This formatting should ideally consist of your shortened practice name, what you are contributing and the date e.g., `eng-coolfeature-291122`.
4. Click Create branch: `eng-coolfeature-291122` from `main`.


Now you have a new branch called, `eng-coolfeature-291122`. Right now, this looks exactly the same as `main`. Next you'll add changes to the new branch.

### Making and committing changes

> You can make and save changes to the files in your repository. On GitHub, saved changes are called commits. Each commit has an associated commit message, which is a description explaining why a particular change was made. Commit messages capture the history of your changes so that other contributors can understand what you’ve done and why.

When you created a new branch in the previous step, GitHub brought you to the code page for your new `eng-coolfeature-291122` branch, which is a copy of `main`.

1. Under the `eng-coolfeature-291122` branch you created, navigate into the `docs` folder.

1. If you already have a folder to manage content for your practice, navigate into that folder, otherwise you will need to create that folder.

    - To create the folder for your practice, in the box at the top of the screen containing `Name your file...`, enter the folder name appended with a forward slash e.g., `UCD/`.  This will create the folder and navigate you into it.  You can repeat this as many times as required to create your structure as desired.  

1. Click in the box at the top of the screen containing `Name your file...`, enter the name for your file appended with a `.md` file extension e.g., `cool-feature.md`

1. In the editor, write your content. Try using different Markdown elements.  Here's a [cheat sheet](https://www.markdownguide.org/cheat-sheet/) to help with formatting. 

1. In the Commit changes box, write a commit message that describes your changes.

1. Click Commit changes.


These changes will be made only to the `cool-feature.md` file on your `eng-coolfeature-291122` branch, so now this branch contains content that's different from `main`.

### Submitting & Reviewing

>Pull requests are the heart of collaboration on GitHub. When you open a pull request, you're proposing your changes and requesting that someone review and pull in your contribution and merge them into their branch. Pull requests show diffs, or differences, of the content from both branches. The changes, additions, and subtractions are shown in different colors.

>As soon as you make a commit, you can open a pull request and start a discussion, even before the code is finished.

Now that you have changes in a branch off of `main`, you can open a pull request.

1. Click the Pull requests tab of this repository.

1. Click New pull request

1. In the Example Comparisons box, select the branch you made, `eng-coolfeature-291122`, to compare with main (the original).

1. Look over your changes in the diffs on the Compare page, make sure they're what you want to submit.

1. Click Create pull request.

1. Give your pull request a title and write a brief description of your changes. You can include emojis and drag and drop images and gifs.

1. Click Create pull request.

Your collaborators can now review your edits and make suggestions.


### Merging

Once your collaborators have reviewed your edits and approved of your changes - you will be able to merge your pull request.
Merging a pull request is the final action you need to do on GitHub.

Once you have merged your pull request, an automatic job will be fired to trigger the [merge pipeline](https://github.com/BurendoUK/burendo-handbook-infrastructure/blob/main/.github/workflows/tf-merge.yml) in [BurendoUK/burendo-handbook-infrastructure](https://github.com/BurendoUK/burendo-handbook-infrastructure) repo.
After a few minutes the handbook will have updated to reflect your new changes.
