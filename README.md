# Project for HackTUES Infinity
![hacktues](https://user-images.githubusercontent.com/54147006/158683996-cc4a2001-8cb8-4dcb-bdc1-2deac70e14f8.png)
Нашият проект цели лесна комуникация в космоса между космонавти, говорещи различни езици.
<br/>

# TtT pager - Space communication system

Когато пътуването в космоса стане по-достъпно, все по-голям брой хора от най-различни страни ще се запътят към него. Тук идва и проблемът за **езиковата бариера**, която Нашият проект TtT pager превъзмогва.<br/>
TtT pager представлява N на брой устройства - **пейджъри**, които всеки космонавт носи със себе си и един **главен сървър** (Big Mama), който се използва за обработване и превеждане на информацията.<br/>
 
## Тема:
![theme](https://user-images.githubusercontent.com/54147006/158684791-c95f0bd4-3810-4b0c-aede-064bcec634b1.png)
🟣 Да се разработи решение, подпомагащо живота на хората в Международната космическа станция (МКС).

<br/>

## Функционалност
Основната функционалност на пейджърите, която ги прави толкова уникални и използваеми е, че космонавтите ще могат **директно да комуникират един с друг**, без да е нужно да знаят езика на другия и **без да им е нужен интернет** за превод(все пак в космоса няма интернет 😁). Пейджърите са **малки и компактни**, за да могат да се приложат на ръката на даден космонавт.  <br/><br/>

## Архитектура
#### - Пейджър
Чрез пейджъра се записват съобщенията и се изпращат за превод на главния сървър.<br>

Ние искаме всеки пейджър да изпраща и да получава информация, затова имаме два отделни процеса: единият **слуша** сървъра, а другият **изпраща** информацията.<br>
За да се конфигурира пейджъра се посочва ip адреса му и порта, на който искаме да изпращаме информацията. <br>

Функциите, които използваме в пейджъра са :
- **Send init message** - изпраща съобщение, под формата на json(човешки четим обмен на данни), което показва, че има нов пейджър свързал се към системата.
- **Send message** - чака потребителя да въведе съобщение, което отново под формата на json се изпраща на главния сървър - "мамата".
- **Receive message** - чака сървъра да изпрати съобщение на пейджъра. Ако получи съобщение от сървъра, го показва на човека.

#### - Главен сървър
Идеята на сървъра (Big „мама”) е винаги да слуша за идващо съобщение от един пейджър към друг. За да се изпрати съобщение се използва json. Използваме го, защото улеснява препращането на структура от данни.<br>

Имаме два вида съобщения, които могат да бъдат получени:
- Init съобщение - това е първото съобщение от всеки пейджър. Чрез него пейджъра се добавя в архива на сървъра. То има 2 компонента: 
    - **име** на човека, който използва пейджъра
    - **езикът**, който той говори.
- Translate съобщение - това е съобщението, което идва от един пейджър, превежда се и се изпраща на посочения пейджър. Това съобщение съдържа 4 компонента: 
    - **име** на човека, който изпраща съобщението
    - **езикът**, който изпращащият говори
    - **име** на човека, който получава съобщението. За изпращане на всички в това поле трябва да се напише "all".
    - **съобщението** </br>

Има и опция да се изпрати до всички, като съобщението автоматично се превежда спрямо езика на всеки пейджър. <br>

Когато сървърът получи съобщение от пейджъра, преди да се изпрати към получателя, съобщението минава през „транслате”(превеждащата) функцията.
#### - Комуникация
Комуникацията става чрез използването на главния сървър. Сървърът получава информация от един пейджър, преработва(превежда) я и я изпраща на пейджъра, за когото е предназначена.

#### - Локална мрежа
Цялата комуникация се осъществява в **локална мрежа**. <br>

**Предимствата** на използването на локална мрежа са: няма нужда от достъп до интернет, което премахва необходимостта от криптиране на данните и по време на авария не е нужно да се декриптира, което подобрява сигурността на космонавите.<br>

В локалната мрежа е свързан един главен сървър и много пейджъри.
<br>
![Local area network](https://user-images.githubusercontent.com/54147006/158655021-d36ad44d-6dbd-4ca5-adee-4d3a07409b1b.jpg)
<br/>



 
За реализиране на този скрипт използваме функциите, make server, multi threaded client, send message, save init message и translate message.
-Make server е функция, която създава връзка за всеки свързал се със сървъра пейджър посредством създаване на нов процес (треад(thread)).
-Send message получава  json и клиент използвайки json генериращ  съобщения, които искаме да изпратим, проверяваме пейджъра, дали съществува..

### Технологии
MCU-to ще бъде с микро Python, а Raspberry си е с Python

### Части
- 2x ESP 32; 
- 1x Raspberry pi 400(клавиатурата) 
- LSD екран PC1602A и е свързан в схема SPI
- Keypad свързан към ESPтата. Keypad-ът е свързан в схема UARD. Той е с цифри, които образуват букви, с които (идея за дисплей, като старите Nokia) да може да пишат изречения, a дисплея просто визуализира. 
- Батерия 2500 mAh и 3,7V и то ще обединява системата ТtТ пейджър с микро контролера ESPто

### В бъдеще
 - Ще има меню с опции, които ще се избират с джойстик.
 - Ще има speak to text и text to speach, но в бъдеще с части микрофон и speaker,  ама нямаме пари, 😭
 - Ще имат функционалност за водене на личен дневник на всеки един от космонавтите и отбелязване на забележки.
 - Ще работи точно като пейджър!!


### Инсталация

##### Python библиотеки
```python
pip install time, socket, operator, json, threading, thread
```

##### Python библиотеки специално за сървъра: big_mama.py
```python
pip install argostranslate
```
Модели нужни за argostranslate:
https://drive.google.com/drive/folders/1cIqOoBTIE0JV6LVrTgF-_7vFS1UtPZEJ?usp=sharing <br/>
Изтеглете и ги сложете в папката при big_mama.py


### Отбор
 - Живко
 - Митко
 - Георги
 - Йоан
 - Ради

### Версии
 - v1 - [HackTUES Infinity](https://github.com/y0608/TtT/releases/tag/HackTUES)
