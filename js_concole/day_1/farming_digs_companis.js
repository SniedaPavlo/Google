// // ==UserScript==
// // @name         Open Search Tabs and Click Links with Random Delay
// // @namespace    http://tampermonkey.net/
// // @version      2024-10-15
// // @description  Открыть вкладки с поиском и нажать на ссылки с официальными хостами с рандомной задержкой
// // @author       You
// // @match        https://pixelscan.net/
// // @icon         https://www.google.com/s2/favicons?sz=64&domain=google.com
// // @grant        none
// // ==/UserScript==

// (function () {
//   "use strict";

//   // Хосты, которые мы будем искать
//   const officialHosts = ["google.com", "ebay.com", "amazon.com", "nike.com"];

//   // Функция для проверки ссылок и клика по ним с задержкой
//   function checkAndClickLinks() {
//     const links = document.querySelectorAll("a");
//     for (let link of links) {
//       const href = link.getAttribute("href");
//       if (href && officialHosts.some((host) => href.includes(host))) {
//         // Генерируем случайную задержку от 1 до 3 секунд
//         const delay = Math.floor(Math.random() * 3000) + 1000; // от 1000 до 3000 миллисекунд (1-3 секунды)

//         // Используем setTimeout для задержки перед кликом
//         setTimeout(() => {
//           link.click();
//           console.log(`Перешел по ссылке: ${href}`);
//         }, delay);

//         break; // Останавливаем цикл после первого клика
//       }
//     }
//   }

//   // Открываем 3 вкладки с поиском
//   window.open("https://www.google.com/search?q=pixelscan", "_blank");
//   window.open("https://www.ebay.com/sch/i.html?_nkw=pixelscan", "_blank");
//   window.open("https://www.amazon.com/s?k=pixelscan", "_blank");

//   // Через некоторое время запускаем проверку ссылок на каждой вкладке
//   setTimeout(checkAndClickLinks, 3000); // Даем время на загрузку страниц
// })();

// ==UserScript==
// @name         Open Search Tabs and Send GET Request on Links
// @namespace    http://tampermonkey.net/
// @version      2024-10-15
// @description  Открыть вкладки с поиском и отправить GET запросы на ссылки с официальными хостами
// @author       You
// @match        https://pixelscan.net/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=google.com
// @grant        none
// ==/UserScript==

(function () {
  "use strict";

  // Открываем несколько вкладок с разными ссылками
  window.open("https://www.ebay.com/");
  window.open("https://www.nike.com/");
  window.open("https://www.amazon.com/");
})();
