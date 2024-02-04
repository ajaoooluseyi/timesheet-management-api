# Timesheet Management Service API

## Description
The Timesheet Management Service API is designed for efficient task assignment and timesheet generation. Built on PostgreSQL, this API streamlines the process of managing tasks and tracking time for staff members, including temporary and contract workers. Staff members, including temporary and contract workers, will be able to submit their timesheets electronically through the system. It generates the timesheets for tasks and staff members, simplifying administrative tasks and ensuring accurate record-keeping. 

### Dependencies
* FastAPI
* PostgreSQL|
* Python version 3.11 

### Features
- Task assignment: Assign tasks to staff members with ease.
- Timesheet generation: Automatically generate timesheets detailing hours worked for each job assignment.
- Electronic submission: Allow staff members to submit timesheets electronically through the system.
- Staff clock-in and clock-out

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

Set up PostgreSQL:
- Install PostgreSQL on your system if not already installed.
- Open your command-line interface (CLI) or terminal.
- Connect to the PostgreSQL server (using psql) by entering the following command:
```bash
psql -U your_username
```
- Create a database for the API
```sql
CREATE DATABASE timesheet;
```

To run the app, navigate to the app folder in your virtual environment and execute the command below
```python
$ uvicorn main:app --reload
```
