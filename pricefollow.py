from email import header
from bs4 import BeautifulSoup
import requests
import time
import smtplib

url='https: ***product link***'
headers={'User-Agent':'***user agent here***'}
 #It is necessary to enter a user agent so that the browser can understand us.What is my user agent => to search on Google.
def price_check():
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    #parsering to HTML code
    title=soup.find(id='***product-name***').getText().strip()
    #Where is product name in HTML codes?
    #Strip clears spaces.
    #getText clears <h1></h1> tags.
    print(title)
    span=soup.find(id="***offering-price***")
    #Where is price in HTML codes?
    content=span.attrs.get('content')
    price=float(content)
    print(price)
    if(price<***22000***):
        send_mail(title)
    #when the product's price is under 22000, this program sends mail

def send_mail(title):
    sender='***abcdfg@gmail.com***'
    receiver='***xyz@icloud.com***'
    try:
        server=smtplib.SMTP('smtp.gmail.com',587)
        #Gmail SMTP works on 587th port.
        server.ehlo()
        #ehlo starts server
        server.starttls()
        #line 32, for safely connection
        server.login(sender,'***Enter password this here***')
        #adding app password.Support: https://support.google.com/mail/answer/185833?hl=en
        subject=title,' \'s price dropped***'
        #Subject of mail
        body='Go to product=>*** '+ url
        #Body of mail
        mailContent=f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        #Mail content
        server.sendmail(sender,receiver,mailContent)
        print("***Mail was sent.***")
        #feedback (optional)
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while(1):
    price_check()
    time.sleep(60*60)
    #Loop always works because 1 is true. This situation true.
    #60 second * 60= 3600. To explain, this program controls in each 3600 second  

