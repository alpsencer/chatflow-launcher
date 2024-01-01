import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flox import Flox
import webbrowser

# -*- coding: utf-8 -*-
import urllib.parse


class HelloWorld(Flox):

    def query(self, prompt):
        if(self.settings.get('default_model')):
            model = self.settings.get('default_model')
        else:
            model = 'text-davinci-002-render-sha'
        encoded_prompt = urllib.parse.quote(prompt)  # URL encode the prompt
        openai_chat_url = f"https://chat.openai.com/?model={model}&prompt={encoded_prompt}"  # Construct the URL with both parameters

        return [
            {
                "Title": f"OpenAI Chat with Model: '{model}' and Prompt: '{prompt}'",
                "SubTitle": "Press Enter to open in OpenAI Chat",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": [openai_chat_url]  # Pass the constructed URL
                }
            }
        ]

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    HelloWorld()
