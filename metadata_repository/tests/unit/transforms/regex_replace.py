# Big Data Smart Socket
# Copyright (C) 2016 Clemson University
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import unittest

from app.transforms import regex_replace


class TestRegexReplaceTransform(unittest.TestCase):

    def testTransform(self):
        opts = dict(pattern="example\.com\/files\/(.*)", repl="example.org/path/to/files/\\1")
        self.assertEqual(regex_replace.transform_url(opts, "http://example.com/files/file.txt"), "http://example.org/path/to/files/file.txt")
