# code to connect with chatgpt and send the prompt 

import openai


def get_response(prompt_input):
    
    api_key = "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"

     
    model_engine = "text-davinci-002" # You can change this if you prefer a different model

    
    prompt_input = "python code : " + prompt_input
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_input
    )


    

    return response

    