# Claude Chat on AWS

## Project Overview

This project demonstrates how to integrate Claude AI on AWS using the Anthropic SDK and build a browser-based chatbot using Streamlit.

The application authenticates with AWS, connects to a Claude Workspace, sends prompts to Claude Sonnet, and displays AI-generated responses through a web-based chat interface.

---

## Architecture

User

↓

Streamlit Chat UI

↓

Python Application

↓

Anthropic SDK

↓

Claude Platform on AWS

↓

Claude Sonnet Model

↓

AI Response

---

## Technologies Used

* AWS
* Claude Platform on AWS
* Claude Sonnet
* Python 3.13
* Anthropic SDK
* Streamlit

---

## Prerequisites

Before starting, ensure you have:

* AWS Account
* Claude Platform Workspace
* AWS Credentials Configured
* Python Installed

---

## Step 1: Create Claude Workspace

1. Sign in to AWS.
2. Open Claude Platform on AWS.
3. Create a new workspace.
4. Copy the Workspace ID.

Example:

```text
wrkspc_xxxxxxxxxxxxxxxxx
```

---

## Step 2: Generate API Access

Create API access for the workspace and configure AWS credentials.

Verify AWS CLI:

```bash
aws configure
```

Check identity:

```bash
aws sts get-caller-identity
```

---

## Step 3: Install Required Packages

Install dependencies:

```bash
pip install anthropic
pip install streamlit
```

---

## Step 4: Create Application

Create a file named:

```text
app.py
```

Paste your Claude + Streamlit application code.

---

## Step 5: Run Application

Start the chatbot:

```bash
python -m streamlit run app.py
```

---

## Step 6: Access Chat Interface

After running the command, Streamlit generates a local URL.

Example:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## How It Works

1. User enters a prompt in the browser.
2. Streamlit sends the prompt to the Python application.
3. Anthropic SDK authenticates using AWS credentials and Workspace ID.
4. Request is sent to Claude Platform on AWS.
5. Claude Sonnet processes the prompt.
6. Response is returned to the application.
7. Streamlit displays the response in the browser.

---

## Project Screenshots

### Workspace Setup

Add screenshot here.

### API Connection Success

Add screenshot showing successful terminal output.

### Streamlit Chat UI

Add screenshot showing browser chat interface.

---

## Example Prompt

```text
What is AWS VPC?
```

Example Response:

```text
AWS VPC is a logically isolated virtual network in AWS.
```

---

## Learning Outcomes

Through this project, I learned:

* AWS Authentication
* Claude Platform Workspace Management
* Anthropic SDK Integration
* API-Based AI Applications
* Streamlit Web Application Development
* End-to-End AI Workflow Architecture

---

## Future Improvements

* Chat History Storage
* User Authentication
* Multi-Model Support
* RAG Integration
* AWS Bedrock Integration
* Deployment on EC2

---

## Author

Subham Badatya

AWS Cloud & DevOps Learner
