from django.test import TestCase
from dogs.models import Breed, Dog, Hobby, Owner, Country
from model_bakery import baker


# Create your tests here.
class DogsViewsetTestCase(TestCase):
    def test_list(self):
        self.assertEqual(1,1)

    def test_get_list(self):
        brd = baker.make("dogs.Breed")
        dog = baker.make("Dog", breed=brd)

        r = self.client.get('/api/dogs/')
        data = r.json()
        print(data)

        assert dog.name == data[0]['name']
        assert dog.id == data[0]['id']
        assert dog.breed.id == data[0]['breed']['id']
        assert len(data) == 1


    def test_create_dog(self):
        brd = baker.make("dogs.Breed")
        hb = baker.make("dogs.Hobby")
        cnt = baker.make("dogs.Country")
        own = baker.make("dogs.Owner")

        r = self.client.post("/api/dogs/", {
            "name": "Собака",
            "breed": brd.id,
            "hobby": hb.id,
            "country": cnt.id,
            "owner": own.id
        })

        new_dog_id = r.json()['id']

        dogs = Dog.objects.all()
        assert len(dogs) == 1

        new_dog = Dog.objects.filter(id=new_dog_id).first()
        assert new_dog.name == "Собака"
        assert new_dog.breed == brd
        assert new_dog.hobby == hb
        assert new_dog.country == cnt
        assert new_dog.owner == own

    def test_delete_dog(self):
        dogs = baker.make("Dog", 10)
        r = self.client.get("/api/dogs/")
        data = r.json()
        assert len(data) == 10

        dog_id_to_delete = dogs[3].id
        self.client.delete(f'/api/dogs/{dog_id_to_delete}/')

        r = self.client.get("/api/dogs/")
        data = r.json()
        assert len(data) == 9

        assert dog_id_to_delete not in [i['id'] for i in data] 


    # def test_update_dog(self):
    #     dogs = baker.make("Dog", 10)
    #     dog: Dog = dogs[2]
    #     brd = baker.make("dogs.Breed")
    #     hb = baker.make("dogs.Hobby")
    #     cnt = baker.make("dogs.Country")
    #     own = baker.make("dogs.Owner")

    #     r = self.client.get(f'/api/dogs/{dog.id}/')
    #     data = r.json()
    #     assert data['name'] == dog.name
    #     assert data['breed']['id'] == dog.breed.id 
    #     assert data['hobby']['id'] == dog.hobby.id 
    #     assert data['country']['id'] == dog.country.id 
    #     assert data['owner']['id'] == dog.owner.id 

    #     r = self.client.patch(
    #         f'/api/dogs/{dog.id}/',
    #         json.dumps({
    #             "name": "Коржик",
    #             "breed": brd.id,
    #             "hobby": hb.id,
    #             "country": cnt.id,
    #             "owner": own.id
    #         }),
    #         content_type='application/json'
    #     )
    #     assert r.status_code == 200

    #     r = self.client.get(f'/api/dogs/{dog.id}/')
    #     data = r.json()
    #     assert data['name'] == "Коржик"
    #     assert data['breed']['id'] == brd.id 
    #     assert data['hobby']['id'] == hb.id 
    #     assert data['country']['id'] == cnt.id 
    #     assert data['owner']['id'] == own.id 

    #     dog.refresh_from_db()
    #     assert data['name'] == dog.name
    #     assert data['breed']['id'] == brd.id 
    #     assert data['hobby']['id'] == hb.id 
    #     assert data['country']['id'] == cnt.id 
    #     assert data['owner']['id'] == own.id
