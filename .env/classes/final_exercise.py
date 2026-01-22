from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,texto):
        
        analisis = TextBlob(texto)
        
        if analisis.sentiment.polarity > 0:
            
            return f'Polarity:{analisis.sentiment.polarity} = Positivo'
        
        elif analisis.polarity == 0:
            
            return f'Polarity:{analisis.sentiment.polarity} = Neutro'
            
        else:
            
            return f'Polarity:{analisis.sentiment.polarity} = negativo'
    
analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento("IM so bad im gonna push some body")
print(resultado)