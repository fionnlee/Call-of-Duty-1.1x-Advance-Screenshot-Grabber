import flask
from fileinput import filename
from flask import *  
import os
from discordwebhook import Discord
import datetime
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
  
def replace(text):
    for ch in ['^0','^1','^2','^3', '^4', '^5', '^6', '^7' ]:
        if ch in text:
            text = text.replace(ch,"\\"+ch)  
    return text

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.form["player"])
        file1 = request.files['ss']
        path = os.path.join("upload", file1.filename)
        file1.save(path)
        name = replace(request.form["player"])
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        discord = Discord(url="https://discord.com/api/webhooks/1244157195386486864/glQwWkyen1efefBQlfW6bYlOjsxvPE3wzFggAeefefChH0rgNYGLHaoCefefZ1ndGnyISH6ihf6WvBG") #discord webhook
        discord.post(
                      embeds=[
                          {
                              "title": "Screenshot System",
                              "description": "",
                              "fields": [
                                  {"name": "Player Name", "value": f"{name}", "inline": True},
                                  {"name": "Player IP", "value": f"||{request.remote_addr}||", "inline": True},
        
                              ],
                              "thumbnail": {"url": f"https://media.licdn.com/dms/image/C5622AQFjCeGIpOPplQ/feedshare-shrink_800/0/1672941698199?e=2147483647&v=beta&t=8d0oUBF1bRVPcrtLLZ0_W_xHer79SOUs3OLMqIiDpBk"}, #custom thumbnail
                              "image": {"url": f"attachment://{file1.filename}"},
                              "footer": {
                                          "text": f"Date & Time : {date}",
                              },
                          }
                      ],
                      file={"file1": open(path, "rb")}
                  )
        return path
      
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=443) #add custom port. 443 added for testing
