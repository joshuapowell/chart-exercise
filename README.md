# Chart from CSV
Parse a CSV and generate a bar chart of the data.

<img src="examples/sample1.png" />

## Usage
To convert a file name `sample1.csv` that lives in the `data` directory of this
project, enter the following command at the command prompt from the project's
root directory.

```
python run.py --file=data/sample1.csv
```

Running the command should produce a chart that looks like this.

<img src="examples/sample1.png" />

If you don't see a bar chart that looks similar to the image above, check the
following.

1. Have you downloaded this code?
2. Did you run the command while you were in the project directory?

## Caveats

1. Please make the first column of your spreadsheet the X-axis label value 
   (i.e., year).
2. Please make sure your CSV has a header row at row 1, if it does not, the
   data in row 1 will be skipped.

## Examples
Several example cases have been added to the system in order to test the
capabilities of the Chart display tool. These sample files can be found in the
`data` directory.

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
