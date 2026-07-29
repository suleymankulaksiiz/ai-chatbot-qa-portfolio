function login() {

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;


    if (email === "" || password === "") {

        alert("Email and password are required");

        return;
    }


    window.location.href = "/chat.html";
}



function sendMessage() {

    const message =
        document.getElementById("message").value;


    const chatBox =
        document.getElementById("chatBox");


    if (message === "") {
        alert("Please enter a message");
        return;
    }


    chatBox.innerHTML +=
        `<p>User: ${message}</p>`;


    chatBox.innerHTML +=
        `<p>Bot: Thanks for your message!</p>`;


    document.getElementById("message").value = "";
}