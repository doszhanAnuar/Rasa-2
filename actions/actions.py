import random
import time
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

# Действие для выбора случайной темы разговора
class ActionSuggestRandomTopic(Action):
    def name(self) -> str:
        return "action_suggest_random_topic"

    def run(self, dispatcher, tracker, domain):
        topics = [
            "И так, почему же все таки мы? Рассказать?",
            "Хотите узнать подробнее, почему крупные казахстанские компании выбирают именно нас?",
            "Хотите я расскажу, Почему крупные организации и ведущие игроки рынка выбирают именно нас?",
            "Рассказать Вам, почему крупные компании внедряют именно наших голосовых роботов?",
            "Хотите узнать еще несколько аргументов, в пользу решения Кибернет?"
        ]
        # Выбираем случайную тему
        selected_topic = random.choice(topics)
        # Отправляем тему пользователю
        dispatcher.utter_message(text=selected_topic)
        return []

# Действие для предложения случайного вопроса о партнёрстве
class ActionSuggestRandomPartnership(Action):
    def name(self) -> str:
        return "action_suggest_random_partnership"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("partnership_confirmed"):
            partnership_questions = [
                "Хотите стать нашим партнером?",
                "Желаете ли Вы стать нашим партнером?",
                "Заинтересованы ли вы в партнерстве с нами?"
            ]
            # Выбираем случайный вопрос
            selected_question = random.choice(partnership_questions)
            time.sleep(2)
            # Отправляем вопрос пользователю
            dispatcher.utter_message(text=selected_question)
        return []

# Действие для ответа на запрос о повторе почты
class ActionRepeatEmail(Action):
    def name(self) -> str:
        return "action_repeat_email"

    def run(self, dispatcher, tracker, domain):
        # Отправляем электронную почту с медленной дикцией
        dispatcher.utter_message(text="Повторяю электронный адрес sales@cyber-net.pro (медленно). Напишите нам! До свидания!")
        return []

# Действие для ответа на запрос о повторе номера телефона
class ActionRepeatPhone(Action):
    def name(self) -> str:
        return "action_repeat_phone"

    def run(self, dispatcher, tracker, domain):
        # Отправляем номер телефона с медленной дикцией
        dispatcher.utter_message(text="Диктую номер для связи +7 777 000 02 62 (медленно). Скорее звоните нам! До новых бесед!")
        return []
