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



