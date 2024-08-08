## Проект по автоматизации тестирования сайта компании Selectel
___
Содержание:
- [Исходные данные](#item-1)
- [Цель проекта](#item-2)
- [Используемые технологии](#item-3)
- [UI тесты](#item-4)
- [Сборка проекта и запуск тестов](#item-5)
- [Отчет о прохождении тестов](#item-6)
- [Уведомление о прохождении тестов](#item-7)
- [Видео о прохождении тестов](#item-8)
___
<a id="item-1"></a>
### Исходные данные

[Cайт компании Selectel](https://selectel.ru)

<img align="center" src="/resources/Main_page.png" width="1000" alt="Main_page"/>

___
<a id="item-2"></a>
### Цель проекта:

Тестирование основных функций сайта, позволяющих покупателю успешно найти желаемый продукт, оценить стоимость 
необходимых услуг, осуществить регистрацию и вход в личный кабинет, для последующей покупки услуг.

___
<a id="item-3"></a>
### Используемые технологии

<table width="100%" border='0'>
  <tbody>
    <tr>
      <td>Язык программирования, IDE</td>
      <td align="center">
        <a target="_blank" href="https://www.python.org/">
          <img align="center" src="/resources/Python.svg" width="40" height="40" alt="Python"/>
        </a>
        <a target="_blank" href=https://www.jetbrains.com/pycharm/>
          <img align="center" src="/resources/PyCharm.svg" width="40" height="40" alt="PyCharm"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>Библиотеки, фреймворки для написания тестов</td>
      <td align="center">
        <a target="_blank" href=https://www.selenium.dev/>
          <img align="center" src="/resources/Selenium.png" width="40" height="40" alt="Selenium"/>
        </a>
        <a target="_blank" href=https://docs.pytest.org/en/stable/index.html#>
          <img align="center" src="/resources/Pytest.svg" width="40" height="40" alt="Pytest"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        Запуск тестов
      </td>
      <td>
        <a target="_blank" href=https://www.jenkins.io/>
          <img align="center" src="/resources/Jenkins.svg" width="40" height="40" alt="Jenkins"/>
        </a>
        <a target="_blank" href=https://github.com/aerokube/selenoid>
          <img align="center" src="/resources/Selenoid.png" width="40" height="40" alt="Selenoid"/>
        </a>
      </td>
    </tr>
    <tr>
      <td>
        Формирование отчета и отправление уведомлений
      </td>
      <td>
        <a target="_blank" href=https://allurereport.org/>
          <img align="center" src="/resources/AllureReport.png" width="40" height="40" alt="Allure Report"/>
        </a>
        <a target="_blank" href=https://telegram.org/>
          <img align="center" src="/resources/Telegram.png" width="40" height="40" alt="Telegram"/>
        </a>
      </td>
    </tr>
  </tbody>
</table>

___
<a id="item-4"></a>
### UI тесты

- Работа поиска на главной странице при условии:
    - Правильного поискового ввода
    - Неправильного поискового ввода
- Вход в личный кабинет при условии:
    - Верного пароля и номера аккаунта (при отсутствии заполнения номера телефона в аккаунте)
    - Верного пароля и номера аккаунта (при наличии заполненного номера телефона в аккаунте)
    - Верного номера аккаунта и неправильного пароля
- Прохождение регистрации при условии:
    - Верно заполненных всех полей
    - Неверно заполненных обязательных полей
    - Пустых обязательных полей
- Работа калькулятора цен на услуги:
    - Возможность добавления всех услуг в корзину для расчета стоимости и их последующего удаления


___
<a id="item-5"></a>
### Сборка проекта и запуск тестов

Сборка, параметризация и запуск проекта производятся удаленно с помощью **Jenkins**.
При каждом запросе на тестирование браузера **Selenoid** запускает новый **Docker**-контейнер и 
останавливает его после закрытия браузера. Параметр, который можно изменить перед запуском проекта, - это версия браузера **Chrome**.

Для запуска проекта необходимо:
- Перейти по [ссылке](https://jenkins.autotests.cloud/job/14_vic_lav_selectel/) к проекту в **Jenkins**
- Нажать **"Build with Parameters"**
- Выбрать версию браузера (или оставить значение по умолчанию)
- Нажать **"Build"**

<p>
<img src="resources/Jenkins_Build_with_Parameters.png" width="1000" alt="Press Build with Parameters">
</p>
<p>
<img src="resources/Jenkins_Browser_version_Build.png" width="1000" alt="Press Build">
</p>


Все необходимые настройки проекта и команды запуска можно посмотреть во вкладке **"Configure"** проекта в **Jenkins**.

___
<a id="item-6"></a>
### Отчет о прохождении тестов

Отчет формируется в **Allure Report** автоматически после прохождения тестов. 
Открыть его можно как из **Jenkins** для интересующего запуска проекта, так и по [ссылке](https://jenkins.autotests.cloud/job/14_vic_lav_selectel/7/allure/).

<p>
<img src="resources/Allure_report.png" width="1000" alt="Allure Report">
</p>

___
<a id="item-7"></a>
### Уведомление о прохождении тестов

Проект в **Jenkins** настроен таким образом, чтобы уведомления приходили в конкретный чат 
приложения **Telegram**.

<p>
<img src="resources/Telegram_message.png" width="350" alt="Message from Telegram">
</p>

___
<a id="item-8"></a>
### Видео о прохождении тестов
В **Allure** отчете для всех тестов приведены видео с их прохождением. 
Ниже приведены:
- все, кроме последнего теста  
<p>
<img src="resources/video_tests.gif" alt="Selenoid Video">
</p>

- последний тест  
<p>
<img src="resources/video_price_calculator.gif" alt="Selenoid Video">
</p>