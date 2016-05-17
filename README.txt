## Setup workinv env

```
#!bash

    mkvirtualenv bounce_email
    pip install -r requirements.txt
```

## Run the tests

```
#!bash

    nosetests --verbose
```

## Usage

```
#!python

    from bounce_email import bounce_email

    msg = """ Fill with raw email text
    """
    # Do something with bounce info
    bounce = bounce_email.BounceEmail(msg)
    bounce.is_bounced  # True/False
    bounce.code  # e.g. "5.0.0"
    bounce.reason  # e.g. "Description of the bounce code"
    bounce.bounce_type  # "Permanent Failure", "Persistent Transient Failure", "Success" -- BounceEmail::TYPE_HARD_FAIL, TYPE_SOFT_FAIL, TYPE_SUCCESS
```
