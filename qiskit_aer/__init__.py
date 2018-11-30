# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import os
from pathlib import Path

from .backends import Aer
from . import backends
from . import noise
from .version import VERSION

__version__ = VERSION
