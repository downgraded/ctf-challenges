# madlib

**Category:** Web

**Difficulty:** Easy-Medium

**Author:** downgrade


## Description

I just created the first draft of my first flask project, a madlib generator that fills the given words into a madlib template! Try it out and let me know what you think! The character length limit should make this app pretty secure.

## Deploy notes

- Simply run the attached `run.sh` script. Replace port 10000 with whatever port you would like the challenge to listen on. 

## Solution

The shortest (currently known) jinja2 RCE payloads are about 55 characters long. However, with ~20 characters and multiple injection points, we can split this up by utilizing `{% set %}` and building up the payload piece by piece. Full solve script in `solve.py`.
