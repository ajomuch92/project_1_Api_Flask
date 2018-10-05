new Vue({
  el: '#app',
  data(){
    return {
      user: '',
      tempUserName: '',
      socket: undefined,
      usersConnected: [],
      message: '',
      messages: []
    }
  },
  created(){
    this.socket = io.connect('http://127.0.0.1:5000');
  },
  mounted(){
    this.socket.on('user-registered', (data) => {
      this.usersConnected.push(data);
    });
    this.socket.on('new-message', (data) => {
      this.messages.push(data);
    });
    axios.get('http://127.0.0.1:5000/users').then(response => {
      this.usersConnected = response.data
    });
    axios.get('http://127.0.0.1:5000/messages').then(response => {
      this.messages = response.data
    });
  },
  methods:{
    login(){
      if(this.tempUserName !== ''){
        this.user = this.tempUserName;
        this.socket.emit('on-connect', {user: this.user});
      }
    },
    sendMessage(){
      fecha = new Date();
      date = fecha.toString();
      newMessage = {
        user: this.user,
        text: this.message,
        date: date
      }
      axios.post('http://127.0.0.1:5000/messages', newMessage).then(response => {
        this.message = '';
      }).catch(console.log)
    }
  }
})