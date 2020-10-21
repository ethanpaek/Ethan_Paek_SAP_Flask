# Ethan Paek SAP Flask

This program is designed for SAP's 2021 SVNT Program Assessment.

## Task:

Create a basic Flask web application:
- Root / is not important :)
- /<int:number> will display integers from 1 to that number
- /<int:number>/odd will display only odd numbers in that range
- /<int:number>/even will display only even numbers in that range
- /<int:number>/prime will display only prime numbers in that range

## Usage:

### For Docker:

- Build the image

```bash
docker image build -t ethan_paek_flask_sap .
```

- Verify that your image shows in your image list

```bash
docker image ls
```

- Run the docker container

```bash
docker run -p 5001:5000 -d ethan_paek_flask_sap
```

Start using the application on http://localhost:5001/

### For Python Virtual Environment:

- Create the virtual environment (if you don't have one already)
```bash
python3 -m venv venv
```

- Activate virtual environment

```bash
. venv/bin/activate
```

- Install the Flask module

```bash
pip install Flask
```

- Set the FLASK_APP environment variable and start running the application

```bash
export FLASK_APP=app.py
python -m flask run
```

Start using the application on http://localhost:5000/
