# This file is part of HDL Code Checker.
#
# HDL Code Checker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HDL Code Checker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HDL Code Checker.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import logging
import subprocess as subp

_logger = logging.getLogger(__name__)

def shell(cmd, env=None):
    """Dummy wrapper for running shell commands, checking the return value and
    logging"""

    if env is not None:
        subp_env = env
    else:
        subp_env = os.environ

    if type(cmd) is str:
        _logger.warning(cmd)
    else:
        _logger.warning(' '.join(cmd))

    for line in subp.check_output(cmd, shell=True, env=subp_env).split("\n"):
        if re.match(r"^\s*$", line):
            continue
        _logger.warning(line)
