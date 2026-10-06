# Expense Report Automation

An AI-powered Expense Report Automation project built with **Python** and **Microsoft Azure**. The project helps automate the processing of expense information by extracting and organizing relevant data, reducing manual effort involved in preparing expense reports.

## Features

* Automated expense data processing
* Extraction of relevant expense information
* Organization of expense records
* AI-powered document/data processing
* Reduces manual data entry
* Azure-powered AI processing
* Python-based implementation

## Technologies Used

* Python
* Microsoft Azure
* Azure AI Services
* Python libraries for document and data processing

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Areeza01/Expense-Report-Automation.git
cd Expense-Report-Automation
```

### 2. Create a `.env` file

Create a `.env` file in the root directory:

```text
.env
```

### 3. Configure Azure credentials

Add your own Azure credentials to the `.env` file.

Example:

```env
AZURE_OPENAI_ENDPOINT=YOUR_AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_KEY=YOUR_AZURE_OPENAI_KEY
DATABASE_URL=YOUR_DATABASE_URL
APPROVAL_AGENT_ID=YOUR_APPROVAL_AGENT_ID
EXPENSE_AGENT_ID=YOUR_EXPENSE_AGENT_ID
AZURE_MODEL_DEPLOYMENT=YOUR_AZURE_MODEL_DEPLOYMENT_NAME
```

Replace the placeholder values with your own Azure configuration.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

Run the main Python file:

```bash
python app.py
```

> **Note:** The `.env` file is intentionally excluded from this repository because it contains sensitive credentials. Each user must create their own `.env` file and provide their own Azure credentials.

## Environment Variables

A `.env.example` file can be included in the repository to show the required configuration without exposing credentials.

Example:

```env
AZURE_OPENAI_ENDPOINT=YOUR_AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_KEY=YOUR_AZURE_OPENAI_KEY
DATABASE_URL=YOUR_DATABASE_URL
APPROVAL_AGENT_ID=YOUR_APPROVAL_AGENT_ID
EXPENSE_AGENT_ID=YOUR_EXPENSE_AGENT_ID
AZURE_MODEL_DEPLOYMENT=YOUR_AZURE_MODEL_DEPLOYMENT_NAME
```

Never commit your actual `.env` file or expose your Azure credentials publicly.

## Project Purpose

The purpose of this project is to demonstrate how AI can automate expense-report workflows by extracting and organizing expense information, making the reporting process more efficient and reducing repetitive manual work.

## Author

**Areeza Maryam**
