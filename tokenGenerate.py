import pypyodbc
import requests
import json

# -------- TOKEN GENERATE -------- #

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-******\SQLEXPRESS;' #Just use symbols.
    'Database=*******;'
    'UID=******;'
    'PWD=******;'
)
curs = db.cursor()

url = "URL_ADDRESS"

payload = 'USERNAME_PASSWORD'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'CODE'
}

response = requests.request("GET", url, headers=headers, data=payload)
con = response.content
jsonVariable = json.loads(con)

tokenList = []
tokenList.append(jsonVariable)
print(tokenList)
curs.execute("TRUNCATE TABLE Token")
komut = 'INSERT INTO Token VALUES(?,?)'
datas = (
    tokenList[0]['access_token'], tokenList[0]['token_type'])
sonuc = curs.execute(komut, datas)
db.commit()
