fetch("http://127.0.0.1:5000/scan_email", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ email_text: "Suspicious email content" })
})
.then(response => response.json())
.then(data => console.log("API Response:", data))
.catch(error => console.error("Error:", error));
