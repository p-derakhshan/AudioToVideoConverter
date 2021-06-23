class Tools:
    def annotation_remover():
        #get text file address
        text_dir = text_dir.translate({ord(i): None for i in "!?.,:)|(;#%^*-_=+][}{\/"})
        text_dir = text_dir.replace('@', 'atsign')
        text_dir = text_dir.replace('$', 'dollar')
        text_dir = text_dir.replace('&', 'and')