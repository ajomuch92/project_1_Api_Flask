new Vue({
  el: '#app',
  data(){
    return {
      userName: '',
      tempUserName: '',
      socket: undefined
    }
  },
  mounted(){
    this.socket = io.connect('http://127.0.0.1:5000');
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