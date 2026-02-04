# from textblob import TextBlob

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self,texto):
        
#         analisis = TextBlob(texto)
        
#         if analisis.sentiment.polarity > 0:
            
#             return f'Polarity:{analisis.sentiment.polarity} = Positivo'
        
#         elif analisis.polarity == 0:
            
#             return f'Polarity:{analisis.sentiment.polarity} = Neutro'
            
#         else:
            
#             return f'Polarity:{analisis.sentiment.polarity} = negativo'
    
# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimiento("IM so bad im gonna push some body")
# print(resultado)

from openai import OpenAI

client = OpenAI()
api_key = ''

OpenAI.api_base = api_key

system_rol = '''Imagine you're a sentiment analyzer.
I'll send you sentiments, and you'll analyze the sentiment of the messages.
Then you'll give me a response with at least one character and no more than four characters.
ONLY NUMERICAL RESPONSES. Where -1 is maximum negativity, 0 is neutral, and 1 is maximum positivity.
(You can only respond with inst or floats)'''  

messages = [{"role": "system", "content": system_rol}]

class SentimentAnalyzer:
    def analyze_sentiments( self, polarity ):
        
        if polarity <= -0.6:
            return "\x1b[1;31m" + "Very negative" + "\x1b[0;37m"
        elif polarity <= -0.3:
            return "\x1b[1;31m" + "Negative" + "\x1b[0;37m"
        elif polarity <= -0.1:
            return "\x1b[1;31m" + "Few negative" + "\x1b[0;37m"
        elif polarity < 0.1:
            return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polarity < 0.4:
            return "\x1b[1;32m" + "Few positive" + "\x1b[0;37m"
        elif polarity < 0.9:
            return "\x1b[1;32m" + "Positive" + "\x1b[0;37m"
        else:
            return "\x1b[1;32m" + "Very Positive" + "\x1b[0;37m"
        
        

while True:
    user_prompt = input("\x1b[1;32m" + "\nTell me something...\n" + "\x1b[0;37m")
    messages.append({"role": "user", "content": user_prompt})
    
    completion = client.responses.create(
    model="gpt-4o-mini",
    input=messages,
    max_output_tokens=100
    )
    
    response = completion.choices[0].message["content"]
    
    messages.append({"role": "assistant", "content": response })
    
    sentimen = SentimentAnalyzer(float(response))
    
    
    


