# react-add-subtract

This is a simple react project to perform arithmetic operations. The operations are addition and subtraction of numbers. The result is obtained using python flask api. The UI accepts two inputs as integers and addition and suntraction using two buttons. The result is received as json from the API. Following are the rules for inputs:

1. Only whole numbers are allowed e.g. 0, 1, 2, 3, 4 ...
2. Nested operations are not allowed e.g. 4+9+15-
3. Errors in input or processing are dispayed as toast messages

# Project dependencies

For dependencies, refer "dependencies" in package.json file in the root folder (cacl-frontend)

# .env file

# The .env file is available in the root folder. Define your site constants

# Must put "VITE\_" prefix for any var name in

# Change VITE_APP_API_BASE_URL value as per need with trailing '/'

# Vite config

vite.config.js in root folder

# Run front end locally in a terminal

npm run dev

# Build project

# Build will copied in /dist folder

npm run build
