new Vue({
  el: '#app',
  data(){
    return {
      userName: '',
      tempUserName: '',
      socket: undefined,
      usersConnected: []
    }
  },
  created(){
    this.socket = io.connect('http://' + document.domain + ':' + location.port);
  },
  mounted(){
    this.socket.on('user-connected', (response)=> {
      this.usersConnected.push(response)
    })
    axios.get('http://127.0.0.1:5000/users').then(response => (this.usersConnected = response));
  },
  methods:{
    login(){
      if(this.tempUserName !== ''){
        this.userName = this.tempUserName;
        this.socket.emit('on-connect', {user: this.userName});
      }
    }
  }
})