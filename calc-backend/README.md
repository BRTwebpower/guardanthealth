# python3-add-subtract

This is a simple react project to perform arithmetic operations. This source has only one file named simplemath.py which contains flask_api lib based APIs.

# Dependencies

python 3.8.x
flask_api
flask-cors

# Installation

Intall python 3.8.x or higher which is applicable to your OS.
pip install flask
pip install -U flask-cors
pip install pytest

# Run in dev with debugging

Open terminal and go to root folder calc-backend and run following command
FLASK_APP=simplemath.py FLASK_DEBUG=1 python -m flask run

# End points

For adding
Json body : {"x": <num>, "y": <num>}
"http://localhost:5000/add"
For subtracting
Json body : {"x": <num>, "y": <num>}
"http://localhost:5000/sub"

# Unit testing (not verified)

Run python -m test_simplmath.py in terminal and test api using postman or other api client
