from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Trang đăng nhập
@app.route("/")
def index():
    return render_template("index.html")


# Trang chủ admin
@app.route("/admin")
def admin():
    return render_template("trangchu1.html")


# Trang chủ sinh viên
@app.route("/student")
def student():
    return render_template("trangchu2.html")


# Quản lý tài khoản
@app.route("/quanly_taikhoan")
def quanly_taikhoan():
    return render_template("quanly_taikhoan.html")


# Thêm tài khoản và lưu CSV
@app.route("/them_taikhoan", methods=["POST"])
def them_taikhoan():

    username = request.form["username"]
    password = request.form["password"]
    role = request.form["role"]

    with open("taikhoan.csv","a",newline="",encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([username,password,role])

    return "Thêm tài khoản thành công"


# Đăng ký học lại
@app.route("/dangky", methods=["POST"])
def dangky():

    mssv = request.form["mssv"]
    monhoc = request.form["monhoc"]

    with open("dangky.csv","a",newline="",encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([mssv,monhoc])

    return "Đăng ký thành công"


if __name__ == "__main__":
    app.run(debug=True)