"""
author: @kavishsanghvi
@purpose: to test the fetched and stored count of commit of the repository from GitHub
"""

import unittest
from HW4_Kavish_Sanghvi import main,repo
from unittest import mock

class TestRepo(unittest.TestCase):
    """ class for test cases
    """

    @mock.patch("urllib.request.urlopen")

    def test_commit(self):
        """ function to test count for commits
        """

        repos = [item for item in repo("kavishsanghvi")]
        result = ['Repo: covid-19-data-analysis-using-python, Commits: 5',
                  'Repo: cs546b_group22_final_project, Commits: 30',
                  'Repo: fauna-image-classification-using-convolutional-neural-network, Commits: 13', 'Repo: file-management-system-using-django, Commits: 3', 'Repo: graduation, Commits: 30', 'Repo: kavishsanghvi-master, Commits: 6', 'Repo: library-management-system, Commits: 8',
                  'Repo: SSW-567-WS, Commits: 8',
                  'Repo: SSW567-WS-Triangle, Commits: 18',
                  'Repo: Student-Repository, Commits: 11']
        self.assertEqual(sorted(repos), sorted(result))

if __name__ == "__main__":
    unittest.main(exit=False)
