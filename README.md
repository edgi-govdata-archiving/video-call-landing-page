[![Code of Conduct](https://img.shields.io/badge/%E2%9D%A4-code%20of%20conduct-blue.svg?style=flat)](https://github.com/edgi-govdata-archiving/overview/blob/main/CONDUCT.md)

# Video Call Landing Page

This small app creates a landing page that participants can be sent
through prior to joining a video call, relaying important info.

Useful for:
- Making a disclaimer about call recording.
- Explaining nuances of how call will work.
- Other things? (Please [create an issue][issue] for any desired new feature!)

## Supported Platforms

- [Zoom](https://zoom.us) Meetings
- Other platforms are easily supported by changing the text instructions!

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

* We auto-deploy the `main` branch to Heroku, so merging a pull
  request deploys it!

<sub>keywords: splash page</sub>

## License & Copyright

Copyright (C) 2017-2020 Environmental Data and Governance Initiative (EDGI)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.0.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the [`LICENSE`](/LICENSE) file for details.

   [issue]: https://github.com/edgi-govdata-archiving/video-call-landing-page/issues/new
