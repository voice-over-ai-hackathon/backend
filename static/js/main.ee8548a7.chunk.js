(window.webpackJsonp=window.webpackJsonp||[]).push([[0],[,,,,,,,,function(e,t,n){e.exports=n.p+"static/media/play.dcb8568c.svg"},function(e,t,n){e.exports=n.p+"static/media/pause.90d6cda5.svg"},,function(e,t,n){e.exports=n(20)},,,,,function(e,t,n){},,function(e,t,n){},,function(e,t,n){"use strict";n.r(t);var a=n(0),i=n.n(a),o=n(1),s=n.n(o),r=(n(16),n(2)),c=n(3),u=n(5),l=n(4),d=n(6),p=(n(18),n(8)),b=n.n(p),h=n(9),m=n.n(h),w=n(10),g=n.n(w),v={undefined:"http://1x1px.me/FF4D00-0.png",null:"http://1x1px.me/FF4D00-0.png",false:"http://1x1px.me/FF4D00-0.png",calm:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/calm.png",happy:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/happy.png",sad:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/sad.png",angry:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/angry.png",fearful:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/fearful.png",neutral:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/neutral.png",informationQuery:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/getting_information2.png",pickupCollection:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/collecting.png",delivery:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/delivery.png",business:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/briefcase.png",private:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/private.png",satisfied:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/courteous_agent.png",unsatisfied:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/uncourteous_agent.png",kind:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/courteous_agent2.png",unkind:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/uncourteous_agent2.png","":"http://1x1px.me/FF4D00-0.png"},f=["happy","angry","unsatisfied","neutral","unkind","angry","calm","neutral","satisfied","unsatisfied","sad","fearful","angry"],j=["","","","business","","","","","","","","","",""],x=function(e){function t(e){var n;return Object(r.a)(this,t),(n=Object(u.a)(this,Object(l.a)(t).call(this,e))).state={playing:!1,secondsElapsed:0},n}return Object(d.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.$el=s.a.findDOMNode(this),this.$waveform=this.$el.querySelector(".wave"),this.wavesurfer=g.a.create({container:this.$waveform,waveColor:"purple",progressColor:"orange",height:300}),this.wavesurfer.load(this.props.src),this.wavesurfer.on("audioprocess",function(t){e.onAudioProcess(t-1.5)})}},{key:"componentWillUnmount",value:function(){}},{key:"onAudioProcess",value:function(e){e<0&&(e=0),this.secondsElapsedFull=e,this.setState({secondsElapsed:Math.round(e),emojiIndex:Math.round(e/5)})}},{key:"play",value:function(){this.setState({playing:!0}),this.wavesurfer.play()}},{key:"stop",value:function(){this.setState({playing:!1}),this.wavesurfer.stop()}},{key:"render",value:function(){var e=this;return console.log(this.state.secondsElapsed),i.a.createElement("div",null,i.a.createElement("style",null,"\n                .playbtn{\n                    border-radius : 50%;\n                }\n                .container {\n                    position: relative;\n                    display: block;\n                    left: 45%\n                    width: 200px;\n                    height: 100%;\n                }\n\n                .pulse-button {\n\n                    position: relative;\n                    width: 100px;\n                    height: 100px;\n                    border: none;\n                    box-shadow: 0 0 0 0 rgba(232, 76, 61, 0.7);\n                    border-radius: 50%;\n                    background-color: #e84c3d;\n                    background-image: url(http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/emoji/briefcase.png);\n                    background-size:cover;\n                    background-repeat: no-repeat;\n                    cursor: pointer;\n                    -webkit-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);\n                    -moz-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);\n                    -ms-animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);\n                    animation: pulse 1.25s infinite cubic-bezier(0.66, 0, 0, 1);\n                }\n                    .pulse-button:hover\n                    {\n                        -webkit-animation: none;-moz-animation: none;-ms-animation: none;animation: none;\n                    }\n\n                    @-webkit-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}\n                    @-moz-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}\n                    @-ms-keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}\n                    @keyframes pulse {to {box-shadow: 0 0 0 45px rgba(232, 76, 61, 0);}}\n\n"),i.a.createElement("div",{className:"waveform"},i.a.createElement("br",null),i.a.createElement("br",null),i.a.createElement("button",{className:"playbtn",onClick:function(){e.state.playing?e.stop():e.play()}},i.a.createElement("img",{className:"play",src:this.state.playing?m.a:b.a,height:50,width:50}))),i.a.createElement("div",{className:"wave"}),i.a.createElement("div",null,this.state.playing?i.a.createElement("div",{width:"100%",align:"left"},i.a.createElement("table",{border:"0"},i.a.createElement("tr",null,i.a.createElement("td",null,i.a.createElement("img",{src:"http://1x1px.me/FF4D00-0.8.png",width:1*this.secondsElapsedFull/67*1812,height:0})),i.a.createElement("td",{align:"center"},i.a.createElement("img",{src:v[f[this.state.emojiIndex]],width:128,height:128}),i.a.createElement("br",null),i.a.createElement("h1",null,f[this.state.emojiIndex]))))):i.a.createElement("div",null)),"business"==j[this.state.emojiIndex]&&i.a.createElement("div",{align:"center",style:{marginTop:"70px"}},i.a.createElement("div",{className:"container"},i.a.createElement("button",{className:"pulse-button"})),"Business"))}}]),t}(i.a.Component);x.defaultProps={src:""};var k=function(e){function t(){return Object(r.a)(this,t),Object(u.a)(this,Object(l.a)(t).apply(this,arguments))}return Object(d.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return i.a.createElement("div",{className:"App"},i.a.createElement(x,{src:"http://ibd-backend.datah-route-b0wnj1b639re-1206570512.eu-west-1.convox.site/static/wav/too2.wav"}))}}]),t}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(i.a.createElement(k,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}],[[11,2,1]]]);
//# sourceMappingURL=main.ee8548a7.chunk.js.map