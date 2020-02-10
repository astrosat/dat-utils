# dat_utils.constants

# Constants for use by other data access token related functions

import re
from datetime import timedelta

JWT_ALGORITHM = "HS256"

# A token will be considered invalid if it was issued with a lifetime greater than this
TOKEN_MAX_LIFETIME = timedelta(hours=24, minutes=1)

# The four parts available in a data source id
SOURCE_ID_PARTS = ["authority", "namespace", "name", "version"]

# In a source id, each part can be made of up of: A-Z, a-z, 0-9 _ -
SOURCE_ID_REGEX = re.compile(
    "([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)/([A-Za-z0-9_\-]+)"
)

# In a source id pattern, each part can additionaly include:
#  * => match 0 or more chars
#  ? => match exactly 1 char
SOURCE_ID_PATTERN_REGEX = re.compile(
    "([A-Za-z0-9_\-*?]+)/([A-Za-z0-9_\-*?]+)/([A-Za-z0-9_\-*?]+)/([A-Za-z0-9_\-*?]+)"
)
