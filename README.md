
# 🤖 Chatbot API Using Gemini Pro (First Aid Assistant)

## 📌 Project Overview
This project is a Flask-based chatbot API that leverages **Gemini Pro (Google AI)** to provide **first aid assistance**.  
Users can interact through a simple web interface, and the chatbot responds in real-time with helpful advice.

## 🛠 Technologies Used
- **Python** (Flask, Google Generative AI SDK, dotenv)
- **Flask-CORS** (for cross-origin requests)
- **HTML, CSS** (basic frontend via `index.html`)
- **Git & GitHub** (for version control)

## 📂 Project Structure
```

chatbot-api/
│── templates/
│   └── index.html           # Frontend interface
│── app.py                   # Main Flask app
│── requirements.txt         # Python dependencies
│── .env                     # API key environment file (not included in repo)
│── README.md                # Project documentation

````

## 💡 Workflow
1. **User sends a message** through the web interface  
2. **Flask API** receives and forwards it to Gemini Pro  
3. **Gemini API** generates a helpful response  
4. **Response is returned** to the user in real-time

---

## 📥 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/chatbot-api.git
cd chatbot-api
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file in the root directory and add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ⚡ Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📡 API Endpoint

### POST `/chat`

**Request:**

```json
{
  "message": "What should I do if someone faints?"
}
```

**Response:**

```json
{
  "reply": "If someone faints, lay them down and raise their legs. Check their breathing and stay calm..."
}
```

---

## 💬 Example Use Case

* Input: "What should I do if someone gets a minor burn?"
* Output: "For minor burns, run cool water over the area for 10-15 minutes and cover with a sterile bandage."

---

## 📷 Screenshots
<img width="1028" height="730" alt="Screenshot 2025-04-12 033545" src="https://github.com/user-attachments/assets/faed1924-a36d-48a3-b540-660cd43c6e47" />
<img width="1075" height="988" alt="Screenshot 2025-04-10 220052" src="https://github.com/user-attachments/assets/69b757e1-86d7-48b2-84c3-ddcb4f90e72b" />
<img width="1877" height="920" alt="Screenshot 2025-04-10 220440" src="https://github.com/user-attachments/assets/26a41bf9-bdd2-4bf1-9a19-ff80aeebea5d" />




---

## 📜 License

This project is licensed under the **MIT License**.

---

### 👤 Author

**Sinai Bandari** – [Your GitHub Profile](https://github.com/Sinai-Bandari)

```

