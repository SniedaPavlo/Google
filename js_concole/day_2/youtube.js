(async function () {
  for (let i = 0; i < 5; i++) {
    // Функция явного ожидания
    function wait(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    }

    ("use strict");

    // Ожидание 2 секунды
    await wait(500);

    //! Поиск видео и клик по рандомному
    // Функция для поиска всех элементов по XPath
    function getElementsByXpath(xpath) {
      return document.evaluate(
        xpath,
        document,
        null,
        XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
        null
      );
    }

    // Получение всех элементов по XPath
    let elements = getElementsByXpath('//*[@id="video-title-link"]');

    // Проверка, есть ли найденные элементы
    if (elements.snapshotLength > 0) {
      // Выбор случайного элемента
      let randomIndex = Math.floor(Math.random() * elements.snapshotLength);
      let randomElement = elements.snapshotItem(randomIndex);

      // Клик по случайному элементу
      randomElement.click();
    } else {
      console.log("Элементы не найдены");
    }

    // Ожидание 2 секунды
    await wait(500);

    //! Лайк
    // Функция для поиска элемента по XPath
    function getElementByXpath(xpath) {
      return document.evaluate(
        xpath,
        document,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null
      ).singleNodeValue;
    }

    // Поиск элемента лайка по XPath
    let likeButton = getElementByXpath(
      '//*[@id="top-level-buttons-computed"]/segmented-like-dislike-button-view-model/yt-smartination/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]'
    );

    // Проверка, найден ли элемент, и клик по нему
    if (likeButton) {
      likeButton.click();
    } else {
      console.log("Лайк не найден");
    }

    // Поиск кнопки подписки по XPath
    let sub_btn = getElementByXpath(
      '//*[@id="subscribe-button-shape"]/button/yt-touch-feedback-shape/div/div[2]'
    );

    // Проверка, найден ли элемент, и клик по нему
    if (sub_btn) {
      sub_btn.click();
    } else {
      console.log("Подписка не найдена");
    }

    // Переход на сайт Amazon на последней итерации
    if (i === 4) {
      window.location.href = "https://www.amazon.com/";
      break; // Прерываем цикл, так как переход на новый сайт
    }
  }
})();
