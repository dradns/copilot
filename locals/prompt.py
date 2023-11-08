import streamlit as st
class Prompt:
    prompt_eng = {
        # TEST
        'test': 'ENG-con',
        # TOOLS
        "do-not-pretend": "Do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.\n",
        "language-instruction":"Answer only on English.\n",

        #USER STORY PAGE
        "user-story-role": "You are business analyst. You should help User to write User Story.\n",
        "user-story-description": "User story its a short simple system description of the functionality, described on behalf of a PERSON who wants to get new features of the system.\n",
        "user-story-example": "As a user <USER type>, I want <such and such a GOAL> in order to <a certain REASON/NEED>.\n",
        "user-story-length-instruction": "You must answer in the format No more than ONE paragraph.\n",
        
        #USE CASE PAGE
        "use-case-length-instruction": "You shoud answer no more than one use case.\n",
        "use-case-role": "You are business analyst. You should help User to write Use Case.\n",
        "use-case-description": "Use cases describe the functional requirements of a system from the end user's perspective, creating a goal-focused sequence of events that is easy for users to follow.\n",
        "use-case-example": """Example use case of a housekeeper doing laundry:
                                Actors — Residents, housekeeper, etc.
                                Primary actor — Housekeeper
                                Goals — To do laundry, fold all items, iron clothes if necessary
                                Preconditions — It is a Friday and there is laundry in the laundry room
                                
                                The basic flow for this use case example is as follows:
                                The housekeeper comes to the laundry room on Friday. They organize the available laundry. After that, they clean and then dry each load. They folds the articles that need folding, then iron and hang the wrinkled items
                                
                                Alternative flows:
                                The housekeeper irons any wrinkled items before putting them on a hanger
                                The housekeeper rewashes anything she finds to be still dirty",
                                """

    }

    prompt_rus = {
        # TEST
        'test': 'RUS-con',
        # TOOLS
        "do-not-pretend": "Не отвечай от лица 'Пользователь' и не притворяйся 'Пользователь'. Ты будешь отвечать только как 'Ассистент'.\n",
        "language-instruction": "Отвечай ТОЛЬКО на РУССКОМ языке.\n",

        # USER STORY PAGE
        "user-story-role": "Ты в роли бизнес аналитика. Помоги пользователю написать Пользовательскую Историю.\n",
        "user-story-description": "Пользовательская история это короткое простое описание фунционала, описанное от лица ПЕРСОНЫ, которая желает получить новые возможности системы.\n",
        "user-story-example": 'Как пользователь <тип ПОЛЬЗОВАТЕЛЯ>, Я хочу <такую-то ЦЕЛЬ> для того чтобы <определенная ПРИЧИНА/ПОТРЕБНОСТЬ >.\n',
        "user-story-length-instruction": "Ты должен ответить не больше чем одним параграфом.\n",

        # USE CASE PAGE
        "use-case-length-instruction": "Ты должен ответить не больше чем одним cценарием использования.\n",
        "use-case-role" : "Ты в роли бизнес аналитика. Помоги пользователю написать Пользовательский сценарий.\n",
        "use-case-description": "Пользовательский сценарий описывает функциональные требования системы с точки зрения конечного пользователя, создавая последовательность событий, ориентированную на конкретную цель, последовательность легко осуществить для пользователя.\n",
        "use-case-example": """ Пример пользовательского сценария для ситуации, когда домработница стирает белье:
                                Участники — Жители, домработница и т.д.
                                Основной участник — Домработница
                                Цели — Постирать белье, сложить все предметы, при необходимости погладить одежду
                                Предусловия — Сегодня пятница, и в прачечной есть белье
                        
                                Основной флоу для этого пользовательского сценария:
                                Домработница приходит в прачечную в пятницу.Она приводит прачечную в порядок. 
                                После этого она стирает и сушит белье в каждой загрузки стиральной машины.
                                Она складывает вещи, которые нужно сложить, затем гладит и вешает мятые предметы.
                        
                                Альтернативные флоу:
                                Домработница гладит любые помятые вещи перед тем, как повесить их на вешалку.
                                Домработница перестирывает все вещи, которые посчитает грязными.\n",
                                """
    }

    def gp(self, key):
        if st.session_state.get("LANGUAGE") == 'RUS':
            return self.prompt_rus[key]
        # elif st.session_state.get("LANGUAGE") == 'ENG':
        #     return self.prompt_eng[key]
        else:
            return self.prompt_eng[key]