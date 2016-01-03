import random, smtplib, time, getpass

def main():
    login()
    
    name_email = {
        'gary':'',
        'kyle':'',
        'ishan':'',
        'kenna':'',
        'katie':'',
        'sean':'',
        'nick':''
    }
    people = list(name_email.keys())
    NUM_PEOPLE = len(people)

    #assign your people
    pairs = assignment(people[:], people[:])
    assert len(pairs) == NUM_PEOPLE
    for person in people:
        assert person in pairs.keys()
        assert person in pairs.values()

    display(pairs, name_email)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Main functions that do the work
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def assignment(givers,recipients):
    pairs = {}
    while givers and recipients:
        assert len(givers) == len(recipients)
        random.shuffle(givers)
        random.shuffle(recipients)
        g_cand, r_cand = givers[0], recipients[0]
        if g_cand != r_cand:
            givers.pop(0)
            recipients.pop(0)
            pairs[g_cand] = r_cand
    return pairs

def display(pairs, name_email):
    f = open('workfile.txt', 'w')

    for giver in pairs:
        recipient = pairs[giver]
        giver_email = name_email[giver]
        print()
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        pwe("TELL "+giver+" TO GET OVER HERE", True, False, False)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print()

        answer = prompt_loop("DID YOU GET OVER HERE?\n\tplease type: 'yes' OR 'not here'\n", ['yes', 'not here'])
        
        if answer.lower()=='yes':
            print_n("",100)
            print()
            print("****************************************")
            pwe(giver+", you're going to buy a gift for "+recipient, True, f, giver_email)
            print("****************************************")
            print()
            prompt_loop("DO YOU UNDERSTAND?\n\tplease type: 'yes'\n", ['yes'])
        else:
            pwe(giver+", you're going to buy a gift for "+recipient, False, f, giver_email)
            
        pwe(" ", True, f, False)
        print_n("", 10000)
    f.close()


###################################
#send email stuff
###################################
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()

def login():
    user = input("Email Address: ")
    password = getpass.getpass()
    try:
        server.login(user, password)
    except:
        print("INVALID USERNAME/PASSWORD COMBINATION. PLEASE TRY AGAIN.")
        login()
                                    
def send_email(destination, subject, msg):
    try:
        server.sendmail( 'Santa', destination , 'Subject: %s\n\n%s' % (subject, msg))
    except:
        return


###########################################
#printing helpers
###########################################
def pwe(msg, p=False, w=None, e=None):
    if p:
        assert type(p) is bool
        print(msg)
    if w:
        w.write(msg+'\n')
    if e:
        assert type(e) is str
        send_email(e,'Secret Santa', msg)

def print_n(str, n):
    for _ in range(n):
        print(str)

def prompt_loop(prompt, target):
    assert type(target) is list
    answer='null'
    while answer.lower() not in target:
        answer=input(prompt)
    return answer.lower()

    
if __name__ == '__main__':
    main()


