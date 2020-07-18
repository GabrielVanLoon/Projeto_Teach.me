import axios from "axios";

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

export default axios.create({
  baseURL: "http://localhost:8000/api/",
  // responseType: "json",
});