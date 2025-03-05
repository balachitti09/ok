console.log("Phishing Detection Background Script Running");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "scan_email") {
        console.log("Received email for scanning:", message.text);

        // Send email text to Flask API
        fetch("http://127.0.0.1:5000/detect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: message.text }),
            
        })
        .then(response => response.json())
        .then(data => {
            console.log("Phishing Detection API Response:", data);
            
            // Send result back to content script
            chrome.runtime.sendMessage({ action: "scan_result", result: data.result });
        })
        .catch(error => console.error("API Error:", error));
    }
});
