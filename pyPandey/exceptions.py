# Pandey - UserBot
# Copyright (C) 2021-2023 TeamPandey
#
# This file is a part of < https://github.com/TeamPandey/Pandey/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamPandey/pyPandey/blob/main/LICENSE>.

"""
Exceptions which can be raised by py-Pandey Itself.
"""


class pyPandeyError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyPandeyError):
    ...
