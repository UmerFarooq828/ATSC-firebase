import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyCFZuOq8frL2tbLepZvOF8woMBfm_tYtlQ",
  "authDomain": "fir-demo-a0603.firebaseapp.com",
  "databaseURL": "https://fir-demo-a0603-default-rtdb.firebaseio.com",
  "projectId": "fir-demo-a0603",
  "storageBucket": "fir-demo-a0603.appspot.com",
  "messagingSenderId": "772314080216",
  "appId": "1:772314080216:web:227d742f3da942dd5188ad",
  "measurementId": "G-SXRD3JEGXB"
}

firebase= pyrebase.initialize_app(firebaseConfig)

db=firebase.database()


#push data

#data={"Deadline":"2pm","name":"Paper"}

#db.child("todolistB").child("Tuesday").push(data)

#------------updating
#db.child("todolistA").child("Monday").child("paper").update({"Deadline":"3pm"})

#data={  "todolistA/Monday/paper":{"Deadline":"12pm"},
#        "todolistA/Tuesday/pull-request":{"Deadline":"12pm"} ,
#        "todolistA/Wednesday/project":{"Deadline":"12pm"}}
#db.update(data)

#updating automatically genertaed keys

#monday_tasks=db.child("todolistB").child("Tuesday").get()


#for task in monday_tasks.each():
    #print(task.val())
    #print(task.key())
 #   if(task.val()["name"]=="Paper"):
  #      key=task.key()


#db.child("todolistB").child("Tuesday").child(key).update({"Deadline":"9pm"})
#create your own key
#data={"age":"21","address":["NY","LA"]}
#db.child("john").set(data)#creating a path to data

#retreiving Data
#  
auth=firebase.auth()
storage=firebase.storage()

output=db.child("todolistA").shallow().get()
print(output.val())

#for user in output.each():
 #   print(user.val())