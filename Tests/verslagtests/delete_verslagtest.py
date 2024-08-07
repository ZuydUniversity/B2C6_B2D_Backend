# Import the necessary classes and modules
from sqlalchemy.orm import Session
from App.Repos.VerslagRepo import VerslagRepo
from App.Data import DatabaseModels as dbmodels

# Dependencies:
# pip install pytest-mock
import pytest

class TestDeleteVerslag:

    # Successfully delete an existing verslag by valid ID
    def test_delete_existing_verslag(self, mocker):
        # Arrange
        mock_db = mocker.create_autospec(Session, instance=True)
        verslag_id = 1
        verslag = dbmodels.Verslag(id=verslag_id)
        mock_db.query.return_value.filter.return_value.first.return_value = verslag

        repo = VerslagRepo(mock_db)

        # Act
        result = repo.delete_verslag(verslag_id)

        # Assert
        mock_db.delete.assert_called_once_with(verslag)
        mock_db.commit.assert_called_once()
        assert result == verslag

    # Attempt to delete a verslag with a non-existent ID
    def test_delete_non_existent_verslag(self, mocker):
        # Arrange
        mock_db = mocker.create_autospec(Session, instance=True)
        verslag_id = 999
        mock_db.query.return_value.filter.return_value.first.return_value = None

        repo = VerslagRepo(mock_db)

        # Act
        result = repo.delete_verslag(verslag_id)

        # Assert
        mock_db.delete.assert_not_called()
        mock_db.commit.assert_not_called()
        assert result is None
