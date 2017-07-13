# Video Call Landing Page

This small app creates a landing page that participants can be sent
through prior to joining a video call, relaying important info.

Useful for:
- Making a dislaimer about call recording.
- Explaining nuance of how call will work.
- Other things? (Please [create an issue][issue] for any desired new feature!)

### Supported Platforms

- Zoom Meetings
- Other platforms easily supported by changing text instructions!

## Development

- [`virtualenvwrapperi`](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
- Python 3 (package usually called `python3` or `python`)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

```
python --version # Should be version 3.y.z

mkvirtualenv edgi-call-splashpage --python=`which python3`
workon edgi-call-splashpage
make setup
make run
```

Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for important details,
including our use of **Heroku Review Apps**.

## Deployment

* We auto-deploy the `master` branch to Heroku, so merging a pull
  request deploys it!

<sub>keywords: splash page</sub>

   [issue]: https://github.com/edgi-govdata-archiving/video-call-landing-page/issues/new
