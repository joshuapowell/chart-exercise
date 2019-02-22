# Chart from CSV
Parse a CSV and generate a bar chart of the data.

<img src="examples/sample1.png" />

```
python start.py --help
```

```
python start.py --file=data/sample1.csv
```

```
python start.py --file=data/sample1.csv --show_values=False
```

## Examples
Several example cases have been added to the system in order to test the
capabilities of the Chart display tool. These sample files can be found in the
`data` directory.

- sample1.csv Example provided by Nielsen in the "Code Excercise" PDF
- sample2.csv Modified example with a column containing a non-numeric character
- sample3.csv
- sample4.csv
- sample5.csv
- sample6.csv
- sample7.csv
- sample8.csv

## Testing
To execute testing a virtual environment with the following test packages must
be installed in the project directory.

- PyCodeStyle
- PyDocStyle
- Nose
- Bandit

### Creating a Virtual Environment
To create a virtual environment to install project specific packages to,
execute this command at the Command Line.

```
virtualenv venv
```

To start the virtual environment after installation. Execute the following
command.

```
source venv/bin/activate
```

Finally, to install the testing packages execute the following command.

```
pip install -r requirements.txt
```

## Objectives

1. Use any programming language
2. Include instructions to run
3. Output the chart however you choose, but do not use a charting library
4. Run the sample with the data included, as well as several other test cases
5. Important
- Code Structure
- Code Style
- Code Comments
- Code Corectness

## Chart Requirements

- Must represent both employees and profits
- Must support negative, zero, and null values

## Sample Data

year,profit,employees
1900,20,3
1910,25,4
1920,40,10
1930,-5,6
1940,5,6

