from operator import and_
from kivy.core import text
from kivy.uix.behaviors import button
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.filemanager import MDFileManager
from pathlib import Path
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout
import os
from proTest import getting_testvalue, kcc
Window.size = (300, 500)

navigation_helper = """
#:import webbrowser webbrowser

ScreenManager:
    MainScreen:
    AboutScreen:
    ContactScreen:
    FilechooserScreen:
    ResultScreen:

<MainScreen>:
    name: 'main'
    Screen:
        MDNavigationLayout:
            ScreenManager:
                Screen:
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Music Genre Classifier'
                            anchor_title: 'left'
                            left_action_items: [["menu",lambda x: nav_drawer.set_state('toggle')]]
                            elevation: 10
                            
                            

                        MDBottomNavigation:
                            panel_color: .7, .7, .7, 1

                            MDBottomNavigationItem:
                                name: 'screen 1'
                                text: 'HOME'
                                icon: 'home'
                                MDRectangleFlatButton:
                                    text: 'Select'
                                    text_color: 'teal'
                                    pos_hint: {'center_x':0.5,'center_y':0.4}
                                    on_release: root.manager.current = 'filechooser'

                                MDLabel:
                                    text: 'Get Started'
                                    halign: 'center'

                            MDBottomNavigationItem:
                                name: 'screen 2'
                                text: 'Result'
                                icon: 'music'

                                MDLabel:
                                    text: 'This is Result'
                                    halign: 'center'

                            MDBottomNavigationItem:
                                name: 'History'
                                text: 'History'
                                icon: 'history'

                                MDLabel:
                                    text: 'This is History'
                                    halign: 'center'
    MDNavigationDrawer:
        id: nav_drawer
        ScrollView:

            MDList:
                OneLineListItem:
                    text: 'About'
                    spacing: '8dp'
                    padding: '8dp'
                    on_release: root.manager.current = 'about'
                
                OneLineListItem:
                    text: 'Contact Us'
                    spacing: '8dp'
                    padding: '8dp'
                    on_release: root.manager.current = 'contact'
                



  

<AboutScreen>:
    name: 'about'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'teal'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_release: root.manager.current = 'main'
    MDLabel
        text: 'This is about'
        halign: 'center'

<ContactScreen>:
    name: 'contact'
    MDRectangleFlatButton:
        text: 'Back'
        text_color: 'teal'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_release: root.manager.current = 'main'
    MDLabel
        id: links
        text: 'Get in touch with us:'
        pos_hint: {'x':-.18, 'y':.4}
        halign: 'center'
    MDLabel
        markup: True
        text: '[ref=some]987654321 [/ref]'
        pos_hint:{'x': 0.2, 'y':0.3}
        on_ref_press:

    MDLabel
        markup: True
        text: '[ref=some]@BethelTeam[/ref]'
        pos_hint:{'x': 0.2, 'y':0.2}
        on_ref_press: webbrowser.open('www.instagram.com',new=1)
    MDLabel
        markup: True
        text: '[ref=some]@TeamBethel[/ref]'
        pos_hint:{'x': 0.2, 'y':0.1}
        on_ref_press: webbrowser.open('www.twitter.com') 
    MDLabel
        markup: True
        text: '[ref=some]@Bthelteam[/ref]'
        pos_hint:{'x': 0.2, 'y':0}
        on_ref_press: webbrowser.open('www.facebook.com')
    MDLabel
        markup: True
        text: '[ref=some]Bthelteam@gmail.com[/ref]'
        pos_hint:{'x': 0.2, 'y':-.1}
        on_ref_press:

    MDIcon
        icon: 'phone'
        pos_hint: {'x':.08, 'y':.3}
    MDIcon
        icon: 'instagram'   
        pos_hint: {'x':.08, 'y':.2}    
    MDIcon    
        icon: 'twitter'
        pos_hint: {'x':.08, 'y':.1}
    MDIcon    
        icon: 'facebook'
        pos_hint: {'x':.08, 'y':0}
    MDIcon    
        icon: 'email'
        pos_hint: {'x':.08, 'y':-.1}
        
<ResultScreen>:
    id: result
    name: 'result'
    MDRectangleFlatButton:
        text: 'Genre'
        text_color: 'teal'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_release: app.show_alert_dialog()
    MDRectangleFlatButton:
        text: 'Accuracy'
        text_color: 'teal'
        pos_hint: {'center_x':0.75,'center_y':0.2}
        on_release: app.show_alert_dialog()
    MDLabel
        text: 'This is result'
        halign: 'center'

<FilechooserScreen>:
    name: 'filechooser'
    MDBoxLayout:
        FileChooserListView:
            id:filechooser
            on_selection: app.selected(filechooser)
            on_selection: root.manager.current = 'result'

            
            MDRectangleFlatButton:
                text: 'Back'
                text_color: 'teal'
                pos_hint: {'center_x':0.5,'center_y':0.2}
                on_release: root.manager.current = 'main'



"""

class MainScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class ContactScreen(Screen):
    pass

class ResultScreen(Screen):
    pass

class FilechooserScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(AboutScreen(name='about'))
sm.add_widget(ContactScreen(name='contact'))
sm.add_widget(ResultScreen(name='result'))
sm.add_widget(FilechooserScreen(name='filechooser'))



class DemoApp(MDApp):


    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_clsprimary_hue = '50'
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(navigation_helper)
        return screen

    dialog = None
    def show_alert_dialog(self):
        
            self.dialog = MDDialog(
                title = 'The Predicted Result is',
                text= 'asfasfa',
                buttons=[
                    MDRectangleFlatButton(text="OK", on_release=self.close),
                    ],
                )
            self.dialog.open()
            return ()

    def close(self, obj):
        self.dialog.dismiss()

    def selected(self, filechooser):
        self.load(filechooser.path, filechooser.selection)

    def load(self, path, selection):
        test_file=str(selection)
        test = test_file.replace("\\\\","/")
        test1 = test.replace("[","")
        test2 = test1.replace("]","")
        test3 = test2.replace("'","")
        getting_testvalue(test3)
        results = kcc()
        result=results[0]
        accuracy = results[1]
        print('THIS IS THE RESULT',result)
        print('THIS IS THE ACCURACY',accuracy)
    


DemoApp().run()