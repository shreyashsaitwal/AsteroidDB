# from datetime import datetime
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
        

class TinyWebDB(db.Model):
    __tablename__ = 'tinywebdb'
    tag = db.Column(db.String, primary_key=True, nullable=False)
    value = db.Column(db.String, nullable=False)
    # The 'date' column is needed for deleting older entries, so not really required
    # date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


db.create_all()
db.session.commit()

@app.route('/')
def hello_world():
    return ''


# -------------------------
#  Store Value
#  - Store a value by using tag.
# -------------------------
@app.route('/store', methods=['POST'])
def store_a_value():
    tag = request.form['tag']
    value = request.form['value']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return 'Security error: Not possible to do any action to password record!'
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return 'Wrong password!'
            # --------------------
            existing_tag = TinyWebDB.query.filter_by(tag=tag).first()
            if existing_tag:
                existing_tag.value = value
                db.session.commit()
            else:
                data = TinyWebDB(tag=tag, value=value)
                db.session.add(data)
                db.session.commit()
        return jsonify(['STORED', tag, value])
    return 'Invalid Tag!'


# -------------------------
#  Get Value
#  - Get the value from tag.
# -------------------------
@app.route('/get', methods=['POST'])
def get_value():
    tag = request.form['tag']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return 'Security error: Not possible to do any action to password record!'
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return 'Wrong password!'
            # --------------------
            value = TinyWebDB.query.filter_by(tag=tag).first().value
            return jsonify(['VALUE', tag, value])
    return 'Invalid Tag!'


# -------------------------
#  Delete Record
#  - Delete a record from tag.
# -------------------------
@app.route('/delete', methods=['POST'])
def delete_entry():
    tag = request.form['tag']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if tag:
        if tag == 'dbpass':
            return 'Security error: Not possible to do any action to password record!'
        else:
            # --------------------
            if getpassword:
                password = request.form['pass']
                if password != getpassword.value:
                    return 'Wrong password!'
            # --------------------
            deleted = TinyWebDB.query.filter_by(tag=tag).first()
            db.session.delete(deleted)
            db.session.commit()
            return jsonify(['DELETED', tag])
    return 'Not found the tag!'


# -------------------------
#  Set/Change Password
#  - If you set a password, you need to type a password when you modify the database.
#  - The password will be saved in the same table along with other data called "dbpass".
#  - If you forgot the password, there is no way to recover it.
# -------------------------
@app.route('/auth/password', methods=['POST'])
def set_key():
    newpassword = request.form['newpass']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if newpassword:
        if getpassword:
            oldpassword = request.form['oldpass']
            if getpassword.value == oldpassword:
                getpassword.value = newpassword
                db.session.commit()
                return jsonify(['CHANGED PASSWORD', newpassword])
            else:
                return 'Wrong old password!'
        else:
            data = TinyWebDB(tag='dbpass', value=newpassword)
            db.session.add(data)
            db.session.commit()
            return jsonify(['SET PASSWORD', newpassword])
    return 'No new password is specified!'


# -------------------------
#  Get All Tags
#  - Return all values
# -------------------------
@app.route('/getall', methods=['POST'])
def get_all():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        # --------------------
        password = request.form['pass']
        if password != getpassword.value:
            return 'Wrong password!'
        # --------------------
    tags = TinyWebDB.query.filter_by().all()
    return tags


# -------------------------
#  Remove Password
#  - If you type your current password, requests won't require pass parameter anymore. And your password will be deleted.
# -------------------------
@app.route('/auth/unlock', methods=['POST'])
def remove_key():
    password = request.form['pass']
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        if getpassword.value == password:
            deleted = TinyWebDB.query.filter_by(tag='dbpass').first()
            db.session.delete(deleted)
            db.session.commit()
            return jsonify(['DELETED PASSWORD', password])
        else:
            return 'Wrong password!'
    return 'You need to set a password first to use this feature!'
        

# -------------------------
#  Is Locked?
#  - Gives information about current lock status.
# -------------------------
@app.route('/islocked')
def is_locked():
    getpassword = TinyWebDB.query.filter_by(tag='dbpass').first()
    if getpassword:
        return jsonify(['IS LOCKED', 'true'])
    else:
        return jsonify(['IS LOCKED', 'false'])
        

if __name__ == '__main__':
    app.run()
