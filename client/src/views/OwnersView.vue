<script setup>
import {computed, ref, onBeforeMount} from 'vue';
import axios from "axios";
import Cookies from 'js-cookie';

const owner = ref({});
const ownerToEdit = ref({});
const ownerToAdd = ref({});

const loading = ref(false); 

async function fetchOwner(){
  const r = await axios.get("/api/owner/");
  console.log(r.data)
  owner.value = r.data;
}


async function onLoadClickForOwner(){
  await fetchOwner()
}


async function onDogClickForOwner(){
  await axios.post("/api/owner/", {
    ...ownerToAdd.value,
  });
  await fetchOwner(); // переподтягиваю
  ownerToAdd.value = {};
}


async function onRemoveClickForOwner(owner) {
  await axios.delete(`/api/owner/${owner.id}/`);
  await fetchOwner();
}

async function onOwnerEditClick(owner) {
  ownerToEdit.value = { ...owner }; 
}

async function onUpdateOwner() {
  await axios.put(`/api/owner/${ownerToEdit.value.id}/`, {
    ...ownerToEdit.value,
  });
  await fetchOwner(); 
}



onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
})

</script>

<template>
  <div><br>
    <button @click="onLoadClickForOwner">Загрузить хозяинов собак</button>

    <div v-for="o in owner" class="owner-item">
      <div>{{ o.first_name }} {{ o.last_name }}</div>
      <button class="btn btn-success" @click="onOwnerEditClick(o)" data-bs-toggle="modal" data-bs-target="#editDogModal3"> 
        <i class="bi bi-pen-fill"></i>
      </button>
      <button class="btn btn-danger" @click="onRemoveClickForOwner(o)">
        <i class="bi bi-x"></i>
      </button>
    </div>

    <form @submit.prevent.stop="onDogClickForOwner">
      <div class="row">
        <div class="col-auto">
        <div class="form-floating">
            <input
              type="text"
              class="form-control"
              v-model="ownerToAdd.first_name"
              required
            />
            <label for="floatingInput">Добавим имя хозяина</label>
          </div>
        </div>
        <div class="col-auto">
        <div class="form-floating">
        <input
              type="text2"
              class="form-control"
              v-model="ownerToAdd.last_name"
              required
            />
            <label for="floatingInput">Добавим фамилию хозяина</label>
          </div>
        </div>
        <div class="col-auto">
        <div class="form-floating">
        <input
              type="text2"
              class="form-control"
              v-model="ownerToAdd.last_name"
              required
            />
            <label for="floatingInput">Добавим номер телефона хозяина</label>
          </div>
        </div>
        <div class="col-auto">
          <button class="btn btn-primary">
            Добавить
          </button>
        </div>
      </div>
    </form>

    <div class="modal fade" id="editDogModal3" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">
              Редактировать хозяина
            </h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col">
                <div class="form-floating">
                  <input type="text" class="form-control" v-model="ownerToEdit.first_name" />
                  <label for="floatingInput">Имя хозяина</label>
                </div>
              </div>
              <div class="col">
                <div class="form-floating">
                  <input type="text" class="form-control" v-model="ownerToEdit.last_name" />
                  <label for="floatingInput">Фамилия хозяина</label>
                </div>
              </div>
              <div class="col">
                <div class="form-floating">
                  <input type="text" class="form-control" v-model="ownerToEdit.phone_number" />
                  <label for="floatingInput">Телефон хозяина</label>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              Close
            </button>
            <button type="button" class="btn btn-primary" @click="onUpdateOwner" data-bs-dismiss="modal">
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
