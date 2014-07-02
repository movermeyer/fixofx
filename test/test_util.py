#coding: utf-8
import re
from os.path import join, realpath, dirname
import unittest
from ofxtools import util


class StripEmptyTags(unittest.TestCase):
    def test_strip_empty_tags(self):
        with open(join(realpath(dirname(__file__)), 'fixtures', 'empty_tags.ofx'), 'r') as f:
            empty_tags_file = f.read()
        empty_tag_pattern = '<(?P<tag>[^>]+)>\s*</(?P=tag)>'

        result = util.strip_empty_tags(empty_tags_file)
        self.assertFalse(re.match(empty_tag_pattern, result))


if __name__ == '__main__':
    unittest.main()
