try:
    with open('emails.txt', 'r') as infile:
        with open('gmail.txt', 'a') as outfile:
            for i in infile:
                i: str = i
                if i.endswith('@gmail.com\n'):
                    outfile.write(i.split()[-1] + '\n')
except Exception as err:
    print(err)
