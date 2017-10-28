import nltk

texto = 'sse tipo de informação pode e já está sendo colhida por governos e empresas para ajustarem seus discursos afim de aproximar de eleitores e clientes, alcançando assim o objetivo desejado. Coincidência ou não 2 meses após o primeiro discurso pedindo tolerância ao povo, em um segundo discurso sobre o radicalismo contra islamitas, Obama se baseou na única parte de seu primeiro discurso que surtiu o efeito esperado, quando pontuou que islamistas são os nossos vizinhos, bombeiros, atletas e cientistas que fazem parte de nosso dia a dia. Já assistiu House Of Cards ? Parece que o uso de Big Data por Conway e Underwood para manipular os eleitores na quarta temporada não é tão ficção cientifica assim...'
frases = nltk.tokenize.sent_tokenize(texto)
print(frases)

tokens = nltk.word_tokenize(texto)
print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

entidades = nltk.chunk.ne_chunk(classes)
print(entidades)