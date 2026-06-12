function checkQuiz() {
  const resultDiv = document.getElementById("quiz-result");
  const q1Answer = document.querySelector('input[name="q1"]:checked');

  resultDiv.classList.remove("hidden", "correct", "incorrect");

  if (!q1Answer) {
    resultDiv.textContent = "Please select an answer.";
    resultDiv.classList.add("incorrect");
    return;
  }

  if (q1Answer.value === "correct") {
    resultDiv.textContent =
      "Correct! This is a classic social engineering tactic known as CEO Fraud. Always verify out-of-character requests through a secondary communication channel.";
    resultDiv.classList.add("correct");
  } else if (q1Answer.value === "buyCards") {
    resultDiv.textContent =
      "Incorrect. Never act on urgent financial requests without verifying them first. Buying gift cards is a common gift card scam tactic and no legitimate CEO will ask for this.";
    resultDiv.classList.add("incorrect");
  } else {
    resultDiv.textContent =
      "Incorrect. Replying to the email just talks to the scammer. Always use a secondary method, like a phone call, to verify urgent financial requests.";
    resultDiv.classList.add("incorrect");
  }
}
