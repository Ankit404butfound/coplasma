from flask import Flask, request

app = Flask('app',static_url_path='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/home")
def home():
  return """<!DOCTYPE html>
<title>Details</title>
<head>
    <style>
        .text{
            text-align: right;
            
        }
        
        .center {
            width: 50%;
            padding: 100px;
            margin: 10px;
        }

        .nav{
            overflow: hidden;
            background-color: rgb(35, 36, 34);
        }

        .nav a{
            float: left;
            text-align: center;
            padding: 14px 16px;
            font-size: 17px;
            color: rgb(233, 233, 233);
            text-decoration: none;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        }

        .nav a:hover{
            background-color: rgb(153, 185, 123);
            color: rgb(24, 23, 23);
        }

        .nav a.active{
            background-color: rgb(72, 196, 72);
        }

        
    </style>
</head>
<body onload="swap_class()">
    <div class="nav">
        <a class="active" href="" id="home">HOME</a>
        <a href="reg" id="reg">REGISTER</a>
    </div>
    <div class="center">
        <div class="text">
            <form action="/action_page.php">
                <label for="fname">First name:</label>
                <input type="text" id="fname" name="fname"><br><br>
                <label for="lname">Last name:</label>
                <input type="text" id="lname" name="lname"><br><br>
                <label for="state">State:</label>
                <input type="text" id="state" name="state"><br><br>
                <label for="phn">Phone Number:</label>
                <input type="text" id="phn" name="phn"><br><br>
                <label for="bld">Blood Group:</label>
                <input type="text" id="bld" name="bld"><br><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
</body>"""


@app.route("/reg")
def reg():
  return """<!DOCTYPE html>
<title>Details</title>
<head>
    <style>
        .text{
            text-align: right;
            
        }
        
        .center {
            width: 50%;
            padding: 100px;
            margin: 10px;
        }

        .nav{
            overflow: hidden;
            background-color: rgb(35, 36, 34);
        }

        .nav a{
            float: left;
            text-align: center;
            padding: 14px 16px;
            font-size: 17px;
            color: rgb(233, 233, 233);
            text-decoration: none;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        }

        .nav a:hover{
            background-color: rgb(153, 185, 123);
            color: rgb(24, 23, 23);
        }

        .nav a.active{
            background-color: rgb(72, 196, 72);
        }

        
    </style>
</head>
<body onload="swap_class()">
    <div class="nav">
        <a href="" id="home">HOME</a>
        <a class="active" href="reg" id="reg">REGISTER</a>
    </div>
    <div class="center">
        <div class="text">
            <form action="/action_page.php">
                <label for="fname">First name:</label>
                <input type="text" id="fname" name="fname"><br><br>
                <label for="lname">Last name:</label>
                <input type="text" id="lname" name="lname"><br><br>
                <label for="state">State:</label>
                <input type="text" id="state" name="state"><br><br>
                <label for="phn">Phone Number:</label>
                <input type="text" id="phn" name="phn"><br><br>
                <label for="bld">Blood Group:</label>
                <input type="text" id="bld" name="bld"><br><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
</body>"""

if __name__ == '__main__':
  app.run(host= '0.0.0.0')
