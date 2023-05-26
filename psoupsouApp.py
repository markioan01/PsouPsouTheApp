import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from kivy.graphics import Color
from kivy.graphics import Rectangle

from kivymd.uix.textfield import MDTextField
from kivy.properties import ListProperty

from kivymd.app import MDApp


from kivy.properties import ObjectProperty

from kivy.uix.dropdown import DropDown

from kivy.uix.scrollview import ScrollView


kivy.config.Config.set('graphics', 'resizable', False)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Top frame for the logo
        self.top_frame = BoxLayout(size_hint=(1, 0.25))
        self.logo = Image(source="your_logo.png")
        self.top_frame.add_widget(self.logo)

        # Bottom frame for the login form
        self.bottom_frame = BoxLayout(orientation="vertical", padding=20, spacing=10, size_hint=(1, 0.6))

        # Inner frame for login inputs and buttons
        self.inner_frame = BoxLayout(orientation="vertical", padding=20, spacing=10, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.username_label = Label(text="Username:")
        self.username_input = TextInput()
        self.inner_frame.add_widget(self.username_label)
        self.inner_frame.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        self.password_input = TextInput(password=True)
        self.inner_frame.add_widget(self.password_label)
        self.inner_frame.add_widget(self.password_input)

        self.error_label = Label(text="")
        self.inner_frame.add_widget(self.error_label)

        self.login_button = Button(text="Login", on_press=self.login, size_hint=(0.5, None), height=40, pos_hint={'center_x': 0.5})
        self.inner_frame.add_widget(self.login_button)

        self.register_label = Label(text="[ref=register]Register[/ref]", markup=True, halign="center")
        self.register_label.bind(on_ref_press=self.register)
        self.inner_frame.add_widget(self.register_label)

        # Add inner frame to bottom frame
        self.bottom_frame.add_widget(self.inner_frame)

        # Footer frame for additional information
        self.footer_frame = BoxLayout(size_hint=(1, 0.15))
        self.footer_label = Label(text="Copyright © 2023. All rights reserved.")
        self.footer_frame.add_widget(self.footer_label)

        # Add all frames to the main layout
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.top_frame)
        self.layout.add_widget(self.bottom_frame)
        self.layout.add_widget(self.footer_frame)
        self.add_widget(self.layout)


    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        #print(username," ",password)
        if username == "" and password == "":
            self.error_label.text = ""
            self.manager.current = "chat"
        else:
            self.error_label.text = "Invalid username or password"

    def register(self, instance, value):
        self.manager.current = "register"


class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Top frame for the logo
        self.top_frame = BoxLayout(size_hint=(1, 0.25))
        self.logo = Image(source="your_logo.png")
        self.top_frame.add_widget(self.logo)

        # Middle frame for the registration form
        self.middle_frame = BoxLayout(orientation="vertical", padding=20, spacing=10, size_hint=(1, 0.6))

        # Inner frame for registration inputs and buttons
        self.inner_frame = BoxLayout(orientation="vertical", padding=20, spacing=10, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.username_label = Label(text="Username:")
        self.username_input = TextInput()
        self.inner_frame.add_widget(self.username_label)
        self.inner_frame.add_widget(self.username_input)

        self.password_label = Label(text="Password:")
        self.password_input = TextInput(password=True)
        self.inner_frame.add_widget(self.password_label)
        self.inner_frame.add_widget(self.password_input)

        self.confirm_password_label = Label(text="Confirm Password:")
        self.confirm_password_input = TextInput(password=True)
        self.inner_frame.add_widget(self.confirm_password_label)
        self.inner_frame.add_widget(self.confirm_password_input)

        self.error_label = Label(text="")
        self.inner_frame.add_widget(self.error_label)

        self.register_button = Button(text="Register", on_press=self.register, size_hint=(0.5, None), height=40, pos_hint={'center_x': 0.5})
        self.inner_frame.add_widget(self.register_button)

        self.back_label = Label(text="[ref=login]Back to login[/ref]", markup=True, halign="center")
        self.back_label.bind(on_ref_press=self.back_to_login)
        self.inner_frame.add_widget(self.back_label)

        # Add inner frame to middle frame
        self.middle_frame.add_widget(self.inner_frame)

        # Add all frames to the main layout
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.top_frame)
        self.layout.add_widget(self.middle_frame)
        
        # Footer frame for additional information
        self.footer_frame = BoxLayout(size_hint=(1, 0.15))
        self.footer_label = Label(text="Copyright © 2023. All rights reserved.")
        self.footer_frame.add_widget(self.footer_label)
        self.layout.add_widget(self.footer_frame)

        self.add_widget(self.layout)



    def register(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        if not username or not password or not confirm_password:
            self.error_label.text = "Please fill in all fields"
        elif password != confirm_password:
            self.error_label.text = "Passwords do not match"
        else:
            self.error_label.text = ""
            self.manager.current = "chat"

    def back_to_login(self, instance, value):
        self.manager.current = "login"


class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create the main layout
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Create the top frame
        self.top_frame = BoxLayout(orientation="horizontal", size_hint=(1, 1/8), spacing=10)

        # Add left frame to the left of the top frame
        self.left_frame = BoxLayout(size_hint=(0.25, 1))
        with self.left_frame.canvas.before:
            Color(1, 0.5, 0, 1)
            self.left_frame_rect = Rectangle(size=self.left_frame.size, pos=self.left_frame.pos)
        self.left_frame.bind(size=lambda s, v: setattr(self.left_frame_rect, 'size', v),
                            pos=lambda s, v: setattr(self.left_frame_rect, 'pos', v))
        self.logo = Image(source="logo.png", size_hint=(1, 1))
        self.left_frame.add_widget(self.logo)
        self.top_frame.add_widget(self.left_frame)

        # Add center frame to the center of the top frame
        self.center_frame = BoxLayout(size_hint=(0.75, 1))
        with self.center_frame.canvas.before:
            Color(1, 0.5, 0, 1)
            self.center_frame_rect = Rectangle(size=self.center_frame.size, pos=self.center_frame.pos)
        self.center_frame.bind(size=lambda s, v: setattr(self.center_frame_rect, 'size', v),
                            pos=lambda s, v: setattr(self.center_frame_rect, 'pos', v))
        
        # Create the search bar and the drop-down list
        self.search_bar = TextInput(hint_text="Find Friends...", size_hint=(0.5, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.center_frame.add_widget(self.search_bar)
        
                
        self.search_button = Button(text="Search", size_hint=(0.2, 0.4), pos_hint={'center_y': 0.5})
        self.search_button.bind(on_release=self.search_friend_button_clicked)
        self.center_frame.add_widget(self.search_button)
        self.button1 = Button(text="Button 1", size_hint=(0.1, 0.4), pos_hint={'center_y': 0.5})
        self.center_frame.add_widget(self.button1)
        self.button2 = Button(text="Button 2", size_hint=(0.1, 0.4), pos_hint={'center_y': 0.5})
        self.center_frame.add_widget(self.button2)
        self.top_frame.add_widget(self.center_frame)

        self.layout.add_widget(self.top_frame)



        # Create the bottom frame
        self.bottom_frame = BoxLayout(orientation="horizontal", size_hint=(1, 7/8), spacing=10)
        self.bottom_frame_left = BoxLayout(orientation="vertical", size_hint=(1/4, 1))
        with self.bottom_frame_left.canvas.before:
            Color(1, 1, 0, 1)
            self.bottom_frame_left_rect = Rectangle(size=self.bottom_frame_left.size, pos=self.bottom_frame_left.pos)
        self.bottom_frame_left.bind(size=lambda s, v: setattr(self.bottom_frame_left_rect, 'size', v),
                                    pos=lambda s, v: setattr(self.bottom_frame_left_rect, 'pos', v))
        self.search_label = Label(text="Conversations:", font_size="18sp", size_hint=(1, 0.5/8))
        self.search_bar = TextInput(hint_text="Type here...", font_size="16sp", size_hint=(1, 0.4/8))
        self.search_button = Button(text="Search", font_size="16sp", size_hint=(1, 0.25/8))
        self.bottom_frame_left.add_widget(self.search_label)
        self.bottom_frame_left.add_widget(self.search_bar)
        self.bottom_frame_left.add_widget(self.search_button)


        # Add a new frame below the search button
        self.bottom_frame_left_bottom = BoxLayout(size_hint=(1, 5/8))
        with self.bottom_frame_left_bottom.canvas.before:
            Color(1, 0, 1, 1)
            self.bottom_frame_left_bottom_rect = Rectangle(size=self.bottom_frame_left_bottom.size, pos=self.bottom_frame_left_bottom.pos)
        self.bottom_frame_left_bottom.bind(size=lambda s, v: setattr(self.bottom_frame_left_bottom_rect, 'size', v),
                                           pos=lambda s, v: setattr(self.bottom_frame_left_bottom_rect, 'pos', v))
        self.bottom_frame_left.add_widget(self.bottom_frame_left_bottom)

        # Create a scrollable container to hold a list of objects
        self.scroll_container = ScrollView()
        self.list_container = BoxLayout(orientation="vertical", spacing=10, size_hint_y=None)
        self.list_container.bind(minimum_height=self.list_container.setter('height'))
        self.scroll_container.add_widget(self.list_container)
        
        # Add some objects to the list container
        for i in range(50):
            label = Label(text=f"Object {i+1}", size_hint=(1, None), height=35)
            self.list_container.add_widget(label)

        # Add the scrollable container to the bottom frame left bottom layout
        self.bottom_frame_left_bottom.add_widget(self.scroll_container)


        # Add a new frame below the scrollable frame
        self.bottom_frame_left_bottom_bottom = BoxLayout(size_hint=(1, 0.5/8))
        with self.bottom_frame_left_bottom_bottom.canvas.before:
            Color(1, 0, 0, 1)
            self.bottom_frame_left_bottom_bottom_rect = Rectangle(size=self.bottom_frame_left_bottom_bottom.size, pos=self.bottom_frame_left_bottom_bottom.pos)
        self.bottom_frame_left_bottom_bottom.bind(size=lambda s, v: setattr(self.bottom_frame_left_bottom_bottom_rect, 'size', v),
                                           pos=lambda s, v: setattr(self.bottom_frame_left_bottom_bottom_rect, 'pos', v))
        self.bottom_frame_left.add_widget(self.bottom_frame_left_bottom_bottom)



        
        self.bottom_frame_right = BoxLayout(orientation="vertical", size_hint=(3/4, 1))
        with self.bottom_frame_right.canvas.before:
            Color(1, 0.5, 0, 1)
            self.bottom_frame_right_rect = Rectangle(size=self.bottom_frame_right.size, pos=self.bottom_frame_right.pos)
        self.bottom_frame_right.bind(size=lambda s, v: setattr(self.bottom_frame_right_rect, 'size', v),
                                     pos=lambda s, v: setattr(self.bottom_frame_right_rect, 'pos', v))
        
        self.bottom_frame.add_widget(self.bottom_frame_left)
        self.bottom_frame.add_widget(self.bottom_frame_right)
        self.layout.add_widget(self.bottom_frame)

        
        # Add frames to bottom_frame_right
        self.bottom_frame_right_top = BoxLayout(size_hint=(1, 0.7/8))
        with self.bottom_frame_right_top.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            self.bottom_frame_right_top_rect = Rectangle(size=self.bottom_frame_right_top.size, pos=self.bottom_frame_right_top.pos)
        self.bottom_frame_right_top.bind(size=lambda s, v: setattr(self.bottom_frame_right_top_rect, 'size', v),
                                         pos=lambda s, v: setattr(self.bottom_frame_right_top_rect, 'pos', v))

        self.bottom_frame_right_middle = BoxLayout(size_hint=(1, 7/8))
        self.bottom_frame_right_middle_scrollview = ScrollView(do_scroll_x=False)
        self.bottom_frame_right_middle_scrollview.add_widget(self.bottom_frame_right_middle)

        self.bottom_frame_right_bottom = BoxLayout(size_hint=(1, 0.7/8))
        with self.bottom_frame_right_bottom.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            self.bottom_frame_right_bottom_rect = Rectangle(size=self.bottom_frame_right_bottom.size, pos=self.bottom_frame_right_bottom.pos)
        self.bottom_frame_right_bottom.bind(size=lambda s, v: setattr(self.bottom_frame_right_bottom_rect, 'size', v),
                                            pos=lambda s, v: setattr(self.bottom_frame_right_bottom_rect, 'pos', v))

        self.bottom_frame_right.add_widget(self.bottom_frame_right_top)
        self.bottom_frame_right.add_widget(self.bottom_frame_right_middle_scrollview)
        self.bottom_frame_right.add_widget(self.bottom_frame_right_bottom)


        # Add the main layout to the screen
        self.add_widget(self.layout)


    def logout(self, instance):
        self.manager.current = "login"

    def search_friend_button_clicked(self, instance):
        popup_content = BoxLayout(orientation='horizontal')

        # Left yellow frame with an image
        left_frame = BoxLayout(orientation='vertical', size_hint=(1/3, 1))
        left_frame.add_widget(Image(source='path_to_image.png'))

        # Right red frame with text and button
        right_frame = BoxLayout(orientation='vertical', size_hint=(2/3, 1))
        right_frame.add_widget(Label(text='Some text on top', size_hint=(1, 0.8)))
        right_frame.add_widget(Button(text='Send Friend Request', size_hint=(1, 0.2)))

        popup_content.add_widget(left_frame)
        popup_content.add_widget(right_frame)

        popup = Popup(title='Search Account', content=popup_content, size_hint=(0.8, 0.4))
        popup.open()


class MyChatApp(App):
    def build(self):
        sm = ScreenManager()

        login_screen = LoginScreen(name="login")
        sm.add_widget(login_screen)

        register_screen = RegisterScreen(name="register")
        sm.add_widget(register_screen)

        chat_screen = ChatScreen(name="chat")
        sm.add_widget(chat_screen)

        return sm


if __name__ == "__main__":
    MyChatApp().run()
