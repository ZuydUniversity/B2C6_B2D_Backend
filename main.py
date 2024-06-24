from App import initializeApp
from App.Data.Database import SessionLocal
from App.Models.VerslagModel import Verslag
from App.Repos.VerslagRepo import VerslagRepo

app = initializeApp()

if __name__ == "__main__":
    db = SessionLocal()

    # Example usage of VerslagRepo methods
    repo = VerslagRepo(db)

    # # Create a new verslag
    # new_verslag = repo.add_verslag(date="2024-06-20", healthcomplaints="Headache", medicalhistory="None", diagnose="Migraine", zorgverlener_id=None, patient_id=None)
    # print(f"Created Verslag: {new_verslag.id}, {new_verslag.date}, {new_verslag.healthcomplaints}, {new_verslag.medicalhistory}, {new_verslag.diagnose}, {new_verslag.zorgverlener_id}, {new_verslag.patient_id}")

    # Read a verslag by ID
    report = repo.get_verslag(1)
    if report:
        print(f"Read Verslag: {report.id}, {report.date}, {report.healthcomplaints}, {report.medicalhistory}, {report.diagnose}, {report.zorgverlener_id}, {report.patient_id}")
    else:
        print("Verslag not found")

    # # Update a verslag
    # updated_verslag = repo.update_verslag(1, date="2024-06-21")
    # if updated_verslag:
    #     print(f"Updated Verslag: {updated_verslag.id}, {updated_verslag.date}, {updated_verslag.healthcomplaints}, {updated_verslag.medicalhistory}, {updated_verslag.diagnose}")
    # else:
    #     print("Verslag not found")

    # # Delete a verslag
    # deleted_verslag = repo.delete_verslag(2)
    # if deleted_verslag:
    #     print(f"Deleted Verslag: {deleted_verslag.id}, {deleted_verslag.date}, {deleted_verslag.healthcomplaints}, {deleted_verslag.medicalhistory}, {deleted_verslag.diagnose}")
    # else:
    #     print("Verslag not found")

    db.close()
