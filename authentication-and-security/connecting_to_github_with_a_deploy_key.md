# Connecting To Github With A Deploy Key

**Step 1:** In Zenlytic, you'll first go into Settings, then Workspace Settings

![Github Deploy Key 1](../.gitbook/assets/github-deploy-key-1.png)

**Step 2:** Next, find your git repo details (these will be in Github).

Make sure to use the "SSH" format of the git URL. The format looks like `git@github.com:<YOUR_ORGANIZATION>/<YOUR_REPO>.git`, and you can find it here in your Github repo under the "Code" button with the SSH tab as shown below.

![Github Deploy Key 2](../.gitbook/assets/github-deploy-key-2.png)

**Step 3:** Now that you have that URL and the branch you want to use as your production branch, return to Zenlytic. In this example, we pasted our Github repo url (SSH format) and our production branch, which was: `master`.

![Github Deploy Key 3](../.gitbook/assets/github-deploy-key-3.png)

**Step 4:** Next we need to generate the SSH key we'll use to connect. Hit the "Generate Deploy Key" button, then the "Confirm" button, and copy the public SSH key generated.

![Github Deploy Key 4](../.gitbook/assets/github-deploy-key-4.png)

**Step 5:** Then hit Copy Deploy Key.

![Github Deploy Key 5](../.gitbook/assets/github-deploy-key-5.png)

**Step 6:** Now that you have the deploy key copied return to Github and go to "Settings."

![Github Deploy Key 6](../.gitbook/assets/github-deploy-key-6.png)

**Step 7:** Then go to Deploy Keys in the left-hand menu.

![Github Deploy Key 7](../.gitbook/assets/github-deploy-key-7.png)

**Step 8:** Then, click "Add new" and give your deploy key a name. Finally, paste that SSH key and click "Add Key."

![Github Deploy Key 8](../.gitbook/assets/github-deploy-key-8.png)

**Step 9:** Then click "Save" in the Zenlytic UI. If this saves without an error, you can close the window. You're fully connected to Github!

![Github Deploy Key 9](../.gitbook/assets/github-deploy-key-9.png)
