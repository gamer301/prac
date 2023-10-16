document.addEventListener("DOMContentLoaded", function () {
    const display = document.getElementById("display");
    const buttons = document.querySelectorAll("button");
    

    let currentInput = "";
    let operator = "";
    let firstOperand = "";
    let secondOperand = "";
    let result = "";

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const buttonText = button.textContent;

            if (buttonText === "C") {
                clear();
            } else if (buttonText === "=") {
                calculate();
            } else if (buttonText === "&#9003;") {
                backspace();
            } else if (button.classList.contains("operator")) {
                handleOperator(buttonText);
            } else {
                currentInput += buttonText;
                updateDisplay();
            }
        });
    });

    document.body.style.backgroundImage ="url('https://source.unsplash.com/1600x900/?book')";


    function clear() {
        currentInput = "";
        operator = "";
        firstOperand = "";
        secondOperand = "";
        result = "";
        updateDisplay();
    }

    function calculate() {
        if (firstOperand && operator && currentInput) {
            secondOperand = currentInput;
            switch (operator) {
                case "+":
                    result = parseFloat(firstOperand) + parseFloat(secondOperand);
                    break;
                case "-":
                    result = parseFloat(firstOperand) - parseFloat(secondOperand);
                    break;
                case "*":
                    result = parseFloat(firstOperand) * parseFloat(secondOperand);
                    break;
                case "/":
                    result = parseFloat(firstOperand) / parseFloat(secondOperand);
                    break;
            }
            currentInput = result.toString();
            operator = "";
            firstOperand = "";
            secondOperand = "";
            updateDisplay();
        }
    }

    function backspace() {
        currentInput = currentInput.slice(0, -1);
        updateDisplay();
    }

    function handleOperator(op) {
        if (currentInput) {
            firstOperand = currentInput;
            operator = op;
            currentInput = "";
            updateDisplay();
        }
    }

    function updateDisplay() {
        display.value = currentInput || "0";
    }
});
