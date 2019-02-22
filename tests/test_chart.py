import unittest

from chart.chart import Chart

class TestExample(unittest.TestCase):

    def test_loadChart1Loads(self):

        chart = Chart(**{
            "file": "data/sample1.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)

    def test_loadChart2Loads(self):

        chart = Chart(**{
            "file": "data/sample2.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)

    def test_loadChart3Loads(self):

        chart = Chart(**{
            "file": "data/sample3.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)        

    def test_loadChart4Loads(self):

        chart = Chart(**{
            "file": "data/sample4.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)        

    def test_loadChart5Loads(self):

        chart = Chart(**{
            "file": "data/sample5.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)        

    def test_loadChart6Loads(self):

        chart = Chart(**{
            "file": "data/sample6.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)                

    def test_loadChart7Loads(self):

        chart = Chart(**{
            "file": "data/sample7.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)                


    def test_loadChart8Loads(self):

        chart = Chart(**{
            "file": "data/sample8.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:
            output_ = output.read()

        self.assertIsNotNone(output_)                

    def test_loadChart9Loads(self):

        chart = Chart(**{
            "file": "data/sample9.csv", 
            "show_values": True
        })
        
        output_ = None

        with open(chart.output_file) as output:

            self.assertIsNone(output_)

    def test_chartIsNumberWholeNumber(self):
        """Whole Number."""
        value1 = Chart(file="", show_values=False).is_number(1)
        self.assertTrue(value1)

    def test_chartIsNumberWholeNumberAsString(self):
        """Whole Number as String."""
        value2 = Chart(file="", show_values=False).is_number('1')
        self.assertTrue(value2)
        
    def test_chartIsNumberFloat(self):
        """Float."""
        value3 = Chart(file="", show_values=False).is_number(1.19283)
        self.assertTrue(value3)

    def test_chartIsNumberFloatAsString(self):
        """Float as String."""
        value3 = Chart(file="", show_values=False).is_number('1.19283')
        self.assertTrue(value3)

    def test_chartIsNumberNegativeFloat(self):
        """Negative Float."""
        value4 = Chart(file="", show_values=False).is_number(-1.19283)
        self.assertTrue(value4)

    def test_chartIsNumberNegativeFloatAsString(self):
        """Negative Float as String."""
        value4 = Chart(file="", show_values=False).is_number('-1.19283')
        self.assertTrue(value4)

    def test_chartIsNumberNegativeWholeNumber(self):
        """Negative Whole Number."""
        value5 = Chart(file="", show_values=False).is_number(-1)
        self.assertTrue(value5)

    def test_chartIsNumberNegativeWholeNumberAsString(self):
        """Negative Whole Number as String."""
        value5 = Chart(file="", show_values=False).is_number('-1')
        self.assertTrue(value5)

    def test_chartIsNumberNonNumberValueAsString(self):
        """Non-numeric String Value."""
        value6 = Chart(file="", show_values=False).is_number('a')
        self.assertFalse(value6)


    def test_chartIsNumberWholeNumberGetValue(self):
        """Whole Number."""
        value1 = Chart(file="", show_values=False).get_value(1)
        self.assertTrue(value1)

    def test_chartIsNumberWholeNumberAsStringGetValue(self):
        """Whole Number as String."""
        value2 = Chart(file="", show_values=False).get_value('1')
        self.assertTrue(value2)
        
    def test_chartIsNumberFloatGetValue(self):
        """Float."""
        value3 = Chart(file="", show_values=False).get_value(1.19283)
        self.assertTrue(value3)

    def test_chartIsNumberFloatAsStringGetValue(self):
        """Float as String."""
        value3 = Chart(file="", show_values=False).get_value('1.19283')
        self.assertTrue(value3)

    def test_chartIsNumberNegativeFloatGetValue(self):
        """Negative Float."""
        value4 = Chart(file="", show_values=False).get_value(-1.19283)
        self.assertTrue(value4)

    def test_chartIsNumberNegativeFloatAsStringGetValue(self):
        """Negative Float as String."""
        value4 = Chart(file="", show_values=False).get_value('-1.19283')
        self.assertTrue(value4)

    def test_chartIsNumberNegativeWholeNumberGetValue(self):
        """Negative Whole Number."""
        value5 = Chart(file="", show_values=False).get_value(-1)
        self.assertTrue(value5)

    def test_chartIsNumberNegativeWholeNumberAsStringGetValue(self):
        """Negative Whole Number as String."""
        value5 = Chart(file="", show_values=False).get_value('-1')
        self.assertTrue(value5)

    def test_chartIsNumberNonNumberValueAsStringGetValue(self):
        """Non-numeric String Value."""
        value6 = Chart(file="", show_values=False).get_value('a')
        self.assertFalse(value6)

