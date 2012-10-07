import builtins
import locale
import codecs
import platform
import subprocess
import sys

if platform.system() == 'Windows':
    if sys.stdout.encoding != 'utf-8':
        encoding = locale.getpreferredencoding()

        subprocess.call('chcp {0} > nul'.format(encoding[2:]), shell=True)
        sys.stdout = codecs.getwriter(encoding)(sys.stdout.detach())

        __old_print = builtins.print

        def new_print(*args, **kwargs):
            __old_print(*args, **kwargs)
            sys.stdout.flush()

        builtins.print = new_print
