import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flox import Flox
import json
import os
import urllib.parse
import webbrowser
from pathlib import Path

class ChatFlowLauncher(Flox):
    def __init__(self):
        super().__init__()
        self.model = self.settings.get("default_model", "gpt-3.5")

    def query(self, prompt):
        # Choose the model based on the prompt
        if(self.model == "gpt-3.5"):
            model = "text-davinci-002-render-sha"
        model = "gpt-4" if prompt.startswith("4 ") else model
        prompt = prompt.lstrip("4 ")
        encoded_prompt = urllib.parse.quote(prompt)  # URL encode the prompt
        openai_chat_url = f"https://chat.openai.com/?model={model}&prompt={encoded_prompt}"  # Construct the URL with both parameters
        if(model == "text-davinci-002-render-sha"):
            visible_model = "GPT 3.5"
        elif(model == "gpt-4"):
            visible_model = "GPT 4"
        self.add_item(
            title=f"Chat with: '{visible_model}' and Prompt: '{prompt}'",
            subtitle="Press Enter to open in OpenAI Chat",
            icon="Images/app.png",
            method=self.open_url,
            parameters=[openai_chat_url]
        )
        return

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    ChatFlowLauncher()
