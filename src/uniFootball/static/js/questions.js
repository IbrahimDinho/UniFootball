// const question = document.getElementById("question");
// const choices = Array.from(document.getElementsByClassName("choice-text"));
// const progressText = document.getElementById("progressText");
// const scoreText = document.getElementById("score");
// let currentQuestion = {};
// let acceptingAnswers = false;
// let score = 0;
// let questionCounter = 0;
// let availableQuesions = [];

// let questions = [];

// fetch(
//   //"https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=multiple"
//   fetch("questions.json")
// )
//   .then((res) => {
//     return res.json();
//   })
//   .then((loadedQuestions) => {
//     questions = loadedQuestions.results.map((loadedQuestion) => {
//       const formattedQuestion = {
//         question: loadedQuestion.question,
//       };

//       const answerChoices = [...loadedQuestion.incorrect_answers];
//       formattedQuestion.answer = Math.floor(Math.random() * 4) + 1;
//       answerChoices.splice(
//         formattedQuestion.answer - 1,
//         0,
//         loadedQuestion.correct_answer
//       );

//       answerChoices.forEach((choice, index) => {
//         formattedQuestion["choice" + (index + 1)] = choice;
//       });

//       return formattedQuestion;
//     });
//     startGame();
//   })
//   .catch((err) => {
//     console.error(err);
//   });

// //CONSTANTS
// const CORRECT_BONUS = 1;
// const MAX_QUESTIONS = 5;

// let startGame = () => {
//   questionCounter = 0;
//   score = 0;
//   availableQuesions = [...questions];
//   getNewQuestion();
// };

// let getNewQuestion = () => {
//   if (availableQuesions.length === 0 || questionCounter >= MAX_QUESTIONS) {
//     //one finished set score in localstorage and go to end page.
//     localStorage.setItem("mostRecentScore", score);
//     return window.location.assign("finishquiz.html");
//   }
//   //update question counter
//   questionCounter++;
//   progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;

//   //new question
//   const questionIndex = Math.floor(Math.random() * availableQuesions.length);
//   currentQuestion = availableQuesions[questionIndex];
//   question.innerText = convert(`${currentQuestion.question}`);

//   choices.forEach((choice) => {
//     const number = choice.dataset["number"];
//     choice.innerText = convert(`${currentQuestion["choice" + number]}`);
//   });

//   availableQuesions.splice(questionIndex, 1);
//   acceptingAnswers = true;
// };

// choices.forEach((choice) => {
//   choice.addEventListener("click", (e) => {
//     if (!acceptingAnswers) return;

//     acceptingAnswers = false;
//     const selectedChoice = e.target;
//     const selectedAnswer = selectedChoice.dataset["number"];

//     const classToApply =
//       selectedAnswer == currentQuestion.answer ? "correct" : "incorrect";

//     if (classToApply === "correct") {
//       incrementScore(CORRECT_BONUS);
//     }
//     // feedback green if correct otherwie red. through css.
//     selectedChoice.parentElement.classList.add(classToApply);

//     setTimeout(() => {
//       selectedChoice.parentElement.classList.remove(classToApply);
//       getNewQuestion();
//     }, 2000);
//   });
// });

// let incrementScore = (num) => {
//   score += num;
//   scoreText.innerText = score;
// };
// // deal with &039 error &quote where it show that that instead of apastrophe
// //doesnt deal with different lanage like e with dot ontop.
// function convert(string) {
//   return string.replace(/&#(?:x([\da-f]+)|(\d+));/gi, function (_, hex, dec) {
//     return String.fromCharCode(dec || +("0x" + hex));
//   });
// }

const question = document.getElementById("question");
const choices = Array.from(document.getElementsByClassName("choice-text"));
const progressText = document.getElementById("progressText");
const scoreText = document.getElementById("score");
let currentQuestion = {};
let acceptingAnswers = false;
let score = 0;
let questionCounter = 0;
let availableQuesions = [];

let questions = [];

fetch("questions.json")
  .then((res) => {
    return res.json();
  })
  .then((loadedQuestions) => {
    questions = loadedQuestions;
    startGame();
  })
  .catch((err) => {
    console.error(err);
  });

//CONSTANTS
const CORRECT_BONUS = 1;
const MAX_QUESTIONS = 5;

let startGame = () => {
  questionCounter = 0;
  score = 0;
  availableQuesions = [...questions];
  getNewQuestion();
};

let getNewQuestion = () => {
  if (availableQuesions.length === 0 || questionCounter >= MAX_QUESTIONS) {
    localStorage.setItem("mostRecentScore", score);
    //go to the end page
    return window.location.assign("finishquiz.html");
  }
  questionCounter++;
  progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;

  const questionIndex = Math.floor(Math.random() * availableQuesions.length);
  currentQuestion = availableQuesions[questionIndex];
  question.innerText = currentQuestion.question;

  choices.forEach((choice) => {
    const number = choice.dataset["number"];
    choice.innerText = currentQuestion["choice" + number];
  });

  availableQuesions.splice(questionIndex, 1);
  acceptingAnswers = true;
};

choices.forEach((choice) => {
  choice.addEventListener("click", (e) => {
    if (!acceptingAnswers) return;

    acceptingAnswers = false;
    const selectedChoice = e.target;
    const selectedAnswer = selectedChoice.dataset["number"];

    const classToApply =
      selectedAnswer == currentQuestion.answer ? "correct" : "incorrect";

    if (classToApply === "correct") {
      incrementScore(CORRECT_BONUS);
    }

    selectedChoice.parentElement.classList.add(classToApply);

    setTimeout(() => {
      selectedChoice.parentElement.classList.remove(classToApply);
      getNewQuestion();
    }, 2000);
  });
});

let incrementScore = (num) => {
  score += num;
  scoreText.innerText = score;
};
