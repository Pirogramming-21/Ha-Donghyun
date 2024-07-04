document.addEventListener("DOMContentLoaded", (event) => {
    initializeGame();
});

let attempts;
let answer;

// 게임 초기화
function initializeGame() {
    attempts = 10;
    answer = generateUniqueNumbers();
    clearInputs();
    clearResults();
    document.getElementById("game-result-img").src = "";
    document.querySelector(".submit-button").disabled = false;
}

function generateUniqueNumbers() {
    let numbers = [];
    while (numbers.length < 3) {
        let num = Math.floor(Math.random() * 10);
        if (!numbers.includes(num)) {
            numbers.push(num);
        }
    }
    return numbers;
}

function clearInputs() {
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
}

function clearResults() {
    document.querySelector(".result-display").innerHTML = "";
}

// 숫자 확인
function check_numbers() {
    let num1 = document.getElementById("number1").value;
    let num2 = document.getElementById("number2").value;
    let num3 = document.getElementById("number3").value;

    if (num1 === "" || num2 === "" || num3 === "") {
        clearInputs();
        return;
    }

    let userNumbers = [parseInt(num1), parseInt(num2), parseInt(num3)];
    let result = getResult(userNumbers);

    updateResults(userNumbers, result);
    attempts--;

    if (result.strike === 3) {
        endGame(true);
    } else if (attempts <= 0) {
        endGame(false);
    } else {
        clearInputs();
    }
}

function getResult(userNumbers) {
    let strike = 0;
    let ball = 0;

    userNumbers.forEach((num, index) => {
        if (num === answer[index]) {
            strike++;
        } else if (answer.includes(num)) {
            ball++;
        }
    });

    return { strike, ball };
}

function updateResults(userNumbers, result) {
    let resultDisplay = document.querySelector(".result-display");
    let resultDiv = document.createElement("div");
    resultDiv.className = "check-result";

    let leftDiv = document.createElement("div");
    leftDiv.className = "left";
    leftDiv.textContent = userNumbers.join(" ");

    let rightDiv = document.createElement("div");
    rightDiv.className = "right";

    if (result.strike === 0 && result.ball === 0) {
        let outDiv = document.createElement("div");
        outDiv.className = "out num-result";
        outDiv.textContent = "O";
        rightDiv.appendChild(outDiv);
    } else {
        if (result.strike > 0) {
            let strikeDiv = document.createElement("div");
            strikeDiv.className = "strike num-result";
            strikeDiv.textContent = `${result.strike} S`;
            rightDiv.appendChild(strikeDiv);
        }
        if (result.ball > 0) {
            let ballDiv = document.createElement("div");
            ballDiv.className = "ball num-result";
            ballDiv.textContent = `${result.ball} B`;
            rightDiv.appendChild(ballDiv);
        }
    }

    resultDiv.appendChild(leftDiv);
    resultDiv.appendChild(rightDiv);
    resultDisplay.appendChild(resultDiv);
}

function endGame(isWin) {
    let resultImg = document.getElementById("game-result-img");
    if (isWin) {
        resultImg.src = "success.png";
    } else {
        resultImg.src = "fail.png";
    }
    document.querySelector(".submit-button").disabled = true;
}