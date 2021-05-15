from chatbot import Chat, register_call
import wikipedia


@register_call("end_session")
def end_session(session, query):
    print('Ok Thanks for checking in.')
    exit()


def acquire_chatbot():
    return Chat("./script.template", default_template='./default.template')


if __name__ == '__main__':
    acquire_chatbot().converse('Hi, how are you?')