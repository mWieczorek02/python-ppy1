import re

if __name__ == "__main__":
    raw_text = 'Wyślij email na adres: info@template.com lubsales-info@template.it'

    email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', raw_text)

    print(email)
