# AI Code & Filesystem Managment System

A lightweight autonomous AI agent capable of inspecting a workspace, reading and writing files, executing Python code, and iterating through tool calls using Gemini 2.5 Flash’s function-calling capabilities.

This project demonstrates how to build a multi-step AI agent that performs real operations inside a local project directory — including debugging, file inspection, and automated code modification.

---

## 🚀 Features

### 🔍 Filesystem Inspection
- List directory contents  
- Retrieve file metadata (size, type, etc.)  
- Explore folder structures  

### 📄 File Content Access
- Read file content securely  
- Prevent access outside working directory  

### ✏️ File Writing & Modification
- Overwrite existing files  
- Create new files  
- Enable the agent to fix or rewrite code  

### 🐍 Python Execution
- Execute Python scripts inside the workspace  
- Return stdout and stderr for debugging  
- Validate changes through iterative execution  

### 🔁 Iterative Agent Loop
- Multi-step reasoning with memory  
- Function call → tool → result → next step  
- Up to 20 autonomous iterations  
- Stops when the model returns a final answer  

---

## 🧠 How It Works

1. User gives a natural-language prompt.  
2. The agent calls Gemini with:
   - System instructions  
   - Entire message history  
   - Available tool definitions  
3. Gemini decides whether to call a function.  
4. The requested Python tool executes locally.  
5. The tool output is appended as a new message.  
6. Gemini uses the new context to plan the next step.

The loop continues until the model returns a final, non–function-calling response.

User → Model → Function Call → Tool Result → Model → …


---

## 📁 Project Structure



youssef_ai/
│
├── main.py # Entry point and agent loop
├── prompts.py # System prompt definition
│
├── functions/
│ ├── function_calling.py # Central function call handler
│ ├── get_files_info.py # Directory listing tool
│ ├── get_file_content.py # File reader tool
│ ├── write_file.py # File writing tool
│ └── run_python_file.py # Python execution tool
│
├── calculator/ # Example project for the agent to operate on
│
└── .env # Gemini API key


---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd youssef_ai

2. Install dependencies
pip install -r requirements.txt

3. Add your Gemini API Key

Create a .env file:

GEMINI_API_KEY=your_key_here

4. Run the agent
uv run main.py "Fix the bug in the calculator"

🧪 Example Commands
List files
uv run main.py "List the files in the root"

Read a file
uv run main.py "Show me the contents of tests.py"

Debug automatically
uv run main.py "Find and fix bugs in the project"

🔒 Safety

Tools restricted to working directory

Path validation prevents directory traversal

Write operations allowed only when invoked by tool calls

Python execution isolated to controlled environment

📌 Roadmap

Multi-file reasoning

Static analysis tools

Git integration

Plugin-based tools

REPL execution mode

📜 License

MIT License (adjust as needed).


If you want, I can also generate:  
🔥 a **GitHub-ready description**,  
🔥 a **project logo**,  
🔥 a **professional tagline**,  
🔥 or convert this into a **powered-by-Gemini badge**.