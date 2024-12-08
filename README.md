# Verisk Code Challenge Compute Utility
# Programmer: Reza Ashrafidoost


## Project Overview

The Compute Utility is a command-line tool that processes a list of numerical values provided via standard input. It applies two arguments: a <threshold> and a <limit> to transform the input values.

### Purpose:
- <Threshold>: For each input value, if it exceeds the threshold, the program subtracts the threshold from the input. If the value is less than the threshold, the output is zero.
- <Limit>: The cumulative sum of the output values should never exceed this limit, ensuring that individual output values are maximized without breaking the limit constraint.

The project is available in Python:
Python Script: (`compute` or `compute.py`)


This repository provides the implementation, the necessary instructions, and examples to use the tool in different environments.

## Features
- Reads input from standard input and processes each number.
- Applies the threshold and limit rules to modify the output.
- Outputs the transformed numbers and their cumulative sum.
- Handles edge cases like exceeding the limit value.

## Setup Instructions

### 1. Python Version

The Python version of the utility can be used in two ways:

#### Option 1: `python compute.py <threshold> <limit>  <  <input.txt>`


#### Option 2: `compute` (Unix Shebang)

 Ensure the script is executable:
   ```bash
   chmod +x compute
