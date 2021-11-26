# PKUAutoSubmit Github Actions版

无需代码基础，无需下载文件到你的电脑，无需保持自己电脑开机，无需配置服务器和环境的

萌新友好的自动出入校备案程序！

祝大家科研和学业顺利，也祝大家身体健康！

【11.26更新：Github Actions环境的Chrome更新了，旧版本不能用了，请大家Fetch and merge upstream最新版本。现在更新为了使用最新driver，以后不会再出现driver版本的问题了~】

【重要提醒：如果你是Fetch and merge upstream了新版本，更新之后请务必不要忘记改config.ini以及workflow下的corn表达式！！】

## 说明

本项目基于[PKUAutoSubmit](https://github.com/Bruuuuuuce/PKUAutoSubmit)3.0版本开发，因此跟随使用了[Apache License 2.0](https://github.com/xiazhongyv/PKUActionSubmit/blob/master/LICENSE)证书。

本项目提供了Github Actions支持，所以现在你只需要在网页端点点鼠标，无需下载任何文件到你自己的电脑或者服务器，更不需要时刻都开着电脑了。

## 如何运行自动报备

熟悉Github的大佬们请无视掉本节内容~ 

因为是在Github提供的Linux服务器上运行的，不需要在本地配环境，所以以下内容适用于任何系统的用户。

以下内容有着[图文教程](https://blog.haysc.tech/pku-auto-beian-2021/)，感谢@hayschan制作该教程！

0. （可选）右上角点个星星吧，不要下次一定嘛~

1. 首先你需要有一个Github账号，如果你现在还没有登录，就赶紧点击右上角登录Github吧！推荐使用edu邮箱注册。

2. （可选）然后如果你想要在每天自动报备后能够收到成功的提醒，那么可以在[Server酱](https://sct.ftqq.com/)用微信扫码登录，得到一个SENDKEY

3. 然后点击右上角的“Fork”，将该仓库分支到你自己，稍等片刻后，现在你应该在【你的ID/PKUAutoSubmit_online】这个仓库里了。（当然，如果您不是github萌新，完全可以把代码clone在任何机器运行）

4. 然后在【你的ID/PKUAutoSubmit_online】下面那一栏里找到找到 <>Code ，在文件列表里里找到config.ini，点进去后右上角有一个小铅笔的符号，点击它就能编辑出入校信息了。
    
    按照你想要的进行编辑完成后，翻到页面最下面，点击commit changes并确认就好了。如果你跳过了第2步，记得把微信通知那里改成False.

5. 然后在【你的ID/PKUAutoSubmit_online】下面那一栏里找到 Settings ，点击，在左侧找到Secrets，点击

    点击右侧New Repository secret，然后添加 ID（大写的），然后输入你的学号

    再点击右侧New Repository secret，然后添加 PASSWORD（大写的），然后输入你的密码。【如果你的密码里有特殊字符如()/\, 请用双引号将你的密码包裹起来，即在value一栏输入："yourpassword"】

    再点击右侧New Repository secret，然后添加 MAIL_ADDRESS（大写的），然后输入你的电子邮箱地址

    再点击右侧New Repository secret，然后添加 PHONE_NUMBER（大写的），然后输入你的手机号码

    再点击右侧New Repository secret，然后添加 SENDKEY（大写的），然后输入你的SENDKEY（如果你不需要微信通知，就随便写点啥都行）

    <font size=5>*secret是github的保密字段，在这里填写的内容，在填写后没人能够看到它是什么，包括你自己，你只能修改它。*
    
6. 当前我的仓库的默认值为周三四五中午12点，如果你想修改这个频率，请务必注意修改.github/workflows/main.yml Line 6的corn表达式来更改为你想要的报备频率。 

7. 然后在【你的ID/PKUAutoSubmit_online】下面那一栏里找到 Actions，点进去，

    可能会弹出提示框，点击“Enable...”允许脚本运行，

    从左侧列表里选中PKUAutoSubmit，

    可能上面还是会有一条提示说是否允许脚本在fork的仓库上运行，点击“Enable...”就好，

    这个时候，脚本应该已经可以按照你设定的频率自动运行了，但是推荐手动测试一下，手动测试点击右侧的“Run workflow” - “Run workflow”就可以手动运行一次了。
    
8. （附加）请手动用浏览器登录一次门户，确保不会有人脸识别授权页面（点击接受或拒绝后便不会再显示该页面）以及微信二维码页面（扫码关注北大信息门户公众号后便不会再弹出该窗口），这两个页面都会干扰程序的正常运行。
    


## 如何修改自动报备的频率
    
通过修改.github/workflows/main.yml Line 6的corn表达式来实现。
    
默认值是 '0 4 * * 3,4,5'，这表示每周三四五UTC 4:00，即北京时间中午12点，执行出校和入校报备各一次。
    
可以通过编辑单引号内的五个字段来改变报备频率，这五个字段分别表示UTC时间的分钟、小时、日期、月份、星期几，比如 '0 0,2 * * 1,2,3,4,5' 表示周一到周五的北京时间八点和十点执行。有关corn表达式的更多信息，可以自行利用搜索引擎搜索。

## 如何取消自动报备

Settings -> Actions -> Disabled Actions
    
也可以直接删除你fork的仓库

也可以删除./github/workflows

也可以编辑./github/workflows/main.yml, 在Line5 Line6前面加个“#”号，注释掉它们
    
## Q&A
如果你有什么问题，可以在【xiazhongyv/PKUAutoSubmit_online】下面那一栏里找到 Issues，提交你的问题

Q：报错，IAAA登录失败

A：请手动登录下门户，检查下是否会弹出人脸验证授权，这个授权页面会干扰程序运行，它只会在门户显示一次，处理后重新运行就好了。以及还有可能是微信扫码关注门户的页面，只要微信扫码关注了，就不会再弹出这个二维码页面了。如果还不行请重新设置下Secrets的账户密码确保没有输入错误。如果还不行请把报错信息提交到issues.
    

Q：报错，缺失ID/PASSWORD/SENDKEY等参数
    
A：要在repo的Setting - Secrets里设置这几个值哦，点进New Repository secret会有两栏，KEY填写全大写的字母ID或PASSWORD或SENDKEY或其他，value填写具体的内容。
    
    
Q：报错，超时错误
    
A：目前我查看了一些fork repo的actions，以及接收到了一些反馈，目前大多数账号是可以反复运行并保证报备成功的，有少部分账号会偶发甚至持续出现超时报错，目前正在排查原因。
 
AA：排查了半天，没找到问题，感觉就是报备网站不稳定，可能要改成每天上下午各运行一次要好一些？
    
AAA: 感谢Xzonn大佬的PR，超时有可能是因为有的同学没有默认的邮箱和手机号，导致“提交”按钮处于不可点击的状态。现在已经更新了，请无法运行的大家Fetch upstream或重新Fork试一下~
  
    
Q：报错，xxxxxxx.sh: line 4: syntax error near unexpected token xx 语法错误
    
A：请在Secrets填写你的密码时双引号包裹起你的密码，报这个语法错误是因为你的Secrets里有特殊字符
    
    
Q：Actions workflow没有按时运行/我没有在指定的时间收到微信提醒

A：Github Actions由于是免费资源，本身资源有限，所以实际上workflow是在指定的时间开始排队。报备这种事晚个几分钟十几分钟问题不大。不过如果想要准点收到报备成功信息，一个比较好的策略是避开整点半点时间。如果workflow完全没有按照计划运行，请提交issue.
    
    
Q：workflow运行不了，按钮是不可点击状态

A：找一找页面上有没有关于是否允许脚本在fork的仓库上运行的提示，点击“Enable...”就好

    
## 免责声明
本代码只供参考学习，造成的一切后果由使用者自行承担。

本品的开发初衷是拯救需要每天出入校的科研党，利人利己，欢迎大家扩散。如果有任何问题或警告，我会立即删除该项目。

