#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

document = { "title": "FooBar", "description": "Some description here" }

table_of_contents = [
    { "title": "test", "description": "Just a test" },
    { "title": "other", "description": "Another topic" },
]

organization = {
    "name": "FooBar.com",
    "since_year": 2000,
}

date = {
    "current_year": 2020,
}

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template("readme.md.jinja")

output = template.render(
    document = document,
    table_of_contents = table_of_contents,
    organization = organization,
    date = date
)

with open("readme.md", "w") as fh:
    fh.write(output)

