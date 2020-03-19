# GIAP-python

[![Build Status](https://travis-ci.com/tutoruniverse/giap_python.svg?token=Lb9PymBqzpGUfjxxkFHm)](https://travis-ci.com/tutoruniverse/giap_python)  [![Coverage Status](https://coveralls.io/repos/github/tutoruniverse/giap_python/badge.svg?branch=mvp/develop&t=FSQDKc)](https://coveralls.io/github/tutoruniverse/giap_python) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)

## About

Python SDK for Got It Analytics Platform

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- [Poetry](https://poetry.eustace.io/)

### Installing

1. Clone this repository

   ```bash
   git clone https://github.com/tutoruniverse/giap_python.git
   ```

2. Install dependencies

   ```bash
   cd giap_python
   poetry install
   ```

3. Install `pre-commit` hooks (if you want to develop the library)

   ```bash
   pre-commit install
   ```

## Usage

```python
from giap import GIAP


TOKEN = "123456abc"
BASE_URL = "https://analytics-api.got-it.io"
USER_ID = 123

giap = GIAP(TOKEN, BASE_URL)

# Track an event
giap.track(USER_ID, "purchase", {"product_id": "EG1_credit16"})

# Set properties for a profile
giap.set_profile_properties(USER_ID, {"email": "info@gotitapp.co"})

# Increase value of a profile property
giap.increase(USER_ID, 'count', 100)
```
