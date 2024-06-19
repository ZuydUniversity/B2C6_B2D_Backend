from App import initializeApp
from App.Data.Database import SessionLocal
from App.Data.DatabaseModels import Verslag
from App.Repos.VerslagRepo import VerslagenRepo

app = initializeApp()

if __name__ == "__main__":
    db = SessionLocal()

    # Create
    new_report = VerslagenRepo.add_verslag(db, date="2024-05-29", healthcomplaints="Headache, nausea", medicalhistory="niets", diagnose="Migraine2")
    print(f"Created Report: {new_report.id}, {new_report.date}, {new_report.healthcomplaints}, {new_report.medicalhistory}, {new_report.diagnose}")

    # # Read
    # report = read_report(db, 4)
    # print(f"Read Report: {report.id}, {report.date}, {report.healthcomplaints}, {report.medicalhistory}, {report.diagnose}")

    # # Update
    # updated_report = update_report(db, 1, date="2024-06-01", healthcomplaints="Severe headache", diagnose="ok")
    # print(f"Updated Report: {updated_report.id}, {updated_report.date}, {updated_report.healthcomplaints}, {updated_report.medicalhistory}, {updated_report.diagnose}")

    # # Delete
    # delete_report(db, 2)
    # deleted_report = read_report(db, 2)
    # print(f"Deleted Report: {deleted_report}")  # Should be None if deleted

    db.close()
