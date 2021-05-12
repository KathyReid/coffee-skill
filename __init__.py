from mycroft import MycroftSkill, intent_file_handler


class Coffee(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('coffee.intent')
    def handle_coffee(self, message):
        self.speak_dialog('coffee')


def create_skill():
    return Coffee()

