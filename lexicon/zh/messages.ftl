<#-- Commands Discription -->
start-command-discription = 重启机器人
help-command-discription = 显示帮助
links-command-discription = 我的主页
language-command-discription = 切换语言


<#-- Commands Dialog -->
start-dialog = <b>你好！👋</b>

                我可以帮助你以<b>实名</b>和<b>匿名</b>两种方式联系机主。

                开始之前，请选择下方的一个按钮 👇：

help-dialog = <b>机器人指南 🆘</b>

            • <b>实名消息</b> 💌：你的消息会连同身份信息一起发送给机主。
            • <b>匿名消息</b> 🥷：你的消息会在不透露身份的情况下发送。
            • 你可以以<b>一条消息</b>的形式发送任意内容（文字、图片、视频、语音等）。
            • 审核后，机主的回复会自动发送给你。

            ⚠️ 在收到回复之前，请不要<b>拉黑</b>机器人。

links-dialog = 💠 我的社交主页：

language-dialog = <b>请选择你的语言 👇</b>
language-changed-dialog = 语言已更新 ✅


<#-- Buttons Dialog -->
message-btn = 实名消息 |💌
anonymous-message-btn = 🥷| 匿名消息
links-btn = 📟| 我的主页
help-btn = 帮助 |🆘
language-btn = 💱 切换语言 💱

cancel-btn = 🔙| 取消
reply-btn = • 回复用户 •
block-btn = 🚫| 拉黑用户
unblock-btn = ☑️| 取消拉黑



<#-- Messaging Flow -->
send-direct-dialog = <b>欢迎 💛。</b>

                    你可以以<b>一条消息</b>的形式、用任意格式发送你的消息（ <tg-spoiler>文字、图片、视频等</tg-spoiler> ）。请注意，你的身份信息将对机主<b>可见</b>。

                    在收到回复之前，请不要<b>拉黑</b>机器人；同时，<b>礼貌</b>也是必须的。

                    <b>请发送你的消息 👇🏻：</b>

send-anon-dialog = <b>欢迎 💛。</b>

                    你可以以<b>一条消息</b>的形式、用任意格式发送你的消息（ <tg-spoiler>文字、图片、视频等</tg-spoiler> ）。请注意，你的身份信息将对机主<b>不可见</b>。

                    在收到回复之前，请不要<b>拉黑</b>机器人；同时，<b>礼貌</b>也是必须的。

                    <b>请发送你的消息 👇🏻：</b>

cancelled-dialog = 操作已取消，我们已返回<b>主</b>菜单。

            如需继续，请选择下方的一个按钮 👇：

message-delivered-dialog = 你的消息已收到并发送 ✅；

                    在收到最终回复之前，请<b>耐心</b>等待，并<u>不要拉黑机器人</u>，因为拉黑后你将<u>无法</u>收到回复。

                    如需使用机器人服务，请选择下方的一个按钮 👇🏻：

you-are-blocked-dialog = <b>尊敬的用户 ❕；</b>
                        你的账号已被封禁，将无法再使用机器人的服务。

dont-spam-dialog = <b>慢一点 ‼️ </b>
                    由于刷屏，你已被封禁 <code>{ $block_duration }</code> 秒。

owner-reply-dialog = 💌•  你的消息已被<b>查看</b>并<b>回复</b>。

                    📝- 回复内容：
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = 尊敬的机主，您收到一条新消息；
                    <b>👤- 姓名：</b><code> { $name } </code>
                    <b>🆔- 用户 ID：</b><code> { $user_id } </code>
                    <b>🫆- 用户名：</b><code> { $user_name } </code>
                    <b>📝- 消息内容：</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = 尊敬的机主，您收到一条新的匿名消息；
                    <b>📝- 消息内容：</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = 请以一条消息（文字、视频、语音等）发送你对该消息的回复。如需取消，请使用下方按钮。
reply-sent-dialog = 回复发送成功！✅
user-blocked-dialog = 用户已封禁 ✅
user-unblocked-dialog = 已解除用户封禁 ✅
reaction-sent-dialog = 已添加表情回应 ✅
