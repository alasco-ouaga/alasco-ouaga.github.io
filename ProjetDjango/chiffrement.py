from email import message


def chiffrementMessage(lettre,maclee):

    maliste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    malistegrand=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range(len(maliste)):
        if lettre =='':
            return ''
        elif maliste[i]==lettre :
            return str(maliste[(i+maclee)%26])

    for i in range(len(malistegrand)):
        if lettre =='':
            return ''
        elif malistegrand[i]==lettre :
            return str(malistegrand[i+maclee])

    return lettre

   

def chiffrement(message,maclee):

    messageChiffrer = str()
    for lettre in message :
        messageChiffrer += chiffrementMessage(lettre, maclee)

    return messageChiffrer 

print(chiffrement("aa",3))