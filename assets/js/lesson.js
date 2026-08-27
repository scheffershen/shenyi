"use strict";

(function () {
  function initializeQuiz(quiz) {
    var options = Array.prototype.slice.call(quiz.querySelectorAll("button[data-answer]"));
    var feedback = quiz.querySelector(".lesson-feedback[data-feedback]");

    if (!feedback || options.length < 2) {
      return;
    }

    feedback.setAttribute("aria-live", "polite");

    options.forEach(function (option) {
      option.addEventListener("click", function () {
        var isCorrect = option.dataset.answer === "correct";

        options.forEach(function (otherOption) {
          otherOption.disabled = true;
          otherOption.setAttribute("aria-pressed", String(otherOption === option));
        });

        option.classList.add(isCorrect ? "is-correct" : "is-incorrect");
        feedback.classList.remove("is-correct", "is-incorrect");
        feedback.classList.add(isCorrect ? "is-correct" : "is-incorrect");
        feedback.textContent = option.dataset.feedback || (isCorrect ? "Correct." : "Not quite.");
      });
    });
  }

  function initializeLessons() {
    document.querySelectorAll("[data-quiz]").forEach(initializeQuiz);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeLessons);
  } else {
    initializeLessons();
  }
}());
