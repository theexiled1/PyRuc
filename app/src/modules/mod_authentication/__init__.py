# -*- coding: utf-8 -*-

""" PyRuc-UAC-SERVICE
    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.
    Development Team: Stanislav WEB
"""

from .index import login
from .exceptions import AuthenticationNotAvailableError, AuthenticationRequestError, \
                        AuthenticationNotFoundError, AuthenticationForbiddenError
