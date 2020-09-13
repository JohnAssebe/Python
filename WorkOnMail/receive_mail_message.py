import imapclient
import pyzmail
imap_obj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
print('Enter legal account and password for login')
email_account=input('Enter Email account: (example@gmail.com)    ')
password=input('Enter Password: ')
imap_obj.login(email_account,password)
#If We Want to fetch and mark as read we should set readonly as False   
imap_obj.select_folder('INBOX',readonly=True)
elapsed_time=imap_obj.search(["From","upwork@e.upwork.com","UNSEEN"])
counter=0
messages=[]
for i in elapsed_time:
    counter+=1
    raw_message=imap_obj.fetch([i],['BODY[]','FLAGS'])
    message=pyzmail.PyzMessage.factory(raw_message[i][b'BODY[]'])
    messages.append(message)
print("You have "+str(counter)+"   Unseen Message(s) from Upwork")
for i in messages:
    print(i.get_addresses('from'))
    print("Subject: ",i.get_subject())
    print()
    if i.text_part!=None:
        print("Message Body Text Part:  "+i.text_part.get_payload.decode(i.text_part.charset))
##    if i.html_part!=None:
##        print("Message Body Html Part: ", i.html_part.get_payload().decode(i.html_part.charset))
##    print("Body:  ",i.get_body())
##    print("")
        
imap_obj.logout()
