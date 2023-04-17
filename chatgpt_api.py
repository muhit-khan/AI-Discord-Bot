import openai

API_KEY = "sk-Iq81CU9##################8tcWSlgTpnVg" # replace with your API KEY
openai.api_key = API_KEY

def chatGPTResponse(conversation):   #function to generates the response of Chatgpt
    try:
        response = openai.ChatCompletion.create(
            model ='gpt-3.5-turbo',
            messages = conversation
        )
    except openai.error.APIConnectionError:
        return None

    conversation.append({'role': response.choices[0].message.role,'content':response.choices[0].message.content})
    return conversation 
def initializeConversation(): 
    global conversation  
    conversation = []
    conversation.append({'role':'system','content':'how may I help you?'})
    conversation=chatGPTResponse(conversation)

def getResponse(prompt):
    global conversation
    conversation.append({'role':'user','content':prompt})
    conversation = chatGPTResponse(conversation)

    return conversation[-1]['content'].strip()