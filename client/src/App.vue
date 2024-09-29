<script setup>
import {computed, ref, onBeforeMount} from 'vue';
import axios from "axios";
import Cookies from 'js-cookie';

const dogs = ref([]);
const dogToAdd = ref({});
const breed = ref({});
const dogToEdit = ref({});
const loading = ref(false); 

async function fetchDogs(){
  loading.value = true;
  const r = await axios.get("/api/dogs/");
  console.log(r.data)
  dogs.value = r.data;
  loading.value = false;
}

async function fetchBreeds(){
  const r = await axios.get("/api/breed/");
  console.log(r.data)
  breed.value = r.data;
}

async function onLoadClick(){
  await fetchDogs()
}

async function onDogClick(){
  await axios.post("/api/dogs/", {
    ...dogToAdd.value,
  });
  await fetchDogs(); // переподтягиваю
  dogToAdd.value = {};
}

async function onRemoveClick(dog) {
  await axios.delete(`/api/dogs/${dog.id}/`);
  await fetchDogs();
}

async function onDogEditClick(dog) {
  dogToEdit.value = { ...dog }; 
}

async function onUpdateDog() {
  await axios.put(`/api/dogs/${dogToEdit.value.id}/`, {
    ...dogToEdit.value,
  });
  await fetchDogs(); 
}

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchBreeds();
})

</script>

<template>
  <div>
    <button @click="onLoadClick">Загрузить собак</button>

    <div v-for="dog in dogs" class="dog-item">
      <div>{{ dog.name }}</div>
      <button class="btn btn-success" @click="onDogEditClick(dog)" data-bs-toggle="modal" data-bs-target="#editDogModal"> 
        <i class="bi bi-pen-fill"></i>
      </button>
      <button class="btn btn-danger" @click="onRemoveClick(dog)">
        <i class="bi bi-x"></i>
      </button>
    </div>

    <form @submit.prevent.stop="onDogClick">
      <div class="row">
        <div class="col">
          <div class="form-floating">
            <input
              type="text"
              class="form-control"
              v-model="dogToAdd.name"
              required
            />
            <label for="floatingInput">Имя</label>
          </div>
        </div>
        <div class="col">
          <div class="form-floating">
            <select name="" id="" class="form-select" v-model="dogToAdd.breed">
              <option :value="b.id" v-for="b in breed">{{ b.name }}</option>
            </select>
            <label for="floatingInput">Порода</label>
          </div>
        </div>
        <div class="col-auto">
          <button class="btn btn-primary">
            Добавить
          </button>
        </div>
      </div>
    </form>

    <div class="modal fade" id="editDogModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">
              Редактировать собаку
            </h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col">
                <div class="form-floating">
                  <input type="text" class="form-control" v-model="dogToEdit.name" />
                  <label for="floatingInput">Имя</label>
                </div>
              </div>
              <div class="col">
          <div class="form-floating">
            <select name="" id="" class="form-select" v-model="dogToEdit.breed">
              <option :value="b.id" v-for="b in breed">{{ b.name }}</option>
            </select>
            <label for="floatingInput">Порода</label>
          </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              Close
            </button>
            <button type="button" class="btn btn-primary" @click="onUpdateDog" data-bs-dismiss="modal">
              Сохранить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
