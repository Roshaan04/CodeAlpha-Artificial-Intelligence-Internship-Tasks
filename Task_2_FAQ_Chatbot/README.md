
# 🤖 AI FAQ Chatbot

An intelligent **Frequently Asked Questions (FAQ) Chatbot** developed as part of the **CodeAlpha Artificial Intelligence Internship**.

This project provides a simple and user-friendly graphical interface where users can enter their questions and receive the most relevant answers from a predefined FAQ knowledge base. The chatbot uses **Natural Language Processing (NLP)** and **text similarity techniques** to understand the user's question and identify the closest matching FAQ.

---

## 📌 Project Overview

The **AI FAQ Chatbot** is designed to simulate a basic question-answering system.

Instead of requiring the user to search manually through a list of frequently asked questions, the user can simply type a question in the chatbot interface. The system processes the question, compares it with the available FAQ questions, and returns the most relevant answer.

### 💡 Example

**User asks:**

> How can I reset my password?

**Chatbot responds:**

> To reset your password, click on the "Forgot Password" option on the login page and follow the instructions provided.

The system is designed to provide quick and simple answers to commonly asked questions.

---

# ✨ Features

* 🤖 Interactive FAQ chatbot
* 💬 User-friendly graphical user interface
* 🧠 Natural Language Processing (NLP)
* 🔍 Question similarity matching
* 📚 Predefined FAQ knowledge base
* ⚡ Fast response generation
* 🖥️ Simple desktop-based interface
* 📦 Easy to install and run
* 🔄 Handles multiple user questions
* 🛡️ Provides a fallback response when no suitable answer is found

---

# 🛠️ Technologies Used

The project is developed using the following technologies:

| Technology                               | Purpose                                     |
| ---------------------------------------- | ------------------------------------------- |
| 🐍 **Python**                            | Main programming language                   |
| 🧠 **Natural Language Processing (NLP)** | Processing and understanding user questions |
| 🔤 **Text Processing**                   | Cleaning and preparing text for comparison  |
| 📊 **TF-IDF / Text Similarity**          | Finding the most relevant FAQ               |
| 🖥️ **Tkinter**                          | Creating the graphical user interface       |
| 📄 **JSON / Python Data**                | Storing FAQ questions and answers           |
| 🌐 **Virtual Environment (venv)**        | Managing project dependencies               |

> **Note:** The exact NLP and similarity libraries used by the project are defined in the project's Python files and dependency configuration.

---

# 🧠 How the Chatbot Works

The chatbot follows a simple NLP-based workflow:

```text
              👤 USER
                 │
                 ▼
       Enter a question
                 │
                 ▼
        🧹 Text Processing
                 │
                 ▼
       🧠 NLP / Similarity
                 │
                 ▼
       Compare with FAQ Data
                 │
                 ▼
       🔍 Find Best Match
                 │
                 ▼
       💬 Generate Response
                 │
                 ▼
              👤 USER
```

### Step 1 — User Input

The user enters a question through the chatbot's graphical interface.

### Step 2 — Text Processing

The input question is processed so that it can be compared with the questions stored in the FAQ dataset.

### Step 3 — Similarity Matching

The chatbot compares the user's question with the available FAQ questions and calculates which question is the most similar.

### Step 4 — Best Match Selection

The FAQ with the highest similarity score is selected as the most relevant result.

### Step 5 — Response

The answer associated with the selected FAQ is displayed in the chatbot interface.

### Step 6 — Fallback Response

If the chatbot cannot find a sufficiently relevant FAQ, it provides a default response informing the user that it could not find a suitable answer.

---

# 📂 Project Structure

The project is organized into separate files according to their responsibilities:

```text
Task_2_FAQ_Chatbot/
│
├── 🤖 gui.py
│   └── Creates and manages the graphical user interface.
│
├── 🧠 bot.py
│   └── Contains the chatbot logic and FAQ matching process.
│
├── 🚀 main.py
│   └── Main entry point used to start the chatbot application.
│
├── 📚 faq_data.py
│   └── Contains the predefined FAQ questions and answers.
│
├── 📦 venv/
│   └── Local Python virtual environment.
│       This folder should NOT be uploaded to GitHub.
│
└── 📖 README.md
    └── Project documentation.
```

### 📌 Important

The `venv` folder is a local virtual environment created on the developer's computer. It should **not** be uploaded to GitHub because it contains installed packages and environment-specific files.

Instead, other users can create their own virtual environment by following the installation instructions below.

---

# ⚙️ Requirements

Before running the project, make sure you have:

* 🐍 Python 3.x
* 💻 Windows, macOS, or Linux
* 📦 Required Python libraries used by the project

You can check whether Python is installed by running:

```bash
python --version
```

If that command does not work, try:

```bash
py --version
```

---

# 🚀 Installation and Setup

Follow the steps below to run the chatbot on your computer.

## 1️⃣ Clone the Repository

Clone the CodeAlpha tasks repository:

```bash
git clone https://github.com/YOUR_USERNAME/codealpha_tasks.git
```

Navigate to the FAQ chatbot directory:

```bash
cd codealpha_tasks/Task_2_FAQ_Chatbot
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

---

## 2️⃣ Create a Virtual Environment

Create a new Python virtual environment:

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 3️⃣ Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

After activation, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal prompt.

For example:

```text
(venv) PS C:\Users\YourName\codealpha_tasks\Task_2_FAQ_Chatbot>
```

---

## 4️⃣ Install Dependencies

If a `requirements.txt` file is provided, install the required packages using:

```bash
pip install -r requirements.txt
```

If the project does not contain a `requirements.txt` file, install the required libraries according to the imports used in the project.

For example, if your project uses Scikit-learn:

```bash
pip install scikit-learn
```

If Tkinter is required, it is generally included with standard Python installations on Windows.

---

# ▶️ Running the Application

Once the virtual environment is activated and all dependencies are installed, run:

```bash
python main.py
```

The chatbot graphical interface should open.

You can then type your question into the input field and submit it to receive an answer.

---

# 🖥️ Expected Output

When the application starts, a graphical chatbot window will appear.

The interface allows the user to:

```text
┌─────────────────────────────────────────────┐
│             🤖 AI FAQ CHATBOT               │
├─────────────────────────────────────────────┤
│                                             │
│  User: How can I reset my password?         │
│                                             │
│  Bot: To reset your password, click the     │
│       "Forgot Password" option and follow   │
│       the instructions provided.            │
│                                             │
├─────────────────────────────────────────────┤
│  Type your question here...                 │
│                              [ Send ]       │
└─────────────────────────────────────────────┘
```

### Example Interaction

**👤 User:**

```text
What is your return policy?
```

**🤖 Chatbot:**

```text
Our return policy allows customers to return
eligible products within the specified return period.
```

Another example:

**👤 User:**

```text
How do I contact customer support?
```

**🤖 Chatbot:**

```text
You can contact customer support through the
support section or the provided contact information.
```

If no suitable FAQ is found:

**👤 User:**

```text
What is the weather today?
```

**🤖 Chatbot:**

```text
Sorry, I couldn't find a suitable answer to your question.
Please try asking your question in a different way.
```

> The exact chatbot responses depend on the FAQ questions and answers defined in the project's FAQ data file.

---

# 🧪 Testing the Chatbot

After launching the application, test it with different types of questions.

### Test Case 1 — Exact Question

```text
Input:
How do I reset my password?

Expected:
The chatbot returns the answer related to password resetting.
```

### Test Case 2 — Similar Question

```text
Input:
I forgot my password. What should I do?

Expected:
The chatbot should identify the password-related FAQ
and return the corresponding answer.
```

### Test Case 3 — Unrelated Question

```text
Input:
What is the capital of France?

Expected:
The chatbot should provide a fallback response if
the question is outside the FAQ knowledge base.
```

### Test Case 4 — Different Wording

```text
Input:
How can I get help from support?

Expected:
The chatbot should identify the closest matching
FAQ related to customer support.
```

---

# 🧩 Main Components

## 🤖 GUI

The GUI component is responsible for displaying the chatbot interface.

It manages:

* User input
* Chat history
* Send button
* Displaying chatbot responses
* User interaction

---

## 🧠 Chatbot Logic

The chatbot component is responsible for processing questions and finding the best FAQ match.

Its main workflow is:

```text
User Question
      ↓
Text Processing
      ↓
Similarity Calculation
      ↓
Best FAQ Match
      ↓
Retrieve Answer
      ↓
Display Response
```

---

## 📚 FAQ Data

The FAQ data component stores the questions and their corresponding answers.

For example:

```python
faqs = [
    {
        "question": "How do I reset my password?",
        "answer": "Click the Forgot Password option and follow the instructions."
    }
]
```

The chatbot uses this information as its knowledge base.

---

## 🚀 Main Program

The `main.py` file serves as the main entry point of the application.

The program is started using:

```bash
python main.py
```

It initializes the chatbot and launches the graphical user interface.

---

# 🔐 Virtual Environment

This project uses a Python virtual environment to isolate project dependencies.

The virtual environment can be created using:

```bash
python -m venv venv
```

Activate it using:

```powershell
.\venv\Scripts\Activate.ps1
```

To deactivate the environment:

```bash
deactivate
```

### ⚠️ GitHub Note

The `venv` directory should not be uploaded to GitHub.

A virtual environment is specific to the developer's computer and can be recreated using the commands above.

---

# 🌱 Future Improvements

The chatbot can be enhanced in the future by adding:

* 🎙️ Voice input
* 🔊 Text-to-speech responses
* 🌐 Web-based interface
* 🧠 More advanced NLP models
* 💾 Database-based FAQ storage
* 📊 Chat history
* 🌍 Multi-language support
* 🔄 Continuous learning
* 🤝 Integration with AI APIs
* 📱 Mobile-friendly interface

---

# 🎯 Learning Objectives

This project helped demonstrate practical concepts related to:

* Artificial Intelligence
* Natural Language Processing
* Text preprocessing
* Text similarity
* Question matching
* Chatbot development
* Python programming
* GUI development
* Software project organization

---

# 🏆 Internship Task

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship**.

### Completed Task

> **Task 2 — Chatbot for FAQs**

The project demonstrates the use of NLP techniques and similarity matching to create a simple interactive FAQ chatbot.

---

# 👨‍💻 Author

**Roshan Jadoon**

🎓 Computer Science / Computing Student

💻 Interested in Artificial Intelligence, Machine Learning, Software Development, and Data Structures & Algorithms.

---

# ⭐ Acknowledgements

Special thanks to **CodeAlpha** for providing the opportunity to work on practical Artificial Intelligence projects and gain hands-on experience in AI and Python development.

---

## 📜 License

This project was created for educational and internship purposes as part of the CodeAlpha AI Internship program.
