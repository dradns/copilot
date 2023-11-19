import streamlit as st
class Content:
    content_eng = {
        #TEST
        "test": "ENG-con",
        #TOOLS
        "thinking": "Thinking...",



        #USER STORY PAGE
        "user-story-title": "User story",
        "user-story-description": "This page will help you to write User Story. It's recommended to read page goals, stages and typical mistakes. After that go to the chat and AI will help you to write User Story for you 😎",
        "user-story-goal-page": "Page goals 🎯",
        "user-story-steps": "Page steps 📶",
        "user-story-typical-mistakes": "Typical mistakes 🚨",
        "user-story-lets-write": "Are you ready to write couple of user stories?",
        "user-story-button-forget": "Forget context",
        "user-story-ass-first-reply": "I'm your copilot! Wanna help?",

        # USE CASE PAGE
        "use-case-title": "Use case",
        "use-case-description": "This page will help you to write Use Case. It's recommended to read page goals, stages and typical mistakes. After that go to the chat and AI will help you to write User Story for you 😎",
        "use-case-goal-page": "Page goals 🎯",
        "use-case-steps": "Page steps 📶",
        "use-case-typical-mistakes": "Typical mistakes 🚨",
        "use-case-lets-write": "Are you ready to write some of use cases?",
        "use-case-button-forget": "Forget context",
        "use-case-ass-first-reply": "I'm best business analyst ever! Wanna help?",

        # ACCEPTANCE CRITERIA PAGE
        "acceptance-criteria-title": "Acceptance criteria",
        "acceptance-criteria-description": "This page will help you to write Acceptance Criteria. It's recommended to read page goals, stages and typical mistakes. After that go to the chat and AI will help you to write Acceptance Criteria for you 😎",
        "acceptance-criteria-goal-page": "Page goals 🎯",
        "acceptance-criteria-steps": "Page steps 📶",
        "acceptance-criteria-typical-mistakes": "Typical mistakes 🚨",
        "acceptance-criteria-lets-write": "Are you ready to write some acceptance criteria?",
        "acceptance-criteria-button-forget": "Forget context",
        "acceptance-criteria-ass-first-reply": "I'm best tester ever! Wanna help?",
    }

    content_rus = {
        # TEST
        "test": "RUS-con",
        # TOOLS
        "thinking": "Думаю...",

        # USER STORY PAGE
        "user-story-title": "Пользовательская история",
        "user-story-description": "Эта страница поможет тебе написать пользовательскую историю. Рекомендую прочитать цели, этапы и типичные ошибки ниже. Потом переходи в чат и AI поможет тебе написать пользовательскую историю для тебя 😎",
        "user-story-goal-page": "Цели страницы 🎯",
        "user-story-steps": "Этапы выполнения 📶",
        "user-story-typical-mistakes": "Типичные ошибки 🚨",
        "user-story-lets-write": "Готов написать пару пользовательских историй?",
        "user-story-button-forget": "Забыть контекст",
        "user-story-ass-first-reply": "Я твой копайлот! Давай помогу?",

        # USE CASE PAGE
        "use-case-title": "Cценарий использования",
        "use-case-description": "Эта страница поможет тебе написать сценарий использования. Рекомендую прочитать цели, этапы и типичные ошибки ниже. Потом переходи в чат и AI поможет тебе написать сценарий использования 😎",
        "use-case-goal-page": "Цели страницы 🎯",
        "use-case-steps": "Этапы выполнения 📶",
        "use-case-typical-mistakes": "Типичные ошибки 🚨",
        "use-case-lets-write": "Готов написать пару сценариев использования?",
        "use-case-button-forget": "Забыть контекст",
        "use-case-ass-first-reply": "Я лучший бизнес аналитик! Давай помогу?",

        # ACCEPTANCE CRITERIA PAGE
        "acceptance-criteria-title": "Критерии приемки",
        "acceptance-criteria-description": "Эта страница поможет тебе написать критерии приемки. Рекомендую прочитать цели, этапы и типичные ошибки ниже. Потом переходи в чат и AI поможет тебе написать критерии приемки 😎",
        "acceptance-criteria-goal-page": "Цели страницы 🎯",
        "acceptance-criteria-steps": "Этапы выполнения 📶",
        "acceptance-criteria-typical-mistakes": "Типичные ошибки 🚨",
        "acceptance-criteria-lets-write": "Готов написать критерии приемки?",
        "acceptance-criteria-button-forget": "Забыть контекст",
        "acceptance-criteria-ass-first-reply": "Я лучший тестировщик! Давай помогу?",
    }

    def gt(self, key):
        if st.session_state.get("LANGUAGE") == 'RUS':
            return self.content_rus[key]
        # elif st.session_state.get("LANGUAGE") == 'ENG':
        #     return self.content_eng[key]
        else:
            return self.content_eng[key]
