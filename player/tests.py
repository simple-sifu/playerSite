from django.test import TestCase
from django.urls import reverse, resolve
from .models import Player
from rest_framework import status

# Create your tests here.
class PlayerTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        player = Player.objects.create(
            playerID="testplayer000", 
            name="Elmhurst Hospital", 
            openDate='04/05/20',
            birthYear="2001",
            birthMonth="15", 
            birthDay="4",
            birthCountry="US",
            birthState="NY",
            birthCity="NYC",
            deathYear="2020",
            deathMonth="04",
            deathDay="04",
            deathCountry="Russia",
            deathState="Moscow",
            deathCity="Lennigrad",
            nameFirst="Boris",
            nameLast="Vladimer",
            nameGiven="Vlad",
            weight="200",
            height="5'11",
            bats="4",
            throws="20",
            debut="2020-04-15",
            finalGame="2020-05-20",
            retroID="asdfsad",
            bbrefID="adfarrr")

    def test_player_content(self):

        pl = player.objects.get(playerID="testplayer000") 

        self.assertEquals(pl.bbrefID, 'adfarrr')  
        self.assertEquals(pl.retroID, "asdfsad")  

    def test_description_content(self):

        desc = Description.objects.get(facility=99999)

        self.assertEquals(desc.shortDescription, 'veryshort')
        self.assertEquals(desc.description, 'desc')

    def test_location_content(self):

        loc = Location.objects.get(facility=99999)

        self.assertEquals(loc.address1, "address")
        self.assertEquals(loc.address2, "address2")
        self.assertEquals(loc.city, "city")
        self.assertEquals(loc.state, "state")
        self.assertEquals(loc.zipCode, "zip")
        self.assertEquals(loc.phoneNumber, "ph")
        self.assertEquals(loc.faxNumber, "fax")
        self.assertEquals(loc.website, "web")
        self.assertEquals(loc.countyCode, "cc")
        self.assertEquals(loc.county, "cou")
        self.assertEquals(loc.latitude, "lat")
        self.assertEquals(loc.longitude, "long")
        self.assertEquals(loc.location, "loc")

    def test_facilities_list_api(self):
        url = reverse('facility-list')

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        facilityDict = dict(dict(self.response.data).get('results')[0])
        self.assertEqual(facilityDict.get('facility'), 99999)
        self.assertEqual(facilityDict.get('name'), 'Elmhurst Hospital')
        descDict = dict(facilityDict.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(facilityDict.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_facilities_detail_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data.get('facility'), 99999)
        self.assertEqual(self.response.data.get('name'), 'Elmhurst Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_missing_facilities_detail_api(self):
        url = reverse('facility-detail', kwargs={"pk":"1"})

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_facilities_list_different_queryParams_api(self):
        url = reverse('facility-list')+'?shortDesc=No'
        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(self.response.data.get('facility'), 99999)

    def test_facilities_list_matching_queryParams_api(self):
        url = reverse('facility-list')+'?shortDesc=veryshort'

        self.response = self.client.get(url)

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        facilityDict = dict(dict(self.response.data).get('results')[0])
        self.assertEqual(facilityDict.get('facility'), 99999)

    def test_facilities_good_delete_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})

        self.response = self.client.delete(url)

        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_facilities_missing_rec_delete_api(self):
        url = reverse('facility-detail', kwargs={"pk":"1"})

        self.response = self.client.delete('/api/v1/facilities/1/')

        self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)

    def test_facilities_update_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})
        self.response = self.client.get(url)
        newNameObject = self.response.data
        newNameObject.update({"name": 'Jackson Hospital'})
 
        self.response = self.client.put(url, newNameObject, "application/json")

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)        
        self.assertEqual(self.response.data.get('facility'), 99999)
        self.assertEqual(self.response.data.get('name'), 'Jackson Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')

    def test_facilities_insert_api(self):
        url = reverse('facility-detail', kwargs={"pk":"99999"})
        self.response = self.client.get(url)
        newFacilityObject = self.response.data
        newFacilityObject.update({"facility": 4})
        url = reverse('facility-list')
 
        self.response = self.client.post(url, newFacilityObject, "application/json")

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data.get('facility'), 4)
        self.assertEqual(self.response.data.get('name'), 'Elmhurst Hospital')
        descDict = dict(self.response.data.get('desc')[0])
        self.assertEqual(descDict.get('shortDescription'), 'veryshort')
        locDict = dict(self.response.data.get('loc')[0])
        self.assertEqual(locDict.get('city'), 'city')
