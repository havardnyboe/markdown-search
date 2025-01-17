# Path to markdown files
MARKDOWN_FILES_DIR = "../../markdown-search/oppgaver"

# path sepearator under your OS
PATH_SEPERATOR = '/'

# Location of index file
INDEX_DIR = "search_index"

# Command to use when clicking on filepath in search results
EDIT_COMMAND = "open"

# Toggle to show Whoosh parsed query
SHOW_PARSED_QUERY=True

# Toogle to use tags
USE_TAGS=True

# Optional prefix in a markdown file, e.g. "tags: python search markdown tutorial"
TAGS_PREFIX="tags: "

# List of tags that should be ignored
TAGS_TO_IGNORE = "and are what how its not with the"

# Regular expression to select tags, eg tag has to start with alphanumeric followed by at least two alphanumeric or "-" or "."
TAGS_REGEX = r"\b([A-Za-z0-9][A-Za-z0-9-.]{2,})\b"

# Flask settings
DEBUG = True,
SECRET_KEY = 'my secret key',