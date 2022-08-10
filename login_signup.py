import json
def my():
    user=input("enter login or signup:")
    if user=="signup":
        a=input("enter user name:")
        password=input("enter the password:")
        l,b,c,d=0,0,0,0
        special_chr="@ _ ! # $ % ^ & * ( ) < > ? / \ | { } ~ :"
        p=len(password)
        for i in password:
            if i.isupper():   
                l+=1
            if i.islower():
                b+=1
            if i.isdigit():
                c+=1
            if i in special_chr :
                d+=1
        if p>=6:
            if l>=1 and b>=1 and c>=1 and d>=1 :
                    print("strong password")
                    password2=input("enter the password again:")
                    if password==password2:
                        print("confirm password")
                        dic={}
                        b=[]
                        d={}
                        d1={}
                        dic["username"]=a
                        dic["password"]=password
                        d["description"]=input("enter the description : ")
                        d["D.O.B"]=input("enter your D.O.B : ")
                        d["Gender"]=input("enter your gender : ")
                        d["Hobbies"]=input("enter your hobbies : ")
                        dic["Profile"]=d
                        b.append(dic)
                        d1["user"]=b
                        file=open("Signup.json","w+")
                        json.dump(d1,file ,indent=4)
                        file.close()
                        print("Signup Succesfully")
                    else:
                        print("both the password are not same")
            else:
                print("invilid")
                print("password should contain atleast one special chr, number, uppercase, lowercase")
        else:
            print("password should contain atleast 6 chr")

    elif user=="login":
        a=open("Signup.json","r")                 
        f=json.load(a)
        name=input("Enter your user name for login:")
        loginpassword=input("Enter your password for login:")
        for i in f["user"]:
            if name==i['username']:
                if loginpassword==i['password']:
                    print("Login successful")
                    print(i)
                    break
                else:
                    print("Check your password")
            else:
                
                print("Check your username")
    else:
        print("you can't login/signup")
my()
            