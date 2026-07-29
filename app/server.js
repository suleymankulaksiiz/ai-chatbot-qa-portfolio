const express = require("express");

const app = express();

const PORT = 3000;


app.use(express.json());

app.use(express.static("public"));


// Health check API
app.get("/api/health", (req, res) => {

    res.json({
        status: "ok",
        message: "Chatbot API is running"
    });

});


// Chat API
app.post("/api/chat", (req, res) => {

    const { message } = req.body;


    if(!message || message.trim() === "") {

        return res.status(400).json({

            error: "Message is required"

        });

    }


    res.json({

        reply: `You said: ${message}`

    });

});


app.listen(PORT, () => {

    console.log(
        `Server running on http://localhost:${PORT}`
    );

});