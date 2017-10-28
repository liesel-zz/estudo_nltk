import nltk



base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia esta muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]


# stopwords sao palavras que nao ajudam a caracterizar um sentimento e por isso podem ser descartadas
# O NLTK ja possuia um pacote de palavras de já classificadas previamente como stopwords então podemos utiliza-las para definir nossas stopwords
stopWordsNltk = nltk.corpus.stopwords.words('portuguese')


def removeStopWords(texto):
    quotes = []
    for(words, emotion) in texto:
        noStopWords = [p for p in words.split() if p not in stopWordsNltk]
        quotes.append((noStopWords,emotion))
    return quotes
print(removeStopWords(base))