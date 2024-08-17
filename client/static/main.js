function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    if (userInput.value.trim() !== "") {
        const userMessage = document.createElement('div');
        userMessage.className = 'message user-message';
        userMessage.textContent = userInput.value;
        chatBox.appendChild(userMessage);

        // Send the message to the backend
        fetch('send_message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken(),
            },
            body: JSON.stringify({ message: userInput.value }),
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('div');
            botMessage.className = 'message bot-message';
            botMessage.textContent = data.reply;
            chatBox.appendChild(botMessage);
        });

        userInput.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function getCSRFToken() {
    const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfToken) {
        return csrfToken.split('=')[1];
    }
    return '';
}
