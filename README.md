# Timesheet Management Service API

## Description
This is a Staff Task Timesheet Management API built on a PostgreSQL. The API is designed to assign task and generate timesheet for said task.
Staff members, including temporary and contract workers, will be able to submit their timesheets electronically through the system.
The system automatically generates timesheets for staff, detailing the hours worked for each job assignment. 

### Dependencies
* FastAPI
* PostgreSQL|
* Python version 3.11 


### Executing program

On the terminal execute the below command to create the projects' working directory and move into that directory.

 
```python
$ mkdir timesheet-mgt
cd timesheet-mgt
```

In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

 
```python
$ py -m venv venv
```

To activate the virtual environment, execute the below command.

```python
$ source venv/Script/activate
```
Clone this repository in the projects' working directory by executing the command below.

```python
$ git clone https://github.com/ajaoooluseyi/timesheet-mgt.git
$ cd timesheet-mgt
```

To install all the required dependencies execute the below command.

```python
$ pip install -r requirements.txt
```

To run the app, navigate to the app folder in your virtual environment and execute the command below
```python
$ uvicorn main:app --reload
```

