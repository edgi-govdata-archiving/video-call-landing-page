# Contributing Guidelines

We love improvements to our tools! EDGI has general [guidelines for contributing][edgi-contributing] and a [code of conduct][edgi-conduct] for all of our organizational repos.

## Here are some notes specific to this project:

We are **using [Heroku Review Apps][review-apps]**, and have enabled _automatic review app creation_ for each pull request. This automation only works when a pull request is made from a feature branch in the upstream repo, and will not work from a personal fork. (This is a security feature.)

**So if you have push access on the upstream repo, this is a great reason to work from there.** When you create a pull request, Heroku will drop a link within the comments, linking to your newly deployed preview app. The app will be updated with each new commit, and will be destroyed when the pull request is merged or closed.

<!-- Links -->
[edgi-conduct]: https://github.com/edgi-govdata-archiving/overview/blob/master/CONDUCT.md
[edgi-contributing]: https://github.com/edgi-govdata-archiving/overview/blob/master/CONTRIBUTING.md
[review-apps]: https://devcenter.heroku.com/articles/github-integration-review-apps
