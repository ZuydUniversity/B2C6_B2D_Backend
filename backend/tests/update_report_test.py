import pytest
from unittest import mock
from backend.models import Report
from backend.main import update_report

class TestUpdateReport:

    def test_update_report_with_valid_inputs(self, mocker):
        db_session = mocker.Mock()
        mocker.patch.object(db_session, 'query')
        mocker.patch.object(db_session, 'commit')
        mocker.patch.object(db_session, 'refresh')

        report = Report(
            id=1,
            date="2024-05-29",  # date as string
            healthcomplaints="Headache",
            medicalhistory="None",
            diagnose="Migraine"
        )

        db_session.query().filter().first.return_value = report

        updated_report = update_report(db_session, 1, date="2024-06-01", healthcomplaints="Severe headache", diagnose="ok")

        assert updated_report.date == "2024-06-01"  # Check date as string
        assert updated_report.healthcomplaints == "Severe headache"
        assert updated_report.diagnose == "ok"
        db_session.commit.assert_called_once()
        db_session.refresh.assert_called_once_with(report)


        #Command test pytest backend/tests/update_report_test.py

