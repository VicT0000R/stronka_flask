from flask import session, current_app
from db.models import Users
from db import db

def user_exists(req):
    with current_app.app_context():
        user = Users.query.filter_by(login=req['login']).first()
        if not user:
            return False, "Użytkownik o podanym loginie nie istnieje."
        if user.password != req['password']:
            return False, "Niepoprawne hasło."
        
        session['name'] = user.name
        session['surname'] = user.surname
        return True, ""
    

def create_user(req):
    with current_app.app_context():
        user = Users.query.filter(Users.name == req['name'], Users.surname == req['surname']).first()
        if user:
            return False, "Dany użytkownik już istnieje."
        else: 
            login= f"{req['name']}.{req['surname']}"

            new_user = Users(
            name = req['name'],
            surname = req['surname'],
            login= login,
            email=req['email'],  
            password=req['password'], 
            )
            db.session.add(new_user)
            try:
                db.session.commit()
                print("Użytkownik został pomyślnie utworzony.")
                session['name'] = new_user.name
                session['surname'] = new_user.surname
            except Exception as e:
                # W przypadku błędu wykonujemy rollback
                db.session.rollback()
                return False, f"Wystąpił błąd: {str(e)}"
            

            
            return True, ""