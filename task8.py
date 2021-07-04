#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("x")


if plate_no == "MP 23 LA 0682"
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : YASH SHARMA
    License No : 12432347910
    Make / Model : Skoda / OCtavia
    Registration Date : 3/1/2017
    Registering Authority : INDORE , MADHYA PRADESH 
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3FRE4538
    Chassis No : HMSURVWVQVJDIF
    Insurance Upto : 5/15/2022
    Fitness Upto : 4/8/2028
    </pre>''')
    print("</body>")

elif plate_no == "UP 11 AR 0364":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : AMIT PANDEY
    License No : 10942424321
    Make / Model : Skoda / Kodiaq
    Registration Date : 1/1/2019
    Registering Authority : MEERUT , UTTAR PRADESH
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N17344738
    Chassis No : HMSFHDSWVQSVWE
    Insurance Upto : 5/13/2024
    Fitness Upto : 5/8/2029
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
