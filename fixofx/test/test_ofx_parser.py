# Copyright 2005-2010 Wesabe, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest

from fixofx.ofx import Parser
from fixofx.test.ofx_test_utils import get_checking_stmt, get_creditcard_stmt, get_blank_memo_stmt


class ParserTests(unittest.TestCase):
    def setUp(self):
        parser = Parser()
        checking_stmt = get_checking_stmt()
        creditcard_stmt = get_creditcard_stmt()
        blank_memo_stmt = get_blank_memo_stmt()
        self.checkparse = parser.parse(checking_stmt)
        self.creditcardparse = parser.parse(creditcard_stmt)
        self.blank_memoparse = parser.parse(blank_memo_stmt)
    
    def test_successful_parse(self):
        """Test parsing a valid OFX document containing a 'success' message."""
        print(list(self.checkparse["body"]["OFX"][0]["SIGNONMSGSRSV1"]))
        self.assertEqual("SUCCESS",
            self.checkparse["body"]["OFX"]["SIGNONMSGSRSV1"]["SONRS"]["STATUS"]["MESSAGE"])
    
    def test_successfull_parse_for_blank_memo(self):
        """Test parsing a valid OFX document with blank memo containing a 'success' message."""
        self.assertEqual("INFO",
            self.blank_memoparse["body"]["OFX"]["SIGNONMSGSRSV1"]["SONRS"]["STATUS"]["SEVERITY"])

    def test_body_read(self):
        """Test reading a value from deep in the body of the OFX document."""
        self.assertEqual("-5128.16",
            self.creditcardparse["body"]["OFX"]["CREDITCARDMSGSRSV1"]["CCSTMTTRNRS"]["CCSTMTRS"]["LEDGERBAL"]["BALAMT"])
    
    def test_body_read_for_blank_memo(self):
        """Test reading a value from deep in the body of the OFX document."""
        self.assertEqual("-23.26",
            self.blank_memoparse["body"]["OFX"]["BANKMSGSRSV1"]["STMTTRNRS"]["STMTRS"]["BANKTRANLIST"]["STMTTRN"]["TRNAMT"])
    
    def test_header_read(self):
        """Test reading a header from the OFX document."""
        self.assertEqual("100", self.checkparse["header"]["OFXHEADER"])
    
    def test_header_read_for_blank_memo(self):
        """Test reading a header from the OFX document."""
        self.assertEqual("100", self.blank_memoparse["header"]["OFXHEADER"])
    

if __name__ == '__main__':
    unittest.main()
