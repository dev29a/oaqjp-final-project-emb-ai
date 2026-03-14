import requests, json
"""this will be a module"""

formatted_response = {}

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    # return response.text  # Return the response text from the API
    formatted_data = json.loads(response.text)
    # return formatted_response
    formatted_response = formatted_data['emotionPredictions'][0]['emotion']
    max_emotion_score = max(formatted_data['emotionPredictions'][0]['emotion'].values())

    temp_data = {}

    for emotion, score in formatted_data['emotionPredictions'][0]['emotion'].items():
        if ( score ==  max_emotion_score):
            temp_data['dominant_emotion'] = emotion
            
    
    return formatted_response | temp_data