def append_to_markdown_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

# Content to append dynamically
dynamic_content = """
## Dynamic Section

This section is dynamically added using Python.
"""

# Path to the existing Markdown file
markdown_file_path = 'example.md'

# Append the dynamic content to the Markdown file
append_to_markdown_file(markdown_file_path, dynamic_content)
