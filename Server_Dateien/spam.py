import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import joblib
import nltk
from keras.models import load_model
nltk.download('wordnet')
from io import StringIO
import sys
import email
from datetime import datetime

object = joblib.load("/home/filter/miscellaneous.pkl")
cv = object[0]
regexp = object[1]
wnl = object[2]
stopWords = object[3]

model = load_model("/home/filter/keras_model")

mail = sys.stdin.read()

message = email.message_from_string(mail)

for part in message.walk():
	if part.get_content_type() == 'text/plain':
		body = part.get_payload(decode=True)

content = body.decode('utf-8')

tokenized_content = regexp.tokenize(content)

text = ""
for i in tokenized_content:
    if i not in stopWords:
        lemm = wnl.lemmatize(i)
        text += lemm + " "

string_io = StringIO(text)
feature = cv.transform(string_io)

prediction = model.predict(feature, verbose=0)[0][0]

if prediction > 0.5:
	message.add_header('X-Spam-Flag', 'YES')
	modified_mail = message.as_string()
	modified_mail = modified_mail.replace("X-Spam-Flag: NO", "X-Spam-Flag: YES") #Trick 17

with open("/home/filter/error.log", "a") as f:
	f.write(f"{str(datetime.now())} - Prediction: {prediction} - Text: {content}\n    {message.as_string()}\n\n\n\n")

modified_mail = message.as_string()

sys.stdout.write(modified_mail)
sys.stdout.flush()

