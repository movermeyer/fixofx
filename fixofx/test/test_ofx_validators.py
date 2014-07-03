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

from fixofx.ofx import RoutingNumber


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.good_aba = RoutingNumber("314074269")
        self.bad_aba  = RoutingNumber("123456789")
    
    def test_not_a_number(self):
        nan = RoutingNumber("123abd")
        self.assertEqual(nan.is_valid(), False)
        self.assertEqual(nan.get_type(), None)
        self.assertEqual(nan.get_region(), None)
        self.assertEqual(str(nan),
                         "123abd (valid: False; type: None; region: None)")
    
    def test_valid_aba(self):
        self.assertEqual(self.good_aba.is_valid(), True)
        self.assertEqual(self.bad_aba.is_valid(), False)
    
    def test_aba_types(self):
        self.assertEqual(RoutingNumber("001234567").get_type(), 
                         "United States Government")
        self.assertEqual(RoutingNumber("011234567").get_type(), 
                         "Primary")
        self.assertEqual(RoutingNumber("071234567").get_type(), 
                         "Primary")
        self.assertEqual(RoutingNumber("121234567").get_type(), 
                         "Primary")
        self.assertEqual(RoutingNumber("131234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("201234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("211234567").get_type(), 
                         "Thrift")
        self.assertEqual(RoutingNumber("251234567").get_type(), 
                         "Thrift")
        self.assertEqual(RoutingNumber("321234567").get_type(), 
                         "Thrift")
        self.assertEqual(RoutingNumber("331234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("601234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("611234567").get_type(), 
                         "Electronic")
        self.assertEqual(RoutingNumber("641234567").get_type(), 
                         "Electronic")
        self.assertEqual(RoutingNumber("721234567").get_type(), 
                         "Electronic")
        self.assertEqual(RoutingNumber("731234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("791234567").get_type(), 
                         None)
        self.assertEqual(RoutingNumber("801234567").get_type(), 
                         "Traveller's Cheque")
        self.assertEqual(RoutingNumber("811234567").get_type(), 
                         None)
    
    def test_aba_regions(self):
        self.assertEqual(RoutingNumber("001234567").get_region(), 
                         "United States Government")
        self.assertEqual(RoutingNumber("011234567").get_region(), 
                         "Boston")
        self.assertEqual(RoutingNumber("071234567").get_region(), 
                         "Chicago")
        self.assertEqual(RoutingNumber("121234567").get_region(), 
                         "San Francisco")
        self.assertEqual(RoutingNumber("131234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("201234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("211234567").get_region(), 
                         "Boston")
        self.assertEqual(RoutingNumber("251234567").get_region(), 
                         "Richmond")
        self.assertEqual(RoutingNumber("321234567").get_region(), 
                         "San Francisco")
        self.assertEqual(RoutingNumber("331234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("601234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("611234567").get_region(), 
                         "Boston")
        self.assertEqual(RoutingNumber("641234567").get_region(), 
                         "Cleveland")
        self.assertEqual(RoutingNumber("721234567").get_region(), 
                         "San Francisco")
        self.assertEqual(RoutingNumber("731234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("791234567").get_region(), 
                         None)
        self.assertEqual(RoutingNumber("801234567").get_region(), 
                         "Traveller's Cheque")
        self.assertEqual(RoutingNumber("811234567").get_region(), 
                         None)
    
    def test_aba_string(self):
        self.assertEqual(str(self.good_aba), 
                         "314074269 (valid: True; type: Thrift; region: Dallas)")
    

if __name__ == '__main__':
    unittest.main()
