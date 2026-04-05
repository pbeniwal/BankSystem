# 🏦 Python-MySQL Bank System

Full-stack banking application with a Python Flask backend and React frontend.

## 🛠 Required Software
Before running the application, ensure you have the following installed on your Windows laptop:
1. **MySql** database - https://dev.mysql.com/downloads/installer/
2. **Mysql Workbench** - https://dev.mysql.com/downloads/workbench/
3. **Python** - https://www.python.org/downloads/
4. **pip** - python -m ensurepip --upgrade
3. **Git** - https://git-scm.com/download/win
4. **VS Code** - https://code.visualstudio.com/


## 🚀 Getting Started

### 1. Database Setup
1. Open **mysql workbench** and create a database named `python_bank`.
2. Run the following SQL queries to create the tables(found in filedatabase_schema.sql ):

```sql
CREATE DATABASE IF NOT EXISTS python_bank;
USE python_bank;

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    type VARCHAR(10) NOT NULL, -- 'deposit' or 'withdraw'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### 2. Backend Setup(server)

#### 1. Open your terminal and navigate to the server folder:

#### Bash
```
cd server
pip install -r requirements.txt
```

#### 2. Create a file named .env in the server folder and add your mysql DB password
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD_HERE
DB_NAME=python_bank
PORT=5000
```

#### 3. Start the backend server::
#### Bash
```
python app.py
```

### 2. Frontend Setup(client)

#### 1. Open your terminal and navigate to the client folder:

#### Bash
```
cd client
npm install
```

#### 2. Launch the React application:
#### Bash
```
npm run dev
```

#### 3. Open your browser and navigate to the local URL provided:

```
http://localhost:5173
```

## 📁 Project Structure
#### /client: React frontend built with Vite, React Router, and Lucide Icons.

#### /server: Python and flask backend using the mysql-python-connector.

