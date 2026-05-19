async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();

    if (message === "") {
        return;
    }

    let chatBox = document.getElementById("chat-box");

    let userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    input.value = "";

    let botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = "Thinking...";
    chatBox.appendChild(botDiv);

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();
        botDiv.innerText = data.reply;

    } catch (error) {
        botDiv.innerText = "Frontend Error: " + error;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}