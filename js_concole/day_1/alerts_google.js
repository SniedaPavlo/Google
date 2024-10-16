// ==UserScript==
// @name         Open Search Tabs and Click Links
// @namespace    http://tampermonkey.net/
// @version      2024-10-15
// @description  Открыть вкладки с поиском и отправить GET запросы на ссылки с официальными хостами
// @author       You
// @match        https://www.google.com/alerts
// @icon         https://www.google.com/s2/favicons?sz=64&domain=google.com
// @grant        none
// ==/UserScript==

(async function () {
  "use strict";

  //   Функция явного ожидания
  function wait(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  try {
    // Определяем XPath для поиска всех элементов с классом "alert_button create_button"
    const xpath =
      "//*[contains(@class, 'alert_button') and contains(@class, 'create_button')]";

    // Функция для получения всех элементов по XPath
    function getElementsByXPath(xpathExpression) {
      const result = [];
      const querySnapshot = document.evaluate(
        xpathExpression,
        document,
        null,
        XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
        null
      );
      for (let i = 0; i < querySnapshot.snapshotLength; i++) {
        result.push(querySnapshot.snapshotItem(i));
      }
      return result;
    }

    // Получаем все элементы по заданному XPath
    const alertButtons = getElementsByXPath(xpath);

    console.log(`Найдено ${alertButtons.length} кнопок`);

    // Проверяем, есть ли найденные элементы
    if (alertButtons.length > 0) {
      // Циклически кликаем по каждому элементу
      let i = 0;
      const interval = setInterval(() => {
        if (i < alertButtons.length) {
          alertButtons[i].click();
          console.log(`Клик по элементу ${i + 1}`);
          i++;
        } else {
          clearInterval(interval); // После кликов останавливаем интервал
          console.log("Все кнопки обработаны.");
        }
      }, 1000); // Кликаем каждые 1 секунду
    } else {
      console.log("Кнопки не найдены.");
    }
  } catch (error) {
    console.error("Ошибка при кнопках (плюс):", error);
  }

  //
  //
  // ! Работаем с инпутом
  //
  //
  //
  await wait(2000); // Используем await для ожидания
  console.log("Прошло 2 секунды ожидания");

  try {
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
    await simulateTyping(inputElement, "sport", 150); // Имитируем набор текста с задержкой 150 мс между символами
    simulateCtrlC(); // После ввода текста выполняем Ctrl + C
  } catch (error) {
    console.error("Ошибка при выполнении кода:", error);
  }

  //
  //
  //
  //! Нажатие на "Добавить" после инпута имитируя максимально клик. Сначала hover для смены классов, потом focus и только потом клик!
  //
  //
  //
  await wait(2000); // Используем await для ожидания
  console.log("Прошло 2 секунды ожидания");

  try {
    let btn_add = document.querySelector("#create_alert");
    if (btn_add) {
      // Прокрутка к элементу
      btn_add.scrollIntoView();

      // Наведение на элемент (симуляция mouseover)
      let mouseOverEvent = new MouseEvent("mouseover", {
        bubbles: true,
        cancelable: true,
        view: window,
      });
      btn_add.dispatchEvent(mouseOverEvent);

      // Симуляция зажатия кнопки мыши (focus через mousedown)
      let mouseDownEvent = new MouseEvent("mousedown", {
        bubbles: true,
        cancelable: true,
        view: window,
      });
      btn_add.dispatchEvent(mouseDownEvent);

      // Симуляция клика (mouseup + click)
      let mouseUpEvent = new MouseEvent("mouseup", {
        bubbles: true,
        cancelable: true,
        view: window,
      });
      btn_add.dispatchEvent(mouseUpEvent);

      let clickEvent = new MouseEvent("click", {
        bubbles: true,
        cancelable: true,
        view: window,
      });
      btn_add.dispatchEvent(clickEvent);

      console.log("Hovered, focused (mousedown), and clicked!");
    } else {
      console.log("Element not found!");
    }
  } catch (error) {
    console.error("Ошибка при клике:", error);
  }
})();
