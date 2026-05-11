from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import (
    Screen,
    SlideTransition
)

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from kivy.storage.jsonstore import JsonStore

import requests
import platform


Window.size = (360, 640)

SUPPORT_EMAIL = "frafalone@gmail.com"


# ---------------- SCREENS ----------------

class StartScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class RegisterScreen(Screen):
    pass


class ForgotScreen(Screen):
    pass


class MainScreen(Screen):
    pass


# ---------------- UI ----------------

KV = '''

ScreenManager:
    StartScreen:
    LoginScreen:
    RegisterScreen:
    ForgotScreen:
    MainScreen:


<StartScreen>:
    name: "start"

    MDScreen:

        MDBoxLayout:
            orientation: "vertical"
            padding: "30dp"
            spacing: "20dp"
            pos_hint: {"center_y": .5}

            Widget:

            MDCard:
                size_hint: .95, None
                pos_hint: {"center_x": .5}
                height: "220dp"
                padding: "25dp"
                spacing: "20dp"
                orientation: "vertical"
                radius: [22]
                elevation: 6

                MDLabel:
                    text: "Benvenuto"
                    halign: "center"
                    font_style: "H5"

                MDRaisedButton:
                    text: "Registrati"
                    pos_hint: {"center_x": .5}
                    size_hint_x: .9
                    on_release: app.switch_screen("register")

                MDRaisedButton:
                    text: "Accedi"
                    pos_hint: {"center_x": .5}
                    size_hint_x: .9
                    on_release: app.switch_screen("login")

            Widget:



<LoginScreen>:
    name: "login"

    MDScreen:

        MDBoxLayout:
            orientation: "vertical"
            padding: "30dp"
            spacing: "20dp"
            pos_hint: {"center_y": .5}

            Widget:

            MDCard:
                size_hint: .95, None
                pos_hint: {"center_x": .5}
                height: "390dp"
                padding: "25dp"
                spacing: "16dp"
                orientation: "vertical"
                radius: [22]
                elevation: 6

                MDLabel:
                    text: "Accesso"
                    halign: "center"
                    font_style: "H5"

                MDTextField:
                    id: login_user
                    hint_text: "Username"
                    size_hint_x: .95
                    pos_hint: {"center_x": .5}

                MDTextField:
                    id: login_pass
                    hint_text: "Password"
                    password: True
                    size_hint_x: .95
                    pos_hint: {"center_x": .5}

                MDRaisedButton:
                    text: "Accedi"
                    pos_hint: {"center_x": .5}
                    size_hint_x: .9
                    on_release: app.login()

                MDTextButton:
                    text: "Indietro"
                    pos_hint: {"center_x": .5}
                    on_release: app.switch_screen("start")

            Widget:



<RegisterScreen>:
    name: "register"

    MDScreen:

        MDBoxLayout:
            orientation: "vertical"
            padding: "30dp"
            spacing: "20dp"
            pos_hint: {"center_y": .5}

            Widget:

            MDCard:
                size_hint: .95, None
                pos_hint: {"center_x": .5}
                height: "430dp"
                padding: "25dp"
                spacing: "16dp"
                orientation: "vertical"
                radius: [22]
                elevation: 6

                MDLabel:
                    text: "Registrazione"
                    halign: "center"
                    font_style: "H5"

                MDTextField:
                    id: reg_user
                    hint_text: "Username"
                    size_hint_x: .95
                    pos_hint: {"center_x": .5}

                MDTextField:
                    id: reg_email
                    hint_text: "Email"
                    size_hint_x: .95
                    pos_hint: {"center_x": .5}

                MDTextField:
                    id: reg_pass
                    hint_text: "Password"
                    password: True
                    size_hint_x: .95
                    pos_hint: {"center_x": .5}

                MDRaisedButton:
                    text: "Crea account"
                    pos_hint: {"center_x": .5}
                    size_hint_x: .9
                    on_release: app.register()

                MDTextButton:
                    text: "Indietro"
                    pos_hint: {"center_x": .5}
                    on_release: app.switch_screen("start")

            Widget:



<ForgotScreen>:
    name: "forgot"



<MainScreen>:
    name: "main"

    MDScreen:

        MDNavigationLayout:

            ScreenManager:

                MDScreen:

                    MDBoxLayout:
                        orientation: "vertical"

                        MDTopAppBar:
                            title: "Auth System"
                            elevation: 4
                            left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                        MDBoxLayout:
                            orientation: "vertical"
                            padding: "20dp"
                            spacing: "20dp"

                            Widget:

                            MDRaisedButton:
                                text: "Credenziali"
                                size_hint_x: .9
                                pos_hint: {"center_x": .5}
                                on_release: app.show_credentials()

                            MDRaisedButton:
                                text: "Versione"
                                size_hint_x: .9
                                pos_hint: {"center_x": .5}
                                on_release: app.show_version()

                            MDRaisedButton:
                                text: "Sicurezza"
                                size_hint_x: .9
                                pos_hint: {"center_x": .5}
                                on_release: app.show_security()

                            MDRaisedButton:
                                text: "Sistema"
                                size_hint_x: .9
                                pos_hint: {"center_x": .5}
                                on_release: app.show_system()

                            Widget:


            MDNavigationDrawer:
                id: nav_drawer

                MDBoxLayout:
                    orientation: "vertical"
                    padding: "20dp"
                    spacing: "10dp"

                    OneLineListItem:
                        text: "Home"
                        on_release: nav_drawer.set_state("close")

                    OneLineListItem:
                        text: "Crediti"
                        on_release: app.show_credits()

                    OneLineListItem:
                        text: "Impostazioni"
                        on_release: app.show_version()

                    OneLineListItem:
                        text: "Supporto"
                        on_release: app.show_support()

                    Widget:

                    MDRaisedButton:
                        text: "Logout"
                        size_hint_x: .9
                        pos_hint: {"center_x": .5}
                        on_release: app.logout()

'''


# ---------------- APP ----------------

class MyApp(MDApp):

    API_URL = "http://127.0.0.1:8000"

    current_user = "guest"


    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"

        self.db = JsonStore(
            "users.json"
        )

        self.remember_db = JsonStore(
            "remember.json"
        )

        root = Builder.load_string(
            KV
        )

        root.transition = SlideTransition(
            duration=0.25
        )

        Clock.schedule_once(
            self.auto_login,
            0.5
        )

        return root


    # ---------- navigation ----------

    def switch_screen(
        self,
        name
    ):

        self.root.current = name


    def logout(self):

        self.root.current = "start"


    # ---------- auth ----------

    def login(self):

        screen = self.root.get_screen(
            "login"
        )

        response = requests.post(
            f"{self.API_URL}/login",
            json={
                "username": screen.ids.login_user.text,
                "password": screen.ids.login_pass.text
            }
        )

        if response.status_code == 200:

            self.current_user = screen.ids.login_user.text

            self.switch_screen(
                "main"
            )


    def register(self):

        screen = self.root.get_screen(
            "register"
        )

        requests.post(
            f"{self.API_URL}/register",
            json={
                "username": screen.ids.reg_user.text,
                "email": screen.ids.reg_email.text,
                "password": screen.ids.reg_pass.text
            }
        )

        self.switch_screen(
            "login"
        )


    # ---------- dialogs ----------

    def show_card(
        self,
        title,
        text
    ):

        MDDialog(
            title=title,
            text=text
        ).open()


    def show_credentials(self):

        self.show_card(
            "Credenziali",
            f"Utente: {self.current_user}\n"
            f"API: {self.API_URL}\n"
            f"Sessione: attiva"
        )


    def show_version(self):

        self.show_card(
            "Versione",
            f"App: v1.0\n"
            f"Python: {platform.python_version()}\n"
            f"FastAPI + KivyMD"
        )


    def show_security(self):

        self.show_card(
            "Sicurezza",
            " bcrypt\n"
            " rate limiting\n"
            " password validation"
        )


    def show_system(self):

        try:

            response = requests.get(
                self.API_URL
            )

            self.show_card(
                "Sistema",
                f"Backend online\n{response.json()}"
            )

        except:

            self.show_card(
                "Sistema",
                "Backend offline"
            )


    def show_support(self):

        self.show_card(
            "Supporto",
            f"Email:\n{SUPPORT_EMAIL}"
        )


    def show_credits(self):

        self.show_card(
            "Crediti",
            "Sviluppato da:\n"
            "Francesco Falone\n\n"
            "Python Developer\n"
            "FastAPI • KivyMD"
        )


    def auto_login(
        self,
        dt
    ):
        pass


if __name__ == "__main__":

    MyApp().run()
