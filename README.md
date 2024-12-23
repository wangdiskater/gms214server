# A server emulator for Maplestory GMS v214.

Acquired from https://forum.ragezone.com/f427/java-v214-swordie-source-1209447/

The original version I acquired has no working cash shop, I managed to fix that. Although you still can't use the account cash shop inventory, and receive failed message after purchasing items, you can now buy things in the cash shop, the purchased item will go to your character inventory directly.

If you missing some files, just go to the link to download the original one, I only changed the src and sql folders.

Current fixes:
1. Cash shop
2. Kinesis skills (because kinesis is the most familiar class for me)

Known issues:
1. Based on the situations of Kinesis skills, I anticipate a lot of skill misbehaviours of other classes.
2. Mob drop data is missing, or I couldn't find them, this original author give drops based on levels, it's working, but not satisfying.
3. A lot of quest and NPC interactions and item interations are missing, for example, you can't get AbsoLab equipments from the shop.
4. V matrix displaying issue.
5. Some skills upgrading issue which cost skill points by skills that do not need them (like Ultimate - Psychic Shot).
6. Boss skill effects missing (eg. Lucid wouldn't cause any damage).
7. You could stuck at some mission maps due to the missing of quest scripts.
8. The runes on the map not working.
9. ...

You can download the v214 client from steam using [DepotDownloader](https://github.com/SteamRE/DepotDownloader), with -app 216150 -depot 216151 -manifest 976750626611673486.

Before running you may need wz folder in the root directory, you can aquire them by extracting all wz files in the v214 maplestory client you downloaded using either [WZ-Dumper](https://github.com/Xterminatorz/WZ-Dumper) (recommended, since it is simple to use and get smaller results, which are sufficient for the server) or [Harepacker](https://github.com/lastbattle/Harepacker-resurrected) (would unpack wz lossless). Or you can just download them from the original link.

Other things just follow the original thread I put above.

我用新楓之谷236版本（因为手头正好有）做的简单汉化文件下载，可能会因为版本不同导致少数文本不准确（比如版本更新修改了某些技能的效果之类）。链接：https://pan.baidu.com/s/13jZNW3bWqRPtgsi1heRIYA 提取码：8ol1


新增：
中文版步骤
1. 获取v214-server源码
2. 获取V214client
3. AuthHook_v214 编译获取ijl15.dll，放在214client目录下覆盖 
4. launcher 编译获取v214.exe
5. v214.exe 放到客户端目录下
6. 启动v214-server
7. 点击v214.exe启动服务

注意事项
1. 使用了lombok 安装插件和打开annotation
2. 设置resource文件夹。否则读不到配置文件路径