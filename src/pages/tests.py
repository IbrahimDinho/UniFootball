from django.test import TestCase

# Create your tests here.

class URLTests(TestCase):
    def test_testHome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_Fixtures(self):
        response = self.client.get('/fixtures')
        self.assertEqual(response.status_code, 200)
    def test_pl(self):
        response = self.client.get('/premierLeague')
        self.assertEqual(response.status_code, 200)
    def test_login(self):
        response = self.client.get('/players/login')
        self.assertEqual(response.status_code, 200)
    def test_register(self):
        response = self.client.get('/players/register')
        self.assertEqual(response.status_code, 200)
    def test_logout(self):
        response = self.client.get('/players/logout')
        self.assertEqual(response.status_code, 302)
    def test_playerstats(self):
        response = self.client.get('/players/playerstats')
        self.assertEqual(response.status_code, 302)
    def test_team(self):
        response = self.client.get('/players/team')
        self.assertEqual(response.status_code, 302)
    def test_profile(self):
        response = self.client.get('/players/profile')
        self.assertEqual(response.status_code, 302)
    def test_table(self):
        response = self.client.get('/table')
        self.assertEqual(response.status_code, 200)