[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

sa_id_number_generator
======================

`sa_id_number_generator`_ Generates South African ID Numbers for testing/QA purposes.

### Installation
```bash
$ python3 setup.py install
```

### Examples
Simple usage without parameter inputs
```python
>>> from sa_id_number_generator import generate_sa_id
>>> generate_sa_id()
['YYMMDDSSSSCAZ','YYYY-MM-DD']
```

Simple usage with parameter inputs
```python
>>> from sa_id_number_generator import generate_sa_id
>>> generate_sa_id("YYYY-MM-DD","female","citizen")
['YYMMDDSSSSCAZ','YYYY-MM-DD']
```
```python
>>> from sa_id_number_generator import generate_sa_id
>>> generate_sa_id("adult","male","citizen")
['YYMMDDSSSSCAZ','YYYY-MM-DD']
```

Usage when importing the entire module
```python
>>> import sa_id_number_generator
>>> sa_id_number_generator.generate_sa_id()
['YYMMDDSSSSCAZ','YYYY-MM-DD']
```

With variables explained
```python
>>> from sa_id_number_generator import generate_sa_id
>>> generate_sa_id(date_of_birth="YYYY-MM-DD",gender="male",citizen_status="citizen")
['YYMMDDSSSSCAZ','YYYY-MM-DD']
```

Usage as main (standalone script) - Use sa_id_number_generator.py directly (assuming you are in the package folder)
```bash
$ python3 sa_id_number_generator --help
Usage: python3 sa_id_number_generator.py [option1] arg1 [option2] arg2 ...

Generates South African ID Numbers based on options specified. If no options
are specified then options marked with (default) will be used.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -d DATE_OF_BIRTH, --date_of_birth=DATE_OF_BIRTH
                        DOB in format YYYY-MM-DD - Also accepts adult, minor
                        or any: any (default)
  -g GENDER, --gender=GENDER
                        Gender with valid values as male, female or any: any
                        (default)
  -c CITIZEN_STATUS, --citizen_status=CITIZEN_STATUS
                        Citizen status with valid values as citizen, resident
                        or any: any (default)
  -l LOOPS, --loops=LOOPS
                        Loops to the value N (number of ID Numbers to
                        generate): 1 (default)

Created by Taahirj to help with QA testing scenarios that require valid South
African ID Numbers.
```

