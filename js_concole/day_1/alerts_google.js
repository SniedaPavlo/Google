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

(function () {
  "use strict";

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
    console.error("Ошибка при выполнении кода:", error);
  }

  //
  //
  //Работаем с инпутом
  //
  //
  //

  try {
    // Определяем XPath для поиска input элемента
    const inputXpath = "//*[@id='query_div']/input";
    // Определяем XPath для кнопки создания оповещения
    const alertButtonXpath = "//*[@id='create_alert']";

    // Функция для получения элемента по XPath
    function getElementByXPath(xpathExpression) {
      const result = document.evaluate(
        xpathExpression,
        document,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null
      );
      return result.singleNodeValue;
    }

    // Функция для имитации ввода текста с естественными задержками между буквами
    function typeText(element, text, callback) {
      let i = 0;
      const typeNextLetter = () => {
        element.value += text[i];
        i++;
        if (i < text.length) {
          // Случайная задержка от 100 до 200 мс между буквами
          const delay = Math.random() * 100 + 100;
          setTimeout(typeNextLetter, delay);
        } else {
          callback(); // Завершение ввода, вызываем callback
        }
      };
      typeNextLetter();
    }

    // Функция для имитации нажатия клавиши Enter
    function pressEnter(element) {
      const event = new KeyboardEvent("keydown", {
        key: "Enter",
        code: "Enter",
        keyCode: 13,
        which: 13,
        bubbles: true,
      });
      element.dispatchEvent(event);
      console.log("Нажата клавиша Enter");
    }

    // Получаем input элемент
    const inputElement = getElementByXPath(inputXpath);
    const alertButton = getElementByXPath(alertButtonXpath);

    if (inputElement && alertButton) {
      console.log("Найден input элемент");

      // Имитация ввода текста "sport" с случайными задержками между буквами
      typeText(inputElement, "sport", () => {
        console.log('Текст "sport" введен');

        // Нажимаем Enter после ввода текста
        pressEnter(inputElement);

        // Кликаем по кнопке создания оповещения
        alertButton.click();
        console.log("Нажата кнопка создания оповещения");
      });
    } else {
      console.log("Не найден input элемент или кнопка создания оповещения");
    }
  } catch (error) {
    console.error("Ошибка при выполнении кода:", error);
  }
})();
