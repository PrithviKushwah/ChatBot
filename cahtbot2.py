import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hi there"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. What's yours?"]
    ],
    [
        r"how are you?",
        ["I'm doing great. How about you?"]
    ],
    [
        r"(.*) your name?",
        ["My name is Chatbot"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ],
]

chatbot = Chat(pairs, reflections)


def run():
    st.title("Chatbot")
    st.markdown("Ask me anything!")
    user_input = st.text_input("You", "")
    if st.button("Send"):
        bot_response = chatbot.respond(user_input)
        st.text_area("Bot", bot_response)

run()