import requests
import config
import telebot
import constants
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(regexp="жопа")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "*нет, ты!*", parse_mode="Markdown")
    pass

@bot.message_handler(regexp="попасть")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Очень непросто.")
    pass

@bot.message_handler(regexp="кейс")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Почитать о кейс-интервью и посмотреть примеры кейсов можно здесь /case_interview")
    pass

@bot.message_handler(regexp="кейсы")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Почитать о кейс-интервью и посмотреть примеры кейсов можно здесь /case_interview")
    pass

@bot.message_handler(regexp="кейсах")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Почитать о кейс-интервью и посмотреть примеры кейсов можно здесь /case_interview")
    pass

@bot.message_handler(regexp="этап")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Чтобы попасть на работу в McKinsey нужно пройти отбор по резюме, тестирование и интервью. \n"
                                      "Подробнее о тесте - /pst \n"
                                      "Подробнее об интервью - /interview")
    pass

@bot.message_handler(regexp="привет")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Привет! Список команд можно вызвать по команде /start")
    pass



greeting=["привет","добрый день","хай","хелло","здравствуй","здравствуйте","привет","Добрый день","Хай","Хелло","здравствуй","Здравствуйте"]
@bot.message_handler(func=lambda message: message.text in greeting)
def handle_message(message):
    bot.send_message(message.chat.id, "Привет! Список команд можно вызвать по команде /start")
    pass

@bot.message_handler(regexp="как дела")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Отлично. Если ты заблудился, то список команд здесь /start")
    pass

@bot.message_handler(regexp="интервью")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Узнать подробнее о процессе интервью можно здесь /interview")
    pass

@bot.message_handler(regexp="канивец")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "канивест")
    pass


@bot.message_handler(regexp="Как варить кукурузу?")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "В КАСТРЮЛЕ!")
    pass

@bot.message_handler(regexp="тест")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Узнать о PST можно здесь /pst")
    pass

mckinsey=["mckinsey","маккинзи","мак кинзи","маккензи","маккинси"]
@bot.message_handler(func=lambda message: message.text in mckinsey)
@bot.message_handler(regexp="McKinsey")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "McKinsey & Company основана в 1926 г. в США. Офис в России открылся в 1993 г. \n"
                                      "McKinsey помогает крупнейшим компаниям из всех сфер бизнеса, государственным органам, международным финансовым организациям и культурным учреждениям решать самые важные, срочные и амбициозные задачи стратегического значения. \n"
                                      "В России наши клиенты – крупнейшие банки, электроэнергетические компании, игроки добывающего и металлургического секторов, а также компании а сфере FMCG, розничной торговли, телекоммуникаций и фармацевтики, крупнейшие нефтяные компании.")
    pass

@bot.message_handler(regexp="проект")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "*Можно ли выбирать проект?* \n"
                                      "Можно. После завершения проекта консультант получает список новых. Он отмечает три наиболее интересных (по задаче, отрасли, географии или другим параметрам) и один, на котором ему совсем не хотелось бы работать. \n"
                                      "Команды формируются так, чтобы проект, с одной стороны, помогал каждому консультанту развивать экспертизу и профессиональные навыки, а с другой стороны – соответствовал нуждам офиса и пожеланиям клиента. \n"
                                      "По результатам ежегодного исследования удовлетворённости сотрудников, 86% консультантов довольны выбором проектов. \n"
                                      "\n"
                                      "*Как долго длятся проекты?*\n"
                                      "В среднем – 3-4 месяца. Стандартного регламента нет, как и стандартных проектов. Каждый отличается масштабами и интенсивностью", parse_mode="Markdown")
    pass

@bot.message_handler(regexp="средний")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Учебные показатели имеют значение. Но резюме оценивается комплексно, решающего фактора нет. \n"
                                      "Помимо баллов за обучение, учитываются опыт работы, достижения в научной, профессиональной или предпринимательской сфере. \n"
                                      "Поэтому другие значительные достижения в резюме при отборе вполне могут компенсировать невысокий средний балл.")
    pass


@bot.message_handler(regexp="специальность")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Большинство консультантов начинают карьеру в качестве специалистов общего профиля. \n"
                                      "Специализация в отдельной области начинается с должности менеджера проектов. \n"
                                      "Также, в McKinsey существуют экспертные группы, где консультанты работают в выбранной ими сфере. Например, Operations, Digital McKinsey и т.д. \n"
                                      "Прочесть об этом подробнее можно в разделе /experienced")
    pass

@bot.message_handler(regexp="специализация")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Большинство консультантов начинают карьеру в качестве специалистов общего профиля. \n"
                                      "Специализация в отдельной области начинается с должности менеджера проектов. \n"
                                      "Также, в McKinsey существуют экспертные группы, где консультанты работают в выбранной ими сфере. Например, Operations, Digital McKinsey и т.д. \n"
                                      "Прочесть об этом подробнее можно в разделе /experienced")
    pass

@bot.message_handler(regexp="зарплата")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Достаточно, чтобы вести такой образ жизни, который захочется. Выбирать любые увлечения, заниматься спортом, путешествовать по всему миру, арендовать или покупать такое жильё, которое понравится. \n"
                                      "Кроме того, консультанты в России получают зарплату в евро, а значит, уровень дохода не зависит от колебаний курса валют")
    pass

@bot.message_handler(regexp="оплата")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Достаточно, чтобы вести такой образ жизни, который захочется. Выбирать любые увлечения, заниматься спортом, путешествовать по всему миру, арендовать или покупать такое жильё, которое понравится. \n"
                                      "Кроме того, консультанты в России получают зарплату в евро, а значит, уровень дохода не зависит от колебаний курса валют")
    pass


@bot.message_handler(regexp="земной")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "А удача — награда за смелость, \n"
                                      "А песни довольно одной, \n"
                                      "Чтоб только о доме в ней пелось. \n"
                                      "\n"
                                      "Теперь — к делу: /start")
    pass



@bot.message_handler(regexp="деньги")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Достаточно, чтобы вести такой образ жизни, который захочется. Выбирать любые увлечения, заниматься спортом, путешествовать по всему миру, арендовать или покупать такое жильё, которое понравится. \n"
                                      "Кроме того, консультанты в России получают зарплату в евро, а значит, уровень дохода не зависит от колебаний курса валют")
    pass

@bot.message_handler(regexp="платят")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Достаточно, чтобы вести такой образ жизни, который захочется. Выбирать любые увлечения, заниматься спортом, путешествовать по всему миру, арендовать или покупать такое жильё, которое понравится. \n"
                                      "Кроме того, консультанты в России получают зарплату в евро, а значит, уровень дохода не зависит от колебаний курса валют")
    pass

@bot.message_handler(regexp="стажировк")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "Подробнее о стажировках и сроках отбора можно узнать здесь: \n"
                                      "Business Analyst Intern /ba_intern \n"
                                      "Research & Analytics Intern /ra_intern \n"
                                      "Advanced Analytics Intern /aa_intern")



@bot.message_handler(regexp="академи")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text + '\n')
    f.close()

    bot.send_message(message.chat.id, "В этом году не будет отдельной McKinsey Academy. \n"
                                          "Вместо этого мы добавим небольшой подготовительный курс к каждому отбору между этапами теста и интервью.")
    pass

@bot.message_handler(regexp="культура")
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()

    bot.send_message(message.chat.id, "В McKinsey открытая, «неиерархичная» среда, плоская структура. Все коллеги обращаются друг к другу на «ты». \n"
                                      "С профессиональным и личным вопросом можно обратиться к сотруднику любого уровня и из любого офиса Фирмы. \n"
                                      "Объединённые общими ценностями, люди с удовольствием приобщают коллег к своим хобби и увлечениям в свободное время. \n"
                                      "Сотрудники вместе занимаются спортом и часто собираются в офисе в пятницу вечером, чтобы пообщаться в неформальной обстановке")
    pass



@bot.message_handler(regexp="/ra_intern")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/research-intern-0652")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Вы будете изучать отраслевую специфику в рамках нескольких проектов Фирмы, выявлять тренды и развивать экспертные знания McKinsey в одном или нескольких направлениях. \n"
                                      "Проектный формат работы позволит обмениваться знаниями со старшими экспертами Фирмы, консультантами и сотрудниками клиента \n"
                                      "\n"
                                      "Следующий набор: осенняя стажировка \n"
                                      "Даты подачи резюме: 1 сентября – 19 ноября \n"
                                      "Тесты: октябрь – ноябрь \n"
                                      "Интервью: декабрь \n"
                                      "Старт стажировки: февраль/апрель/июль - на выбор \n"
                                      "Кто может податься: студенты последнего курса и выпускники 2017 г. \n"
                                      "\n"
                                      "Следующий набор: весенняя стажировка \n"
                                      "Даты подачи резюме: 5 марта 2018 г. – 30 мая 2018 г. \n"
                                      "Тесты: апрель - май \n"
                                      "Интервью: июнь \n"
                                      "Старт стажировки: июнь/октябрь - на выбор \n"
                                      "Кто может податься: студенты последнего курса и выпускники 2017 г.", reply_markup=keyboard)


    pass


@bot.message_handler(regexp="/aa_intern")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/advanced-analytics-intern-9064")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Вы будете участвовать в проектах по различным индустриям, создавая математические и статистические модели. \n"
                                      "Совместно с командами экспертов Фирмы и наших клиентов Вы будете искать, создавать и оптимизировать лучшие решения для работы с большими данными \n"
                                      "\n"
                                      "Даты подачи резюме: в любой момент в течение года \n", reply_markup=keyboard)


    pass

@bot.message_handler(regexp="/parttime")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/part-time-intern-6877")
    url_button1 = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/associate-0000")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    bot.send_message(message.chat.id, "Во время стажировки вы будете работать с командами консультантов и решать очень разные задачи - \n"
                                      "от полевого сбора и анализа массивов данных  до продвинутого моделирования и участия в стриме конкретного проекта. \n"
                                      "После окончания учебы в рамках программы у вас будет возможность не только перейти на стажировку с полной занятостью, но и пройти интервью на позицию Business Analyst Intern, минуя этапы скрининга резюме и problem solving test. \n"
                                      "\n"
                                      "Требования к кандидатам: \n"
                                      "- от 3-го курса бакалавриата и старше; \n"
                                      "- знание английского языка не ниже уровня upper-intermediate; \n"
                                      "- продвинутое знание PowerPoint и Excel; \n"
                                      "- готовность посвящать работе не менее 20 часов в неделю. \n" , reply_markup=keyboard)

    pass


@bot.message_handler(regexp="/pst")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard4 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Test А", url="http://www.mckinsey.com/~/media/McKinsey/Careers%20REDESIGN/Interviewing/Main/Problem%20Solving%20Test%20PDFs/practice-test-A.ashx")
    url_button1 = types.InlineKeyboardButton(text="Test B", url="http://www.mckinsey.com/~/media/McKinsey/Careers%20REDESIGN/Interviewing/Main/Problem%20Solving%20Test%20PDFs/practice-test-B.ashx")
    url_button2 = types.InlineKeyboardButton(text="Test C", url="http://www.mckinsey.com/~/media/McKinsey/Careers%20REDESIGN/Interviewing/Main/Problem%20Solving%20Test%20PDFs/practice-test-C.ashx")
    url_button3 = types.InlineKeyboardButton(text="iOS", url="https://itunes.apple.com/us/app/mckinsey-problem-solving-practice/id884221581?mt=8")
    url_button4 = types.InlineKeyboardButton(text="Android", url="https://play.google.com/store/apps/details?id=com.pst.android")
    keyboard.add(url_button, url_button1,url_button2,url_button3,url_button4)
    bot.send_message(message.chat.id, "Все кандидаты в процессе отбора пишут специально разработанный тест на английском языке. \n"
                                      "Он состоит из 26 вопросов, основанных на реальных кейсах из практики McKinsey.\n"
                                      "Во время теста нельзя пользоваться телефонами и калькуляторами.\n"
                                      "Для подготовки к тесту можно использовать пробные варианты или мобильное приложение. \n",reply_markup=keyboard)


    pass

@bot.message_handler(regexp="/interview")
def handle_message(message):

    bot.send_message(message.chat.id,
                     'Все кандидаты проходят два раунда интервью после теста. Первый раунд проходит с менеджерами проектов и младшими партнерами, второй - с партнерами и старшими партнерами. \n'
                     'У стажеров в первом раунде два интервью, во втором - одно. У опытных специалистов три интервью в каждом раунде.\n'
                     'Все интервью проходят одинаково и состоят из двух частей.\n'
                     '\n'
                     'Первая часть или experience interview нацелена на проверку основных компетенций, которые мы ищем у наших кандидатов.\n'
                     'Эту часть иногда называют fit interview \n'                    
                     '/experience_interview — узнать подробнее \n'
                     '\n'
                     'Вторая часть интервью посвящена решению кейса, основанного на реальной практике. \n'
                     '/case_interview — узнать подробнее\n')

    pass


@bot.message_handler(regexp="/feedback")
def handle_message(message):

    bot.send_message(message.chat.id,
                     'В рамках политики отбора мы даем подробную обратную связь только по итогам интервью. \n'
                     'Мы не даем развернутой обратной связи по резюме и по результатам теста. \n'
                     'В случае отказа на этапе теста или интервью мы будем рады снова увидеть ваше резюме не ранее, чем через два года. \n'
                     'Единственное исключение мы делаем для кандидатов в стажеры, которые пишут тест ниже проходного балла, - для них срок переподачи составляет один год. \n'
                     'Для кандидатов на стажировку с частичной занятостью срок переподачи на любом этапе составляет 6 месяцев. \n'
                     'При отказе на этапе скрининга резюме срок переподачи не регламентирован, подать резюме еще раз можно в любой момент. \n')


    pass

@bot.message_handler(regexp="/experience_interview")
def handle_message(message):

    bot.send_message(message.chat.id,
                     'Первая часть или experience-interview нацелена на проверку основных компетенций, которые мы ищем у наших кандидатов. \n'
                     'Мы советуем заранее подумать об историях из вашего опыта на темы, указанные ниже:\n'
                     '\n'
                     '*Entrepreneurial drive*\n'
                     'Здесь мы ждем рассказа о том, как вы смогли инициировать и запустить какой-либо проект. \n'
                     'Примером может послужить свой бизнес, внутрикорпоративное предпринимательство, социальные проекты, академические проекты и т.п.\n'
                     'Хорошим примером будет как запуск кофейни на капмусе университета, так и организация благотворительного марафона для коллег и сотрудников вашей компании.\n'
                     '\n'
                     '*Leadership*\n'
                     'Все наши кандидаты рассматриваются с учетом того, что однажды, им нужно будет управлять проектами McKinsey. \n'
                     '95% партнеров московского офиса выросли с позиции бизнес-аналитика или ассоциата. На интервью мы ждем примера, как вы управляли командой и вдохновляли людей.\n'
                     '\n'
                     '*Personal Impact*\n'
                     'Здесь нам нужно понять вашу способность влиять на мир вокруг. \n'
                     'Personal Impact – это пример того, как вам удалось переубедить партнера или добиться нужного результата в сложной ситуации. \n'
                     'Хорошим примером можно считать решение следующих задач: получить бюджет на рискованный проект, добиться изменения управленческого решения.\n'
                     '\n', parse_mode="Markdown")
    pass

@bot.message_handler(regexp="/case_interview")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard4 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Diconsa", url="http://www.mckinsey.com/careers/interviewing/diconsa")
    url_button1 = types.InlineKeyboardButton(text="Electro-light ", url="http://www.mckinsey.com/careers/interviewing/electrolight")
    url_button2 = types.InlineKeyboardButton(text="GlobaPharm", url="http://www.mckinsey.com/careers/interviewing/globapharm")
    url_button3 = types.InlineKeyboardButton(text="Education system ", url="http://www.mckinsey.com/careers/interviewing/national-education")
    url_button4 = types.InlineKeyboardButton(text="Подробнее на сайте", url="http://www.mckinsey.com/careers/interviewing")
    keyboard.add(url_button, url_button1,url_button2,url_button3,url_button4)
    bot.send_message(message.chat.id,
                     'Вторая часть интервью посвящена решению кейса, основанного на реальной практике. \n'
                     'В McKinsey решение кейса проходит в формате диалога - это называют interviewer-led interview. \n'
                     'Вам предложат кейс клиента, дадут вводную информацию и опишут проблему. \n'
                     'Ваша задача - в процессе интервью построить верную и глубокую структуру кейса, произвести необходимую аналитику по предложенным данным и вывести логичные и применимые гипотезы и инициативы, которые помогут решить кейс.\n'
                     'Примеры кейсов, которые можно встретить на интервью: \n', parse_mode="Markdown", reply_markup=keyboard)


    pass

@bot.message_handler(regexp="/ask")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="VK", url="https://vk.com/mckinseyrussia")
    url_button1 = types.InlineKeyboardButton(text="FB", url="https://www.facebook.com/McKinseyRussia")
    keyboard.add(url_button, url_button1)
    bot.send_message(message.chat.id, "Если вы не найдете ответа на свой вопрос, просто напишите нам в любую социальную сеть" , reply_markup=keyboard)

    pass

@bot.message_handler(regexp="/start")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard2 = types.InlineKeyboardMarkup()
    keyboard3 = types.InlineKeyboardMarkup()
    keyboard4 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Узнать о PST", url="http://www.mckinsey.com/careers/interviewing")
    url_button1 = types.InlineKeyboardButton(text="Почитать про интервью", url="https://google.ru")
    url_button2 = types.InlineKeyboardButton(text="Перейти в Гугл", url="https://google.ru")
    url_button3 = types.InlineKeyboardButton(text="Перейти в Гугл", url="https://google.ru")
    url_button4 = types.InlineKeyboardButton(text="Перейти в Гугл", url="https://google.ru")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    bot.send_message(message.chat.id, "Добрый день! Меня зовут Надежда, я стажер в отделе рекрутинга McKinsey и готова ответить на частые вопросы.\n"
                                      "\n"
                                      "Узнать подробнее об этапах отбора в McKinsey.\n"
                                      "/pst — о Problem Solving Test \n"
                                      "/interview — об интервью \n"
                                      "/feedback — об обратной связи и сроках переподачи \n"
                                      "\n"
                                      "Узнать подробнее о позициях и сроках отбора. \n"
                                      "/apply — найти подходящую позицию"
                                      "\n"
                                      "/ask — задать вопрос")


    pass

@bot.message_handler(regexp="/apply")
def handle_message(message):

    bot.send_message(message.chat.id, "Если вы учитесь и еще не готовы работать полный день, то вы можете податься на стажировку с частичной занятостью \n"
                                      "Узнать подробнее: /parttime \n"
                                      "\n"
                                      "Если вы скоро заканчиваете или недавно закончили учебу и готовы работать полный день,то вы можете податься на позицию стажера: \n"
                                      "Business Analyst Intern /ba_intern \n"
                                      "Research & Analytics Intern /ra_intern \n"
                                      "Advanced Analytics Intern /aa_intern \n"
                                      "\n"
                                      "Если вы закончили учебу больше года назад, то стоит рассмотреть позиции для опытных специалистов \n"
                                      "Узнать подробнее: /experienced \n")
    pass


@bot.message_handler(regexp="/ba_intern")
def handle_message(message):

    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/business-analyst-intern-0003")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Стажер McKinsey является полноценным консультантом команды и его задачи принципиально не отличаются от задач бизнес-аналитика или ассоциата. \n"
                                      "Стажер полностью вовлекается в проект, ведет работу над своим направлением, общается с клиентом и отвечает за общий результат.\n"
                                      "\n"
                                      "Стажером Фирмы может стать студент последнего курса бакалавриата и магистратуры или выпускник 2017 года. \n"
                                      "Стажировка длится 12 месяцев для выпускников бакалавриата и 6 месяцев – для магистратуры и специалитета.\n"
                                      "\n"
                                      "Подать резюме на стажировку можно в любой момент в течение года, а начать стажироваться в феврале, мае, июле или октябре. \n"
                                      "В зависимости от даты старта мы предложим вам индивидуальные даты для теста и интервью. \n"               
                                      "В течение всего года мы формируем группы после тестирования и приглашаем на специальный курс занятий McKinsey Academy в нашем офисе. \n" 
                                      "Таким образом, независимо от даты старта вы сможете подготовиться к интервью с нашими консультантами. \n"
                                      "\n"
                                      "Все стажировки в McKinsey предполагают полную занятость: совмещать их с учебой невозможно.", reply_markup=keyboard)
    pass


@bot.message_handler(regexp="/experienced")
def handle_message(message):

    bot.send_message(message.chat.id, "Для опытных специалистов в московском офисе есть несколько путей развития.\n"
                                      "\n"
                                      "Консультанты общего профиля, готовые участвовать в проектах с разной отраслевой или функциональной направленностью \n"
                                      "Узнать подробнее: /consulting \n"
                                      "\n"
                                      "Консультанты в конкретной практике, специализирующиеся в определнной области \n"
                                      "Узнать подробнее: /practices \n"
                                      "\n"
                                      "Специалисты Research & Analytics \n"
                                      "Узнать подробнее: /research")
    pass


@bot.message_handler(regexp="/consulting")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/business-analyst-0039")
    url_button1 = types.InlineKeyboardButton(text="Подать резюме", url="http://www.mckinsey.com/careers/search-jobs/jobs/associate-0000")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    bot.send_message(message.chat.id, "Ближайший набор: \n"
                                      "Даты подачи резюме: до 30 декабря \n"
                                      "Problem-Solving Test: ноябрь - декабрь \n"
                                      "Интервью: офевраль \n"
                                      "Старт: март - апрель 2018 г. \n"
                                      "Кто может подать резюме: выпускники 2016 и предшествующих годов \n"
                                      "\n")
    bot.send_message(message.chat.id, "Бизнес-аналитик отвечает за отдельное направление работы в рамках проекта, принимает самостоятельные решения по многим вопросам и активно участвует в подготовке окончательных рекомендаций. \n"
                                      "Бизнес-аналитики часто представляют результаты работы руководству компании-клиента, их мнение учитывается при определении режима и темпов работы на проекте.", reply_markup=keyboard)
    bot.send_message(message.chat.id, "Ассоциат полностью отвечает за определенное направление работы на проекте. При минимальном вовлечении со стороны руководителей проекта он определяет план работы, представляет результаты работы команды руководству комании клиента", reply_markup=keyboard1)

    pass


@bot.message_handler(regexp="/practices")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard2 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Узнать подробнее", url="http://www.mckinsey.com/business-functions/operations/how-we-help-clients/about-this-practice")
    url_button1 = types.InlineKeyboardButton(text="Узнать подробнее", url="http://www.mckinsey.com/business-functions/mckinsey-implementation/how-we-help-clients/what-we-do")
    url_button2 = types.InlineKeyboardButton(text="Узнать подробнее", url="http://www.mckinsey.com/business-functions/digital-mckinsey/how-we-help-clients")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    keyboard2.add(url_button2)
    bot.send_message(message.chat.id, "*OPS (Operations Practice)* \n"
                                      "Консультанты в рамках практики Operations помогают клиентам решать самые сложные вопросы повышения операционной эффективности, начиная с этапа диагностики и закачивая внедрением разработанных решений. \n", parse_mode="Markdown")
    bot.send_message(message.chat.id,
                     "Мы ищем кандидатов на позиции уровня Fellow Associate и выше, имеющих степень бакалавра, магистра или доктора наук с опытом работы от 5 лет в производственном секторе, логистике, капитальном строительстве, закупках. Финальное решение об уровне предлагаемой позиции зависит от вашего предыдущего опыта и принимается по итогам интервью.",
                     reply_markup=keyboard)
    bot.send_message(message.chat.id, "*MI (McKinsey Implementation)* \n"
                                      "Консультанты в рамках практики MI помогают клиентам добиться максимально высокого финансового результата, работая с ними на всех этапах внедрения изменений, включая разработку программы реализации, управление эффективностью проекта, наставничество в ходе проекта и др. \n", parse_mode="Markdown")
    bot.send_message(message.chat.id,
                     "Мы ищем кандидатов, имеющих степень бакалавра, магистра или доктора наук с опытом работы от 7 лет в области реализации крупных проектов по трансформации бизнес-процессов и внедрению изменений в производственных, добывающих и сервисных компаниях. \n"
                     "Финальное решение об уровне предлагаемой позиции зависит от вашего предыдущего опыта и принимается по итогам интервью.", reply_markup=keyboard1)
    bot.send_message(message.chat.id, "*Digital McKinsey* \n"
                                      "Консультанты в рамках практики McKinsey Digital помогают клиентам преображать свой бизнес с помощью последних технологий, начиная от создание диджитал среды, перестройки системы управления до вопросов кибербезопасности и оптимального хранения данных. \n"
                                      "Мы ищем людей с техническим или экономическим образовнаием и с опытом от 2 лет в сфере технологий, разработки или внедрения IT решений.  Финальное решение об уровне предлагаемой позиции зависит от вашего предыдущего опыта и принимается по итогам интервью.", parse_mode="Markdown", reply_markup=keyboard2)

    pass


@bot.message_handler(regexp="/research")
def default_test(message):

    keyboard = types.InlineKeyboardMarkup()
    keyboard1 = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подать резюме",
                                            url="http://www.mckinsey.com/careers/search-jobs/jobs/research-analyst-financial-institutions-0773")
    url_button1 = types.InlineKeyboardButton(text="Подать резюме",
                                             url="http://www.mckinsey.com/careers/search-jobs/jobs/electric-power--natural-gas-research-analyst-1894")
    keyboard.add(url_button)
    keyboard1.add(url_button1)
    bot.send_message(message.chat.id, "Research & Analytics - это глобальная сеть экспертов и аналитиков McKinsey, основные задачи которых таковы: построение отраслевой экспертизы, продвинутая аналитика, математическое моделирование и программирование. \n"
                                      "Для опытных специалистов в московском офисе сейчас открыты две вакансии: \n")
    bot.send_message(message.chat.id,
                     "Отраслевой эксперт в области банков и страхования", reply_markup=keyboard)
    bot.send_message(message.chat.id,
                     "Отраслевой эксперт в области электроэнергетики и природного газа", reply_markup=keyboard1)

    pass


@bot.message_handler(content_types='text')
def handle_message(message):
    f = open('text.txt', 'a', encoding='utf-8')
    f.write(message.text+'\n')
    f.close()
    bot.send_message(message.chat.id, constants.random_message1())


    pass

while True:
    try:
        bot.polling(none_stop=True)
    except:
        continue