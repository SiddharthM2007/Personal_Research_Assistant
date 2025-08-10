// Grab the DOM elements
const input = document.getElementById("question");
const btn = document.getElementById("askBtn");
const out = document.getElementById("response");

// When the button is clicked, run ask()
btn.addEventListener("click", ask);

async function ask() {
  const question = (input.value || "").trim();

  // Guard: don't send empty requests
  if (!question) {
    out.textContent = "Please enter a topic.";
    return;
  }

  // Show a temporary status
  out.textContent = "Thinking...";

  try {
    // POST JSON to the Flask endpoint /ask
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })  // <- JSON body
    });

    // Parse JSON back from Flask
    const data = await res.json();

    // Show either the answer or an error
    out.textContent = data.answer || data.error || "No response.";
  } catch (err) {
    console.error(err);
    out.textContent = "Error talking to the server.";
  }
}
