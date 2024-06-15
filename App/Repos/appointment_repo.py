from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from App.Data import databaseModels as dbmodels
from ..Models.appointment_model import Appointment

class AppointmentRepo:

    def get_appointments(db: Session):
        appointments = db.query(dbmodels.Appointment).all()
        for appointment in appointments:
            appointment.decrypt()
        return appointments
    
    def get_appointment_by_id(id: int, db: Session):
        appointment = db.query(dbmodels.Appointment).filter(dbmodels.Appointment.id == id).first()
        if not appointment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Appointment with id: {id} does not exist")
        appointment.decrypt()
        return appointment
    
    def create_appointment(appointment: Appointment, db: Session):
        new_appointment = dbmodels.Appointment(**appointment.model_dump())
        new_appointment.encrypt()

        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return new_appointment
    
    def update_appointment(id: int, appointment: Appointment, db: Session):
        appointment.id = id
        query = db.query(dbmodels.Appointment).filter(dbmodels.Appointment.id == id)
        existing_appointment = query.first()
        if existing_appointment == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Appointment with id: {id} does not exist")

        existing_appointment.decrypt()

        updated_values = appointment.model_dump()
        for key, value in updated_values.items():
            setattr(existing_appointment, key, value)

        # Encrypt de bijgewerkte afspraak
        existing_appointment.encrypt()

        # Gebruik de update method van SQLAlchemy om de gegevens bij te werken
        db.query(dbmodels.Appointment).filter(dbmodels.Appointment.id == id).update(
        updated_values, synchronize_session=False)
        db.commit()
        return query.first()

    def delete_appointment(id: int, db: Session):
        deleted_appointment = db.query(dbmodels.Appointment).filter(dbmodels.Appointment.id == id)
        if deleted_appointment.first() == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Appointment with id: {id} does not exist")
        
        deleted_appointment.delete(synchronize_session=False)
        db.commit()
        return deleted_appointment