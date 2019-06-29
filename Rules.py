import base64
import requests
import json


def speech_recognition():
    #Reconnaisance vocale
    with open('input.wav', 'rb') as input:
        content=input.read()
        query_audio = base64.b64encode(content)
        query_audio=str(query_audio)[2:-1]
    req="""{
    "audio": {
      "content": "%s"
     },
     "config": {
      "encoding": "LINEAR16",
      "languageCode": "en-US"
     }
    }"""%(query_audio)
    json_request=json.loads(req)
    resp = requests.post('https://speech.googleapis.com/v1/speech:recognize?key=INSERT_YOUR_HASH_HERE', json=json_request)
    #print("Code de reconnaissance vocale : ", resp.status_code)
    confidence = resp.json()["results"][0]["alternatives"][0]["confidence"]
    #print("Indice de confiance = ", confidence)
    query_text=resp.json()["results"][0]["alternatives"][0]["transcript"]
    #print("Texte traduit : ", query_text)

    return query_text

def search_for_answer(query_text):

    #DialogFlow

    #header={'Authorization': 'Bearer CODE'}
    req="""{
    "lang": "en",
    "query": "%s",
    "sessionId": "12345",
    "timezone": "Europe/Paris"
    }"""%(query_text)
    json_request=json.loads(req)
    resp = requests.post("https://api.dialogflow.com/v1/query?v=20170712", headers=header, json=json_request)
    #print("Code de DialogFlow : ", resp.status_code)
    response_text=resp.json()["result"]["fulfillment"]["speech"]
    #print("Réponse de DialogFlow : ", response_text)

    return response_text



def speech_synthesis(response_text):
    #Synthese vocale avec GoogleSpeech, en utilisant la méthode WaveNet
    req="""{
     "input": {
      "text": "%s"
     },
     "audioConfig": {
      "audioEncoding": "LINEAR16",
      "pitch": 0,
      "speakingRate": 1
     },
     "voice": {
      "languageCode": "en-US",
      "name": "en-US-Wavenet-D"
     }
    }"""%(response_text)
    json_request=json.loads(req)
    resp = requests.post('https://texttospeech.googleapis.com/v1/text:synthesize?key=INSERT_YOUR_HASH_HERE', json=json_request)
    #print("Code de synthese vocale : ", resp.status_code)
    audio_raw=resp.json()["audioContent"]

    with open('output.wav', 'wb') as out:
        out.write(base64.b64decode(audio_raw))
        #print('Audio content written to file "output.wav"')
        return True