Api_key = "Your Key here"


import openai

openai.api_key = Api_key

prompt = "First decide wether this mail is spam or real and then explain why:\nMail:\nI am Dr. Bakare Tunde, the cousin of Nigerian Astronaut, Air Force Major Abacha Tunde. "\
    "He was the first African in space when he made a secret flight to the Salyut 6 space station in 1979. "\
    "He was on a later Soviet spaceflight, Soyuz T-16Z to the secret Soviet military space station Salyut 8T in 1989. He was stranded there in 1990 when the Soviet Union was dissolved. "\
    "His other Soviet crew members returned to earth on the Soyuz T-16Z, but his place was taken up by return cargo. There have been occasional Progrez supply flights to keep him going since that time. He is in good humor, but wants to come home.\n" \
    "In the 14-years since he has been on the station, he has accumulated flight pay and interest amounting to almost $ 15,000,000 American Dollars. This is held in a trust at the Lagos National Savings and Trust Association. "\
    "If we can obtain access to this money, we can place a down payment with the Russian Space Authorities for a Soyuz return flight to bring him back to Earth. "\
    "I am told this will cost $ 3,000,000 American Dollars. In order to access the his trust fund we need your assistance.\n"\
    "Consequently, my colleagues and I are willing to transfer the total amount to your account or subsequent disbursement, since we as civil servants are prohibited by the Code of Conduct Bureau (Civil Service Laws) from opening and/ or operating foreign accounts "\
    "in our names.\n\n Needless to say, the trust reposed on you at this juncture is enormous. "\
    "In return, we have agreed to offer you 20 percent of the transferred sum, while 10 percent shall be set aside for incidental expenses (internal and external) between the parties in the course of the transaction."\
    "You will be mandated to remit the balance 70 percent to other accounts in due course.\n"\
    "Response:"


prompt2 = "We are working on a E-Comme"

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=40)

print(response)


