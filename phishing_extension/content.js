console.log("Phishing Detection Content Script Loaded");

// Function to extract email content from Gmail
function scanEmails() {
    let emailBody = document.querySelector(".adn .a3s"); // Gmail's email body container
    if (emailBody) {
        let emailText = emailBody.innerText || emailBody.textContent;
        console.log("Extracted Email:", emailText);

        // Send the email text to background.js
        chrome.runtime.sendMessage({ action: "scan_email", text: emailText });
    }
}

// Use MutationObserver to detect changes in the Gmail page
const observer = new MutationObserver((mutations, obs) => {
    for (let mutation of mutations) {
        if (mutation.type === "childList" || mutation.type === "subtree") {
            scanEmails();  // Run scanning when new content appears
        }
    }
});

// Observe Gmail's email container for updates
const targetNode = document.body;
const observerConfig = { childList: true, subtree: true };

// Start observing changes in the email page
observer.observe(targetNode, observerConfig);

console.log("MutationObserver started for email scanning.");
