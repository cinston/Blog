# Blog

2/16/2019

#### By **Winston Carlos**

## Description

This is a web application for adding up blogs and commenting on existing blogs

## Link to live site
 https://carlosstoneblog.herokuapp.com
 
## User Requirements
- One should be able to sign in or register if he or she is a new user
- One should see various blogs and select the ones they prefer
- One should comment on the blogs

## Setup/Installation Requirements

### Technologies Used

- HTML
- CSS
- Flask-Bootstrap
- Python3.6
- Flask

### Clone the repo and checkout into the project folder.

- `git clone https://github.com/cinston/Blog`
- `cd Blog`

### Create and activate the virtual environment

- `python3.6 -m venv virtual`
- `source virtual/bin/activate`

### Setting up environment variables

Create a 'start.sh' file and paste the following where appropriate:

- `export SECRET_KEY='<secret_key>'`
- `export MAIL_USERNAME='<username>'`
- `export MAIL_PASSWORD='<password>'`
- `python3.6 manage.py server`

### Known Bugs
After signing in there might be an error that am working on but the thing is that your profile will have already been created, so just go back and login 

### Install the dependencies

Install dependancies that will create an environment for the app to run.

- `pip install -r requirements.txt`

### Make the file executable

- `chmod a+x start.sh`

### Open the file in the terminal

- `./start.sh`

### License

Copyright (c) 2018 **Winston Carlos**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
