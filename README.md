# pylinkedin

Django Rest Framework Task


License: GPLv3


## Basic Commands

- Open a terminal at the project root and run the following for local development:

    $ docker-compose -f local.yml up


- And then run:

    $ docker-compose -f local.yml run --rm django python manage.py migrate

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ docker-compose -f local.yml run --rm mypy pylinkedin

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker-compose -f local.yml run --rm coverage run -m pytest
    $ docker-compose -f local.yml run --rm coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ docker-compose -f local.yml run --rm pytest


### Sentry


## Deployment

The following details how to deploy this application.

### Docker
