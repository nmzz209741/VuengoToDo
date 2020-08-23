<template>
  <div class="home">
    <nav class="navbar navbar-light bg-light">
      <span class="navbar-brand mb-0 h1">Vuengo ToDo App</span>
    </nav>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <form @submit.prevent="addTask">
            <h4 class="subtitle">Add Task</h4>
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
                  <button class="btn btn-sm btn-primary" type="submit">Add Task</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <h4 class="subtitle">To Do</h4>
          <div class="todo">
            <div class="card" v-for="task in todoTasks" :key="task.id">
              <div class="card-content">{{ task.title }}</div>
              <footer class="card-footer">
                <a class="card-footer-item">In Progress</a>
              </footer>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <h4 class="subtitle">In Progress</h4>
          <div class="in_progress">
            <div class="card" v-for="task in inProgressTasks" :key="task.id">
              <div class="card-content">{{task.title}}</div>
              <footer class="card-footer">
                <a href class="card-footer-item">Done</a>
              </footer>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <h4 class="subtitle">Done</h4>
          <div class="done">
            <div class="card" v-for="task in doneTasks" :key="task.id">
              <div class="card-content">{{task.title}}</div>
              <footer class="card-footer">
                <a href class="card-footer-item">Delete</a>
              </footer>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
const BASE_URL = "http://127.0.0.1:8000";
const AUTH = {
  username: "admin",
  password: "admin"
};
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      tasks: [],
      title: null,
      status: "todo",
      errors: []
    };
  },
  created() {
    this.getTasks();
  },
  methods: {
    getTasks: function() {
      var vm = this;
      axios
        .get(`${BASE_URL}/tasks/`, {
          auth: AUTH
        })
        .then(response => {
          console.log(response);
          vm.tasks = response.data;
        });
    },
    addTask: function() {
      if (this.title) {
        axios({
          method: "post",
          url: BASE_URL + "/tasks/",
          data: {
            title: this.title,
            status: "todo"
          },
          auth: {
            username: "admin",
            password: "admin"
          }
        })
          .then(response => {
            let newTask = {
              id: response.data.id,
              title: this.title,
              status: "todo"
            };
            this.tasks.push(newTask);
            this.title = "";
            this.status = "todo";
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        if (!this.title) this.errors.push("Title is required");
      }
    }
  },
  computed: {
    todoTasks() {
      return this.tasks.filter(task => task.status === "todo");
    },
    inProgressTasks() {
      return this.tasks.filter(task => task.status === "in_progress");
    },
    doneTasks() {
      return this.tasks.filter(task => task.status === "done");
    }
  }
};
</script>

<style>
@import "./../assets/css/home.scss";
</style>
