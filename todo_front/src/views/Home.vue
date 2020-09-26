<template>
  <div class="home">
    <nav class="navbar navbar-dark bg-dark">
      <span class="navbar-brand mb-0 h1">Vuengo ToDo App</span>
    </nav>
    <div class="add-panel">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <form @submit.prevent="addTask">
              <div class="row">
                <div class="col-md-10">
                  <div class="form-group">
                    <input
                      type="text"
                      class="input form-control"
                      placeholder="Make a to do list :D"
                      name="title"
                      v-model="title"
                    />
                  </div>
                </div>
                <div class="col-md-2">
                  <div class="form-group">
                    <button class="btn btn-sm btn-dark" type="submit">Add Task</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="task-panel" v-if="tasks.length>0">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <h4 class="subtitle">To Do</h4>
            <div class="todo">
              <div class="card" v-for="task in todoTasks" :key="task.id">
                <div class="card-header header-todo">{{ task.title }}</div>
                <div class="card-footer footer-in-progress">
                  <a class="card-footer-item" @click="setStatus(task, 'in_progress')">In Progress</a>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <h4 class="subtitle">In Progress</h4>
            <div class="in_progress">
              <div class="card" v-for="task in inProgressTasks" :key="task.id">
                <div class="card-header header-in-progress">{{task.title}}</div>
                <div class="card-footer footer-done">
                  <a class="card-footer-item" @click="setStatus(task,'done')">Done</a>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <h4 class="subtitle">Done</h4>
            <div class="done">
              <div class="card" v-for="task in doneTasks" :key="task.id">
                <div class="card-header header-done">{{task.title}}</div>
                <div class="card-footer footer-delete">
                  <a href class="card-footer-item" @click="deleteTask(task)">Delete</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="task-panel-empty" v-else>
      <p>You have no tasks currently!</p>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

const BASE_URL = 'https://vtodo-api.herokuapp.com';
const AUTH = {
  username: 'admin',
  password: 'admin',
};
export default {
  name: 'Home',
  data() {
    return {
      tasks: [],
      title: null,
      status: 'todo',
      errors: [],
    };
  },
  mounted() {
    this.getTasks();
  },
  methods: {
    getTasks() {
      const vm = this;
      axios
        .get(`${BASE_URL}/tasks/`, {
          auth: AUTH,
        })
        .then((response) => {
          console.log(response);
          vm.tasks = response.data;
        });
    },
    addTask() {
      if (this.title) {
        axios({
          method: 'post',
          url: `${BASE_URL}/tasks/`,
          data: {
            title: this.title,
            status: 'todo',
          },
          auth: {
            username: 'admin',
            password: 'admin',
          },
        })
          .then((response) => {
            const newTask = {
              id: response.data.id,
              title: this.title,
              status: 'todo',
              url: response.data.url,
            };
            this.tasks.push(newTask);
            this.title = '';
            this.status = 'todo';
          })
          .catch((error) => {
            console.log(error);
          });
      } else if (!this.title) this.errors.push('Title is required');
    },
    setStatus(task, status) {
      axios({
        method: 'patch',
        url: task.url,
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          status,
          description: task.description,
        },
        auth: {
          username: 'admin',
          password: 'admin',
        },
      }).then(() => {
        // eslint-disable-next-line no-param-reassign
        task.status = status;
      });
    },
    deleteTask(task) {
      axios({
        method: 'delete',
        url: task.url,
        auth: AUTH,
      }).then(() => {
        const delIndex = this.tasks.findIndex((item) => item.url === task.url);
        this.tasks.splice(delIndex, 1);
      });
    },
  },
  computed: {
    todoTasks() {
      return this.tasks.filter((task) => task.status === 'todo');
    },
    inProgressTasks() {
      return this.tasks.filter((task) => task.status === 'in_progress');
    },
    doneTasks() {
      return this.tasks.filter((task) => task.status === 'done');
    },
  },
};
</script>

<style>
@import "./../assets/css/home.scss";
</style>
