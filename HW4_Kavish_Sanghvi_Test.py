"""
author: @kavishsanghvi
@purpose: to test the fetched and stored count of commit of the repository from GitHub
"""

import unittest
from HW4_Kavish_Sanghvi import main,repo
from unittest import mock
from unittest.mock import Mock, patch

class TestRepo(unittest.TestCase):
    """ class for test cases
    """
    
    def test_commit(self):
        """ function to test count for commits
        """

        mock_get_patcher = patch("urllib.request.urlopen")
        mock_get = mock_get_patcher.start()
        githubResponse = [{},{},{},{}]
        mock_get.return_value.json.return_value = githubResponse
        mock_get.return_value.ok = True
        mock_get.return_value.status_code = 200
        mock_get_patcher.stop()

if __name__ == "__main__":
    unittest.main(exit=False)
