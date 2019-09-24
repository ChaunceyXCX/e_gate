# e_gate
基于ESP8266做的车库门wifi控制器

## 控制页面在8081端口,IP为`路由器分配的ip`,ap模式下为`192.168.4.1`

## 烧录前需要先设置`wifi`与`ap`的`ssid`与`密码`,分别在[main.py](https://github.com/ChaunceyXCX/e_gate/blob/master/main.py)和[wlanauto.py](https://github.com/ChaunceyXCX/e_gate/blob/master/wlanauto.py)

## tips
- 上电启动后板载蓝灯,一直`闪烁`,表示没有连接到局域网wifi,请查看`ssid`与`密码`是否设置正确,如果正确请确认是否在wifi的信号范围,
  - 因为配网没有做完所以在页面上禁用了,可以访问`192.168.*.*:8081/wlancfg`,查看附近可以搜索到的wifi
- 上电启动后如果灯亮且不闪烁表示启动成功

## TODO

- [ ] 目前只做了局域网的功能,需要加入互联网
- [ ] 配网功能9不应该把ssid与密码写入程序中,一点也不优雅)
- [ ] ai支持
  - [-] 支持siri(可通过添加safari指令实现)
  - [ ] 支持小爱音响(小爱没有开放api,看到米家上可以添加机智云,但是机智云好像没有micropython的sdk,考虑再开一个esp8266做一个基于机智云的智能网关应该可行,如果哪位老哥有更优雅的方案,请赐教)
  - [ ] 支持bixby(需要app)
  - [ ] 接入微信(WeTeBot,小程序)
 - [ ] 做出配套app(考虑用flutter)
