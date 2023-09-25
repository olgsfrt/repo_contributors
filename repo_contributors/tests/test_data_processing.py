import os
import unittest
from unittest.mock import patch, Mock
from src.data_processing import process_repositories, save_data_to_excel

class TestDataProcessing(unittest.TestCase):

    def test_process_repositories(self):
        # Mock the fetch_contributors and enrich_contributor_data functions
        with patch('src.data_processing.fetch_contributors', return_value=[{'login': 'user1'}]), \
             patch('src.data_processing.enrich_contributor_data', return_value=[['user1', 10, 'url', 'followers_url', 5, 3, 2, 1, 'topic1, topic2', 'location']]):
            
            repo_links = ['https://github.com/owner/repo']
            result = process_repositories(repo_links)
            
            self.assertEqual(result, {'repo': [['user1', 10, 'url', 'followers_url', 5, 3, 2, 1, 'topic1, topic2', 'location']]})
    
    def test_save_data_to_excel(self):
        # Define the test data
        repositories_data = {'repo': [['user1', 10, 'url', 'followers_url', 5, 3, 2, 1, 'topic1, topic2', 'location']]}
        
        # Call the function to save data to Excel
        save_data_to_excel(repositories_data)
        
        # Check if the file has been created
        self.assertTrue(os.path.exists('data/contributors_repo.xlsx'))
        
        # Cleanup: Remove the created file
        os.remove('data/contributors_repo.xlsx')

if __name__ == '__main__':
    unittest.main()
