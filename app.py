from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout()
        # Create a label for the title of the form
        title_label = Label(text="Registration Form", font_size=20)
        layout.add_widget(title_label)
        # Create an input field for first name
        fname_input = TextInput(hint_text='First Name')
        layout.add_widget(fname_input)
        # Create an input field for last name
        lname_input = TextInput(hint_text='Last Name')
        layout.add_widget(lname_input)
        # Create an input field for email address
        email_input = TextInput(hint_text='Email Address', multiline=False, password=True)
        layout.add_widget(email_input)
        # Create an input field for phone number
        pnum_input = TextInput(hint_text='Phone Number', multiline=False, password=True)
        layout.add_widget(pnum_input)
        # Create a submit button to register user
        submit_button = Button(text='Register User', background_color=[1, 1, 1, .5])
        layout.add_widget(submit_button)
        return layout
    if __name__ == '__main__':
        RegistrationApp().run()

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout()
        # Create a label for the title of the form
        title_label = Label(text="Registration Form", font_size=20)
        layout.add_widget(title_label)
        # ... other input fields ...

        # Create a submit button to register user
        submit_button = Button(text='Register User', background_color=[1, 1, 1, .5], on_press=self.submit_form)
        layout.add_widget(submit_button)
        return layout

    def submit_form(self, instance):
        # Get input field values
        fname = fname_input.text
        lname = lname_input.text
        email = email_input.text
        pnum = pnum_input.text

        # Check if inputs are not empty
        if fname and lname and email and pnum:
            # Change the layout to a success message
            Clock.schedule_once(self.success_message, 1)

    def success_message(self, dt):
        # Remove the previous layout
        self.root.clear_widgets()

        # Create a success message
        success_label = Label(text="Registration Successful!", font_size=20)
        self.root.add_widget(success_label)


