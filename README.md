# ChatBot
#### an AI chatbot based on Gemini 2.5 Flash
#### created by Ishaan Jog

---

## Direct usage
You can visit [iamchatbot.streamlit.app] to directly access ChatBot.

---

## Developer installation

1. **Download the source code.**
2. **Install the requirements**

   ```
   $ pip install -r requirements.txt
   ```
3. **Add Your API Key**

    1. **Get your API key:**  
    Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and generate your own Gemini API key.

    2. **Set the environment variable:**  
    Set the key as an environment variable named `GOOGLE_API_KEY` on your system.

        > 🔽 Need help? Check the steps below for setting environment variables on **Windows**, **macOS**, and **Linux**.

4. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

---

## Setting API Key Environment Variable

### 🪟 Windows

**Temporarily (Command Prompt or PowerShell):**
```cmd
set GOOGLE_API_KEY=your-api-key-here
```

**Permanently (System Settings):**
1. Search for **"Environment Variables"** in the Start menu.
2. Click **"Edit the system environment variables"**.
3. In the System Properties window, click **"Environment Variables..."**.
4. Under **User variables**, click **"New..."**.
5. Set:
   - **Variable name:** `GOOGLE_API_KEY`
   - **Variable value:** your API key
6. Click OK and restart your terminal.

---

### 🍎 macOS

**Temporarily (Terminal):**
```bash
export GOOGLE_API_KEY=your-api-key-here
```

**Permanently:**
1. Open your shell configuration file:
   - For bash: `~/.bash_profile`
   - For zsh: `~/.zshrc`
2. Add this line at the end:
   ```bash
   export GOOGLE_API_KEY=your-api-key-here
   ```
3. Save the file and run:
   ```bash
   source ~/.bash_profile   # or ~/.zshrc
   ```

---

### 🐧 Linux

Same as macOS. Use `~/.bashrc` or `~/.zshrc` based on your shell.

**Temporarily:**
```bash
export GOOGLE_API_KEY=your-api-key-here
```

**Permanently:**
1. Open your shell config file (e.g. `~/.bashrc`)
2. Add:
   ```bash
   export GOOGLE_API_KEY=your-api-key-here
   ```
3. Save and run:
   ```bash
   source ~/.bashrc
   ```

---

Hope you have a delightful experience!
