// ! Имитация написания инпута

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

//
//
//! Имитация нажатия мыши (CLICK!)
// ! Помимо простого click() здесь на сам элемент наводится (hover) что меняет стили если есть псевдо-элемент
// ! Дальше еще к всему этому надается focus(), что дадает классы если есть псевдоэлемент (focus) и только потом нажимается.
// ! Что имитирует максимальный клик, так как всегда сначала идет hover потом focus (зажим кнопки) и только потом событие клик
// ! Очень помогло на сайте https://www.google.com/alerts так как там все события эти меняли класс и без них невохможно было кликнуть.

try {
  let el = document.querySelector("#create_alert");
  if (el) {
    // Прокрутка к элементу
    el.scrollIntoView();

    // Наведение на элемент (симуляция mouseover)
    let mouseOverEvent = new MouseEvent("mouseover", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    el.dispatchEvent(mouseOverEvent);

    // Симуляция зажатия кнопки мыши (focus через mousedown)
    let mouseDownEvent = new MouseEvent("mousedown", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    el.dispatchEvent(mouseDownEvent);

    // Симуляция клика (mouseup + click)
    let mouseUpEvent = new MouseEvent("mouseup", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    el.dispatchEvent(mouseUpEvent);

    let clickEvent = new MouseEvent("click", {
      bubbles: true,
      cancelable: true,
      view: window,
    });
    el.dispatchEvent(clickEvent);

    console.log("Hovered, focused (mousedown), and clicked!");
  } else {
    console.log("Element not found!");
  }
} catch (error) {
  console.error("Ошибка при клике:", error);
}
