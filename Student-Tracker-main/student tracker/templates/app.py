from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route("/")
def home():
    return render_template("home1.html")


@app.route("/student page")
def student():
    return render_template("studentlogin.html")


@app.route("/competition page")
def comppage():
    return render_template('competition page.html')


@app.route("/studreg")
def studreg():
    return render_template("Reg.html")


@app.route("/studportal")
def studportal():
    return render_template("stdptl.html")


@app.route("/bio page")
def biography():
    return render_template("bio.html")


@app.route("/Time Table")
def timetable():
    return render_template("tt.html")


@app.route("/student mark")
def studentmark():
    return render_template("stumar.html")


@app.route("/attendance")
def attendance():
    return render_template("att.html")


@app.route("/today's attendance")
def todattendance():
    return render_template("todatt.html")


@app.route("/general details")
def gendetails():
    return render_template("gen.html")


@app.route("/contact us")
def contactus():
    return render_template("cont.html")


@app.route("/fees details")
def feedetails():
    return render_template("fee.html")


@app.route("/transport details")
def transportdetails():
    return render_template("trans.html")


@app.route("/feedback")
def feedback():
    return render_template("fdb.html")


@app.route("/contactus")
def contact_us():
    return render_template("cont.html")


@app.route("/staff")
def staff():
    return render_template("staff.html")


@app.route("/profpage")
def staff_profilepage():
    return render_template("profile page.html")


@app.route("/admin page")
def admin():
    return render_template('adminlogin.html')


@app.route("/admin portal")
def adminportal():
    return render_template("admin portal.html")


@app.route('/student register')
def student_register():
    return render_template("student register.html")


@app.route("/teacher register")
def teacher_register():
    return render_template('teacher register.html')


if __name__ == '__main__':
    app.run(debug=True)
