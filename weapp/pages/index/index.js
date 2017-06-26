//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    character: '',
    imgUrl: '',
    userInfo: {}
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    var that = this
    //调用应用实例的方法获取全局数据
    app.getUserInfo(function(userInfo){
      //更新数据
      that.setData({
        userInfo:userInfo
      })
    })
  },
  bindCharacter: function(e) {
    this.setData({
      character: e.detail.value
    })
  },
  bindImgUrl: function(e) {
    this.setData({
      imgUrl: 'http://www.52wubi.com/wbbmcx/tp/' + this.data.character + '.gif'
    })
  }
})
