try:
    with open('emails.txt','r') as file:
        for i in file:

except Exception as err:
    print(err)