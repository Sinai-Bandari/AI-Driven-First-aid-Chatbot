document.getElementById("chat-form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const userInput = document.getElementById("user-input");
  const userText = userInput.value.trim();
  const lang = document.getElementById("language").value;
  if (!userText) return;

  appendMessage(userText, "user");
  userInput.value = "";

  showTyping(true);

  const response = await fetch("/get_response", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `user_query=${encodeURIComponent(userText)}&lang=${lang}`,
  });

  const data = await response.json();
  showTyping(false);
  appendMessage(data.response, "bot");
});

function appendMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);

  const avatar = document.createElement("img");
  avatar.classList.add("avatar");
  avatar.src = sender === "user"
    ? "https://img.icons8.com/ios-filled/36/user-male-circle.png"
    : "https://img.icons8.com/color/36/bot.png";

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");
  bubble.innerHTML = `${text}<div class="timestamp">${new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}</div>`;

  messageDiv.appendChild(sender === "user" ? bubble : avatar);
  messageDiv.appendChild(sender === "user" ? avatar : bubble);

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function toggleDarkMode() {
  document.body.classList.toggle("dark");
}

function startVoiceInput() {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Speech recognition not supported in this browser.");
    return;
  }

  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.onresult = function (event) {
    document.getElementById("user-input").value = event.results[0][0].transcript;
  };
  recognition.start();
}

function showTyping(show) {
  const typing = document.getElementById("typing-indicator");
  typing.classList.toggle("show", show);
}