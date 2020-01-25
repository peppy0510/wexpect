# __init__.py

import os

try:
    spawn_class_name = os.environ['WEXPECT_SPAWN_CLASS']
except KeyError:
    spawn_class_name = 'legacy_wexpect'

if spawn_class_name == 'legacy_wexpect':
    from .legacy_wexpect import ExceptionPexpect
    from .legacy_wexpect import EOF
    from .legacy_wexpect import TIMEOUT
    from .legacy_wexpect import spawn
    from .legacy_wexpect import run
    from .legacy_wexpect import split_command_line
    from .legacy_wexpect import join_args
    from .legacy_wexpect import ConsoleReader
    from .legacy_wexpect import __version__
    from .legacy_wexpect import searcher_string
    from .legacy_wexpect import searcher_re

    __all__ = ['ExceptionPexpect', 'EOF', 'TIMEOUT', 'spawn', 'run', 'split_command_line',
    '__version__', 'ConsoleReader', 'join_args', 'searcher_string', 'searcher_re']
    
else:
        
    from .wexpect_util import split_command_line
    from .wexpect_util import join_args
    from .wexpect_util import ExceptionPexpect
    from .wexpect_util import EOF
    from .wexpect_util import TIMEOUT

    from .console_reader import ConsoleReaderSocket
    from .console_reader import ConsoleReaderPipe

    from .host import SpawnSocket
    from .host import SpawnPipe
    from .host import run
    
    try:
        spawn = globals()[spawn_class_name]
    except KeyError:
        print(f'Error: no spawn class: {spawn_class_name}')
        raise
        
    __all__ = ['split_command_line', 'join_args', 'ExceptionPexpect', 'EOF', 'TIMEOUT',
           'ConsoleReaderSocket', 'ConsoleReaderPipe', 'spawn', 'SpawnSocket', 'SpawnPipe', 'run']