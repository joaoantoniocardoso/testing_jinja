#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import re, mmap

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

def get_custom_content(output_file):
    try:
        with open(output_file, "r+") as f:
            data = mmap.mmap(f.fileno(), 0).read().decode('utf-8')
            start_re = "<!---\s*start\s*of\s*user\s*content\s*-->\n"
            end_re = "<!---\s*end\s*of\s*user\s*content\s*-->\n"
            result = re.search("(" + start_re + ".*" + end_re + ")",
                            data, re.DOTALL)
            if result:
                return result.group(1)
            return ''
    except Exception as error:
        return ''


output_file = "readme.md"

custom_content = get_custom_content(output_file)

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

template = env.get_template("readme.md.jinja")

output = template.render(
    document = document,
    table_of_contents = table_of_contents,
    organization = organization,
    date = date,
    custom_content = custom_content
)

with open(output_file, "w") as fh:
    fh.write(output)

