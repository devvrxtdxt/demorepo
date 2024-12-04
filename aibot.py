import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq

# Initialize the agent with the Groq model
agent = Agent(
    model=Groq(id="mixtral-8x7b-32768", api_key="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"),
    markdown=True
)

# Set the title of the Streamlit app
st.title("AI Assistant Chatbot")

# Create a text input for the user to enter a prompt
prompt = st.text_input("Enter a prompt to search the web :")

# Create a button to generate the story
if st.button("Generate"):
    if prompt:
        # Generate the story using the agent
        response = agent.print_response(prompt)
        # Display the generated story
        st.markdown(response)
    else:
        st.warning("Please enter a prompt to search the web.")