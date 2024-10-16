// ==UserScript==
// @name          news.google.com
// @namespace    http://tampermonkey.net/
// @version      2024-10-15
// @description  Добавляет интересы в google alerts
// @author       You
// @match        https://news.google.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=google.com
// @grant        none
// ==/UserScript==

(async function () {
  "use strict";

  // Функция явного ожидания
  function wait(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  // Асинхронная функция для ожидания появления элемента по XPath и клика по нему
  async function AsyncClickElementByXPath(xpath, timeout = 10000) {
    // Ожидание элемента по XPath
    const element = await waitForElement(xpath, timeout);

    // Если элемент найден, имитируем клик
    if (element) {
      // Имитируем hover (наведение курсора)
      const hoverEvent = new MouseEvent("mouseover", {
        bubbles: true,
        cancelable: true,
        view: window,
      });
      element.dispatchEvent(hoverEvent);

      // Имитируем focus (получение фокуса)
      element.focus();

      // Имитируем клик
      const mouseEvent = new MouseEvent("click", {
        bubbles: true,
        cancelable: true,
        view: window,
      });

      // Имитируем клик по элементу
      element.dispatchEvent(mouseEvent);
      console.log(`Клик по элементу с XPath: ${xpath}`);
      return true; // Возвращаем true, если клик успешен
    }
    return false; // Возвращаем false, если элемент не найден
  }

  // Асинхронная функция для ожидания появления элемента по XPath
  async function waitForElement(xpath, timeout = 2000) {
    const startTime = Date.now();

    while (Date.now() - startTime < timeout) {
      const xpathResult = document.evaluate(
        xpath,
        document,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null
      );
      const element = xpathResult.singleNodeValue;

      if (element) {
        return element; // Элемент найден
      }

      await new Promise((resolve) => setTimeout(resolve, 50)); // Ждём 50ms перед следующим поиском
    }

    throw new Error(
      `Элемент с XPath ${xpath} не найден за ${timeout / 1000} секунд`
    );
  }

  // Получаем все элементы с классом 'brSCsc' как список
  const elements = await getElementsByXPath("//*[@class='brSCsc']");

  // Проверяем, есть ли элементы
  if (elements.length > 0) {
    console.log(`Найдено ${elements.length} элементов с классом 'brSCsc'`);

    // Итерируем по каждому элементу
    for (let i = 0; i < elements.length; i++) {
      try {
        // Кликаем по элементу
        const clickSuccess = await AsyncClickElementByXPath(
          `(//*[@class='brSCsc'])[${i + 1}]`
        );

        if (clickSuccess) {
          console.log(`Клик по элементу ${i + 1} выполнен`);

          // Проверяем наличие кнопки подписки
          const subscriptionButtonXPath =
            "//*[@id='yDmH0d']/c-wiz[5]/div/main/c-wiz/div/div[2]/div/span/div[1]/button";
          const subscriptionButtonExists = await waitForElement(
            subscriptionButtonXPath,
            1000
          );

          if (subscriptionButtonExists) {
            console.log("Кнопка подписки появилась, кликаем по ней...");
            wait(1000);
            await AsyncClickElementByXPath(subscriptionButtonXPath);
          } else {
            console.log(
              "Кнопка подписки не появилась, продолжаем с следующим элементом"
            );
          }

          // Пауза между итерациями (можно настроить)
          await new Promise((resolve) => setTimeout(resolve, 1000));
        } else {
          console.log(`Не удалось кликнуть по элементу ${i + 1}`);
        }
      } catch (error) {
        console.error(
          `Ошибка при клике или ожидании элемента ${i + 1}:`,
          error
        );
        // Ошибка поймана, цикл продолжит выполнение
      }
    }
  } else {
    console.log("Не найдено элементов с классом 'brSCsc'");
  }

  // Функция для получения всех элементов по XPath
  async function getElementsByXPath(xpath) {
    const elements = [];
    const xpathResult = document.evaluate(
      xpath,
      document,
      null,
      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
      null
    );

    for (let i = 0; i < xpathResult.snapshotLength; i++) {
      elements.push(xpathResult.snapshotItem(i));
    }

    return elements;
  }
})();

//! Не все кнопки 'Подписаться почему-то кликает. Может делать проверку на класс и кликать заново еще 3-4 итерации пока класс не будет изменен.'
