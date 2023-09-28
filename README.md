# Rayka code challenge

This is a programming challenge to build a simple API and deploy it on the AWS platform.

>You can test the API using the below URL
>>[API Base URL](https://uq3ivlxsij.execute-api.eu-north-1.amazonaws.com/dev)

##Dependencies
1. python 3.11
2. node 20.5
3. serverless 3.35

## Run it on your local machine

**1. Create a virtual environment**

Go to the project root directory and run the below command to create a new Python virtual environment:

```console
python3 -m venv <virtual-environment-name>
```

**2. Activate the virtual environment**

Run the below command to activate your virtual environment:

```console
source ./venv/bin/activate
```

Now your virtual environment is ready to use

**3. Install dependencies**

You can install the project dependencies by the below command:

```console
pip install -r requirements.txt
```

**4. Start the server**

Start the server with Django `runserver` with the following command:

```console
python manage.py runserver 0.0.0.0:<port>
```

Done:beer:	

## Deploy and run on AWS

**1. Config AWS credentials on Serverless**

Run the below command to set your credentials on serverless:

```console
serverless config credentials --provider aws --key <access-key-id> --secret <secret-access-key>
```

**2. Install Serverless plugins**

To install Serverless plugins, navigate to the project root directory and run the following command:

```console
npm install
```

**3. Deploy on AWS**

To deploy the code on the AWS cloud provider, use the following command:

```console
serverless deploy
```

Done:beer:	

## Environment variables:

| Key | Value |
| --- | ----------- |
| AWS_ACCESS_KEY_ID | AWS access key id |
| AWS_SECRET_ACCESS_KEY | AWS secret key id |
| AWS_DEFAULT_REGION | Your region on AWS |

> **_NOTE:_**  If you running the application on your local machine, you need to create a `.env` file in `python_code_challenge` directory. Otherwise, there is no need to specify environment variables.
