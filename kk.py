from flask import Flask, render_template
import speech_recognition as sr
import sqlite3

app = Flask(__name__)
#
# videoFound ="https://a.top4top.io/m_1785994ep1.mp4"

# # create db
# db = sqlite3.connect("table1.db")
# # delete the # from 2 line below for create the db then return it back for triaing something
# db.execute("CREATE TABLE ArSL(word varchar(20) not null primary key ,video mediumblob not null )")
# db.execute("DROP TABLE ArSL")
# cur = db.cursor()
#
# cur.execute("insert into ArSL(word , video ) values ('مرحبا','https://a.top4top.io/m_1785994ep1.mp4')")

def getstr():
    wt = ""  # for store the word
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    try:
        print("You said: " + r.recognize_google(audio, language="ar-AR"))
        wt = r.recognize_google(audio, language="ar-AR")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    db = sqlite3.connect("table1.db")

    # delete the # from 2 line below for create the db then return it back for triaing something
    # db.execute("CREATE TABLE ArSL(word varchar(20) not null primary key ,video mediumblob not null  )")
    cur = db.cursor()

    cur.execute("select video from table1 where word='" + wt + "'")
    v = cur.fetchone()  # for store video link
    sv = str(v)  # from list to string
    p = sv.split("'")[1]
    print(p)
    return p

# rm = sv.translate({ord(i): None for i in "[(,)]'"})  # remove [(,)] from the fetch link
#
@app.route('/')
def showvideo():
    return render_template('home.html', videoFound = getstr())
if __name__ == '__main__':
    app.run(debug=True)
