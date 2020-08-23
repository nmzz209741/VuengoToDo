<template>
  <div class="home">
    <nav class="navbar navbar-light bg-light">
      <span class="navbar-brand mb-0 h1">Vuengo ToDo App</span>
    </nav>
    <div class="row">
      <div class="col-md-3">
        <form>
          <h2 class="subtitle">Add Task</h2>
          <div class="form-group">
            <label for="title">Title</label>
            <input type="text" class="input form-control"
              placeholder="Make a to do list :D" name="title">
          </div>
          <div class="form-group">
            <label for="status">Status</label>
            <select name="status" id="status" class="form-control">
              <option value="todo">To Do</option>
              <option value="in_progress">In Progress</option>
              <option value="done">Done</option>
            </select>
          </div>
          <div class="form-group">
            <button class='btn btn-sm btn-primary' type=submit>Add Task</button>
          </div>
        </form>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">
        <h2 class="subtitle">
          To Do
        </h2>
        <div class="todo">
          <div class="card">
            <div class="card-content">Task 1</div>
            <footer class="card-footer">
              <a href="" class="card-footer-item">In Progress</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <h2 class="subtitle">
          In Progress
        </h2>
        <div class="in_progress">
          <div class="card">
            <div class="card-content">Task 2</div>
            <footer class="card-footer">
              <a href="" class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <h2 class="subtitle">
          Done
        </h2>
        <div class="done">
          <div class="card">
            <div class="card-content">Task 3</div>
            <footer class="card-footer">
              <a href="" class="card-footer-item">Delete</a>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

// import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    // getTasks: function () {
    //   var vm = this
    //   axios.get('http://127.0.0.1:8000/tasks/')
    //   .then()
    // }
  },
};
</script>

<style>
@import './../assets/css/home.scss';
</style>
