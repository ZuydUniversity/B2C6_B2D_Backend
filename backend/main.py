from fastapi import FastAPI
from models import Person 
from models import Report
from database import Sessionlocal

app = FastAPI() # standaard webserver runnen met uvicorn --> uvicorn main:app --reload

#Commands:
#Enviroment= python -m venv env  Starten Enviroment= env\Scripts\activate.bat
#pip install fastapi uvicorn sqlalchemy pymysql



@app.get("/")
def read_root():
    return "hello world"

#De Create function voor report
def create_report(db_session, date, healthcomplaints, medicalhistory, diagnose):
    report = Report(
        date=date, 
        healthcomplaints=healthcomplaints, 
        medicalhistory=medicalhistory, 
        diagnose=diagnose
    )
    db_session.add(report)
    db_session.commit()
    db_session.refresh(report)
    return report

#De read functie voor report
def read_report(db_session, report_id):
    return db_session.query(Report).filter(Report.id == report_id).first()

#De update functie voor report
def update_report(db_session, report_id, date=None, healthcomplaints=None, medicalhistory=None, diagnose=None):
    report = db_session.query(Report).filter(Report.id == report_id).first()
    if report:
        if date:
            report.date = date
        if healthcomplaints:
            report.healthcomplaints = healthcomplaints
        if medicalhistory:
            report.medicalhistory = medicalhistory
        if diagnose:
            report.diagnose = diagnose
        db_session.commit()
        db_session.refresh(report)
    return report

#De delete functie voor report
def delete_report(db_session, report_id):
    report = db_session.query(Report).filter(Report.id == report_id).first()
    if report:
        db_session.delete(report)
        db_session.commit()
    return report


if __name__ == "__main__": # eerst je database opzetten en dan runnen met python main.py
    db = Sessionlocal()


    #Create
    new_report = create_report(db, date="2024-05-29", healthcomplaints="Headache, nausea", medicalhistory="None", diagnose="Migraine")
    print(f"Created Report: {new_report.id}, {new_report.date}, {new_report.healthcomplaints}, {new_report.medicalhistory}, {new_report.diagnose}")

    #Read
    report = read_report(db, 1)
    print(f"Read Report: {report.id}, {report.date}, {report.healthcomplaints}, {report.medicalhistory}, {report.diagnose}")

    # Update
    updated_report = update_report(db, 1, date="2024-06-01", healthcomplaints="Severe headache", diagnose="ok")
    print(f"Updated Report: {updated_report.id}, {updated_report.date}, {updated_report.healthcomplaints}, {updated_report.medicalhistory}, {updated_report.diagnose}")

    # Delete
    delete_report(db, 2)
    deleted_report = read_report(db, 2)
    print(f"Deleted Report: {deleted_report}")  # Should be None if deleted

    db.close()
# @app.get("/persons")
# hier moet je de database gegevens ophalen met een query get all 


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}