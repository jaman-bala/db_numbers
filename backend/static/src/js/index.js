document.addEventListener("DOMContentLoaded", function () {
    const numberExistsMessage = document.getElementById("number-exists-message");

    // Функция для отправки запроса на сервер
    function checkNumberExists(number) {
        fetch(`/check_number_exists?number=${number}`)
            .then(response => response.json())
            .then(data => {
                if (data.exists) {
                    numberExistsMessage.innerText = "Номер уже существует";
                } else {
                    numberExistsMessage.innerText = "";
                }
            })
            .catch(error => {
                console.error("Error checking number exists:", error);
            });
    }

    // Вызов функции checkNumberExists при загрузке страницы
    const numberInput = document.getElementById("id_number");
    if (numberInput) {
        checkNumberExists(numberInput.value.trim()); // Вызываем функцию с текущим значением поля
    }

    // Слушатель события ввода номера пользователем
    if (numberInput) {
        numberInput.addEventListener("input", function () {
            const number = numberInput.value.trim();
            if (number !== "") {
                checkNumberExists(number);
            } else {
                numberExistsMessage.innerText = "";
            }
        });
    }
});