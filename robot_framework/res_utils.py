import re
import random

ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')


def escape_ansi(lines):
    return '\n'.join(ansi_escape.sub('', line) for line in lines.splitlines())


def join_list(list_to_join, separator='\n'):
    return separator.join(list_to_join)