# Cache Refresh After Direct Git Pushes

Zenlytic caches your data model to keep responses fast. When you edit the model through the [Data Model Editor](../zenlytic-ui/data_model_editor.md) in the UI, the cache is invalidated automatically. When changes are pushed **directly to the underlying git repository** — bypassing the UI — the cache does not know about them.

If you or a teammate pushed changes straight to git and Zoë still appears to be using the old data model, use the **force-refresh** button in the UI to rebuild the cache from the current state of the repo. After the refresh completes, Zoë will pick up your latest changes on the next question.

## When you need to force-refresh

* A pull request was merged directly to the production branch in git.
* A teammate pushed model changes through an IDE or command line instead of the Zenlytic UI.
* You're integrating Zenlytic with a CI pipeline that commits model files automatically.

## When you don't need to force-refresh

* You edited the model in the Data Model Editor and clicked **Deploy to Production**.
* You switched branches in the UI (the UI already refreshes the cache for branch switches).
