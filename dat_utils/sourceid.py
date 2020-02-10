# dat_utils.sourceid

# Functions dealing with data source ids and pattern matching

import re
import fnmatch
from pathlib import PurePosixPath as PurePath
from dat_utils.constants import (
    SOURCE_ID_REGEX,
    SOURCE_ID_PATTERN_REGEX,
    SOURCE_ID_PARTS,
)


def is_valid_source_id(source_id, pattern=False):
    """
    Checks if the given string is a valid short-form data source id, e.g.
      astrosat/forestry/canopy-change/2019-12-05
    Returns a boolean indicating validity.
    """
    m = (SOURCE_ID_PATTERN_REGEX if pattern else SOURCE_ID_REGEX).match(source_id)
    return m is not None


def source_id_to_parts(source_id, pattern=False):
    """
    Converts a short-form data source id to a dict, e.g.
      astrosat/forestry/gu-canopy-change/2019-12-04
    is converted to:
    {
        "authority": "astrosat",
        "namespace": "forestry",
        "name": "gu-canopy-change",
        "version": "2019-12-04"
    }

    The pattern parameter allows pattern symbols to be included.
    Returns either the dict, or raises ValueError if the id is invalid.
    """
    m = (SOURCE_ID_PATTERN_REGEX if pattern else SOURCE_ID_REGEX).match(source_id)
    if m is None:
        if pattern:
            raise ValueError("Not a valid source id pattern: {}".format(source_id))
        else:
            raise ValueError("Not a valid source id: {}".format(source_id))
    else:
        return {
            "authority": m.group(1),
            "namespace": m.group(2),
            "name": m.group(3),
            "version": m.group(4),
        }


def match_source_id_pattern(source_id, id_pattern):
    """
    Given a source id, check it against the pattern.
    Returns True if matches, False if it doesn't.
    """
    source_id_parts = source_id_to_parts(source_id)
    id_pattern_parts = source_id_to_parts(id_pattern, pattern=True)

    for part in SOURCE_ID_PARTS:
        if not fnmatch.fnmatch(source_id_parts[part], id_pattern_parts[part]):
            return False

    return True


def match_source_id_patterns(source_id, id_patterns):
    """
    Given a source id, check it against a list of patterns.
    If any of the patterns match, returns True, otherwise False.
    """
    for id_pattern in id_patterns:
        if match_source_id_pattern(source_id, id_pattern):
            return True

    return False


def pattern_to_regex(pattern):
    """
    Given a pattern, return a regex that will match the pattern
    """
    return pattern.replace("*", ".*").replace("?", ".")


def source_id_parts_regexs(parts):
    """
    Given a source id pattern in parts form, return regexes
    """
    return {
        "authority": pattern_to_regex(parts["authority"]),
        "namespace": pattern_to_regex(parts["namespace"]),
        "name": pattern_to_regex(parts["name"]),
        "version": pattern_to_regex(parts["version"]),
    }
