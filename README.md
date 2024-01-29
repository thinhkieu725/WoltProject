# Wolt Summer 2024 Engineering Internships
## Assignment by Thinh Kieu

## Backend - Python

### Purpose
This project aims to build an HTTP API which could be used for calculating the delivery fee.

Specific task requirements are available at https://github.com/woltapp/engineering-internship-2024.

### Project build requirements

In order to build the project and perform the task, the computer must be installed with Python and some additional packages with the following versions (or later):

- Python 3.9.0
- FastAPI 0.109.0
- Uvicorn 0.27.0
- Pydantic 2.5.3
- Postman
- ...

This project uses FastAPI to create an API and Uvicorn to provide an ASGI server to run the FastAPI application.
All the required packages can be installed by running

```
pip install -r requirements.txt
```


To perform the task, Postman application is used to make POST requests. The instruction on installation can be found at https://web.postman.co/.

### Task performance
To run the project, make the working directory to be the directory with the file **Delivery_fee_calculator.py**. 

Run the following command 
```
uvicorn main:app --reload
```
The window then should respond with some info lines such as:
```
INFO:     Will watch for changes in these directories: ['D:\\PythonFiles\\WoltProject']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [35580] using WatchFiles
INFO:     Started server process [29180]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
Then, open Postman application to make a post request. 
On the Postman interface, 

- Choose the request type POST.
- Enter the URL as http://127.0.0.1:8000/delivery_fee_calculator (or different first part corresponding to the http link appeared on the info lines).
- In the "Body" tab, select "raw" and choose the content type to be "JSON".
- Paste the content of a valid test in JSON format into the request body.
- Push "Send" to send the request.

Following the instructions, you should receive a response with the calculated delivery fee in the "response" dialog.

### Output example
For an example using the following test in JSON format
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
```

the output in the "response" dialog should be 

```json
{"delivery_fee": 710}
```

Additionally, more "requests" written in JSON format and their expected outputs are available in **tests** folder.