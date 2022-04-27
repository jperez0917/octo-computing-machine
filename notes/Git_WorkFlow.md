## Card creation and git workflow

1. Start in [Project Board](https://github.com/jperez0917/octo-computing-machine/projects/1)
1. Create 'note' and convert it to 'Issue', or create 'Issue' directly.
1. Go to Issue page.
1. Click on 'Create a branch':
     ![image](https://user-images.githubusercontent.com/47562501/165170721-15299073-46d2-4627-932e-efe48c694a0a.png)
1. Click 'Create branch':
     ![image](https://user-images.githubusercontent.com/47562501/165170869-08942f34-1b53-4fba-af96-ce8a194cd1fc.png)
1. Click the copy button:
     ![image](https://user-images.githubusercontent.com/47562501/165170998-f904cb02-290a-4b42-8e47-7aedc88d8286.png)
1. Paste branch fetch and checkout command into terminal (which has current directory as the repository) and press enter:
     ![image](https://user-images.githubusercontent.com/47562501/165171263-53971ab5-365f-41f2-8350-396c9bc7c02b.png)
1. The branch should now be checked out on your machine.
1. Perform the work on the code.
1. When coding finished, do:
     `git add <files>`
  2. `git commit -m "<commit message>"`
  3. `git push`
1. Go to GitHub and open branch page:
     ![image](https://user-images.githubusercontent.com/47562501/165171952-37c8caf0-4d87-46dd-8815-106cb99313f1.png)
1. Click compare and pull request button.
1. Verify merging to proper branch.
1. Click 'Create pull request'.
1. Assign task to 'Reviewers' or 'Assignees'.
     ![image](https://user-images.githubusercontent.com/47562501/165172447-0a51169e-c641-430a-9a70-ad2f92859906.png)
1. Go to your terminal.
1. After the branch has been merged into main on remote.
1. Go ahead and use the delete branch button on the merge request.
1. `git fetch`
1. `git checkout main`
1. `git merge origin main`
1. `git remote update origin --prune`
1. Continue on to next card.
