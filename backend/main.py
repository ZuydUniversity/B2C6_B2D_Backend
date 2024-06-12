from fastapi import FastAPI
from backend.models import Person, Report
from backend.database import SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# runnen met uvicorn = uvicorn backend.main:app --reload



#Commands:
#Enviroment= python -m venv env  Starten Enviroment= env\Scripts\activate.bat
#pip install fastapi uvicorn sqlalchemy pymysql
#pip install pytest and pip install pytest-mock

@app.get("/")
def read_root():
    return {"message": "Hello World"}

def create_report(db_session: Session, date, healthcomplaints, medicalhistory, diagnose): #run python -m backend.main
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

def read_report(db_session: Session, report_id):
    return db_session.query(Report).filter(Report.id == report_id).first()

def update_report(db_session: Session, report_id, date=None, healthcomplaints=None, medicalhistory=None, diagnose=None):
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

def delete_report(db_session: Session, report_id):
    report = db_session.query(Report).filter(Report.id == report_id).first()
    if report:
        db_session.delete(report)
        db_session.commit()
    return report

if __name__ == "__main__":
    db = SessionLocal()

    # Create
    # new_report = create_report(db, date="2024-05-29", healthcomplaints="Headache, nausea", medicalhistory="None", diagnose="Migraine2")
    # print(f"Created Report: {new_report.id}, {new_report.date}, {new_report.healthcomplaints}, {new_report.medicalhistory}, {new_report.diagnose}")

    # # Read
    report = read_report(db, 4)
    print(f"Read Report: {report.id}, {report.date}, {report.healthcomplaints}, {report.medicalhistory}, {report.diagnose}")

    # # Update
    # updated_report = update_report(db, 1, date="2024-06-01", healthcomplaints="Severe headache", diagnose="ok")
    # print(f"Updated Report: {updated_report.id}, {updated_report.date}, {updated_report.healthcomplaints}, {updated_report.medicalhistory}, {updated_report.diagnose}")

    # # Delete
    # delete_report(db, 2)
    # deleted_report = read_report(db, 2)
    # print(f"Deleted Report: {deleted_report}")  # Should be None if deleted

    db.close()


  