//

// Получаем элемент с помощью XPath
const inputElement = document.evaluate(
  '//*[@id="query_div"]/input',
  document,
  null,
  XPathResult.FIRST_ORDERED_NODE_TYPE,
  null
).singleNodeValue;

// Функция для имитации клика на элементе
function simulateClick(element) {
  const mouseEvent = new MouseEvent("click", {
    bubbles: true,
    cancelable: true,
    view: window,
  });
  element.dispatchEvent(mouseEvent);
}

// Функция для имитации нажатия клавиш Ctrl + C
function simulateCtrlC() {
  const ctrlCEvent = new KeyboardEvent("keydown", {
    key: "c",
    ctrlKey: true,
    bubbles: true,
    cancelable: true,
  });
  document.dispatchEvent(ctrlCEvent);
}

// Функция для имитации набора текста с задержкой
async function simulateTyping(element, text, delay) {
  // Устанавливаем фокус на элементе
  element.focus();

  for (const char of text) {
    // Создаем событие 'keydown' для каждого символа
    const keydownEvent = new KeyboardEvent("keydown", {
      key: char,
      bubbles: true,
      cancelable: true,
    });

    // Отправляем событие 'keydown'
    element.dispatchEvent(keydownEvent);

    // Обновляем значение элемента
    element.value += char;
    element.dispatchEvent(new Event("input", { bubbles: true }));

    // Ожидаем перед отправкой следующего символа
    await new Promise((resolve) => setTimeout(resolve, delay));
  }

  // Отправляем 'keyup' для последнего символа
  const keyupEvent = new KeyboardEvent("keyup", {
    key: text[text.length - 1],
    bubbles: true,
    cancelable: true,
  });
  element.dispatchEvent(keyupEvent);
}

// Выполняем последовательность действий
simulateClick(inputElement); // Имитируем клик
simulateTyping(inputElement, "sport", 150) // Имитируем набор текста с задержкой 150 мс между символами
  .then(() => simulateCtrlC()); // После ввода текста выполняем Ctrl + C
