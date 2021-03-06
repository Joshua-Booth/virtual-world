# ===================================
# Filename: _log.py
# Purpose: To provide logging functionality to the virtual-world program.
#
#
# virtual-world
# Copyright (C) 2017  Joshua Peter Booth
#
# This file is part of virtual-world.
#
# virtual-world is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# virtual-world is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with virtual-world (see LICENSE.md).
# If not, see <http://www.gnu.org/licenses/>.
#
# Contact me:
# Email: joshb00th@icloud.com
# ===================================

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
log_format = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s - ' \
             'Line: %(lineno)d'
formatter = logging.Formatter(log_format)

fh = logging.FileHandler('log.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
