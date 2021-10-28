# AutoSubmit

无需代码基础，无需下载文件到你的电脑，无需保持自己电脑开机，无需配置服务器和环境的

自动出入校备案程序！

## 说明
本项目基于[PKUAutoSubmit](https://github.com/Bruuuuuuce/PKUAutoSubmit)3.0版本开发，因此跟随使用了Apache License 2.0证书

并且提供了Github Action支持，所以现在你无需下载任何文件到你自己的电脑或者服务器，更不需要时刻都开着电脑了。

## 如何使用

熟悉Github的大佬们请无视掉本节内容~ 因为是在Github提供的Linux服务器上运行的，不需要在本地配环境，而且以下内容适用于任何系统的用户。

0. （可选）右上角点个星星吧，不要下次一定嘛~

1. 首先你需要有一个Github账号，如果你现在还没有登录，就赶紧点击右上角登录Github吧！推荐使用edu邮箱注册。

2. （可选）然后如果你想要在每天自动报备后能够收到成功的提醒，那么可以在[Server酱](https://sct.ftqq.com/)用微信扫码登录，得到一个SENDKEY

3. 然后点击右上角的“Fork”，将该仓库分支到你自己，稍等片刻后，现在你应该在【你的ID/PKUActionSubmit】这个仓库里了。（当然，如果您不是github萌新，完全可以把代码clone在任何机器运行）

4. 然后在【你的ID/PKUActionSubmit】下面那一栏里找到找到 <>Code ，在文件列表里里找到config.ini，点进去后右上角有一个小铅笔的符号，点击它就能编辑出入校信息了，按照你想要的进行编辑完成后，翻到页面最下面，点击commit changes并确认就好了。如果你跳过了第2步，记得把微信通知那里改成False.

5. 然后在【你的ID/PKUActionSubmit】下面那一栏里找到 Settings ，点击，在左侧找到Secrets，点击

点击右侧New Repository secret，然后添加ID（大写的），然后输入你的学号

再点击右侧New Repository secret，然后添加PASSWORD（大写的），然后输入你的密码

再点击右侧New Repository secret，然后添加SENDKEY（大写的），然后输入你的SENDKEY（如果你不需要微信通知，就随便写点啥都行）

secret是github的保密字段，在这里填写的内容，在填写后没人能够看到它是什么，包括你自己，你只能修改它。

6. 然后在【你的ID/PKUActionSubmit】下面那一栏里找到 Actions，点进去，

可能会弹出提示框，点击“Enable...”允许脚本运行，

从左侧列表里选中PKUAutoSubmit，

可能上面还是会有一条提示说是否允许脚本在fork的仓库上运行，点击“Enable...”就好，

这个时候，脚本应该已经可以在每天中午十二点都运行一次了，但是推荐手动测试一下，手动测试点击右侧的“Run workflow” - “Run workflow”就可以手动运行一次了。

## 如何取消使用

你可以直接删除你fork的仓库

也可以删除./github/workflows

也可以编辑./github/workflows/main.yml, 在Line5 Line6前面加个“#”号，注释掉它们

## Q&A
如果你有什么问题，可以在【你的ID/PKUActionSubmit】下面那一栏里找到 Issues，提交你的问题

Q：Github Action 报错，IAAA登录失败
A：请手动登录下门户，检查下是否会弹出人脸验证授权，这个授权页面会干扰程序运行，它只会在门户显示一次，处理后重新运行就好了。如果还不行请重新设置下Secrets的账户密码。如果还不行请把报错信息提交到issues.
