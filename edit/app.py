from flask import Flask, render_template, request, Response
import requests, time, json, random, re
import Find
#------------------------------------------------------------------------------------------------------------------
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")
#---------------------------------------------------------------------------------------------------------------------
#Error from form
@app.route("/error")
def error():
    return render_template("Errordata.html")
#----------------------------------------------------------------------------------------------------------------------
@app.route("/back")
def back():
    return render_template("Form.html")
#----------------------------------------------------------------------------------------------------------------------
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        select =  request.form.getlist('Url')#ดึงข้อมูลของ Form จากหน้า Main.html
        url = (str(select).strip("[']"))
        pattern = r"(http|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?"
        print(url)
        if re.match(pattern,url):
            headers = {"User-Agent":"Chrome"}
            response = requests.get(url,headers=headers)
        #---------------------------------------------------------------------------------------------------------------
        #print(response)
        #----------------------------------------------------------------------------------------------------------------
            if (response.status_code == 200):
                Find.Url = url
                return render_template ("Form.html")
            else:
                return render_template("Main.html", result = "Can't Get" + url + "Please Choose Another Website.")
        else:
            return render_template("Main.html",result = "Missing schema http or https.")
#----------------------------------------------------------------------------------------------------------------------
@app.route("/form", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        requests = request.form
        print(requests)
        GetN = GetT = GetA = GetV = GetW = 0
        N = [] #Name
        T = [] #Tag
        A = [] #Attribute
        V = [] #Value
        W = [] #Widget
        #-------------------------------------------------------------------------------------------------------------
        #Create Number in Array
        for i,j in requests.items(): 
            if 'Name' in i:
                N.append('Name') #Name
                T.append('Name') #Tag
                A.append('Name') #Attribute
                V.append('Name') #Value
                W.append('Name') #Widget
        #-------------------------------------------------------------------------------------------------------------
        for i,j in requests.items():
            if 'Name' in i:
                N[GetN] = j
                GetN = GetN+1
            #Find Tag
            elif 'Tag' in i:
                T[GetT] = j.lower()
                GetT = GetT+1
            #Find Attribute
            elif 'Attr' in i:
                A[GetA] = j.lower()
                GetA = GetA+1
            #Find Value in Attribute
            elif 'Value' in i:
                V[GetV] = j
                GetV = GetV+1
            elif 'Widget' in i:
                W[GetW] = j
                GetW = GetW+1
        Find.Name = N #send N to Name in Find.py
        Find.Tag = T #send T to Tag in Find.py
        Find.Attri = A #send A to Attri in Find.py
        Find.Value = V #send V to Value in Find.py
        Find.Chart = W #send W to Chart in Find.py
    return render_template("Show.html")
#----------------------------------------------------------------------------------------------------------------------

def replace():
    Replace = Find.Getdata()
    Replace = [R.replace(',', '') for R in Replace]
    Replace = [R.replace('$', '') for R in Replace]
    return(Replace)

#----------------------------------------------------------------------------------------------------------------------
'''@app.route('/streamdata')
def stream():
    #name = Find.Name
    def generate_data():
        name = Find.Name
        widget = Find.Chart
        while True:
            data = replace()
            print(data)
            js = json.dumps({'Data' : data, 'Name' : name, 'Widget' : widget, 'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            #json_data = json.dumps({'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield f"data:{js}\n\n"
            time.sleep(1)
    return Response(generate_data(), mimetype="text/event-stream")'''
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
   app.run(debug = True)