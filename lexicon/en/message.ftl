<#-- Commands Discription -->
start-command-discription = Restart the bot
help-command-discription = Show the help
links-command-discription = My pages
language-command-discription = Change language


<#-- Commands Dialog -->
start-dialog = <b>Hello! 👋</b>

                I help you reach the owner both <b>directly</b> and <b>anonymously</b>.

                To get started, choose one of the buttons below 👇:

help-dialog = <b>Bot guide 🆘</b>

            • <b>Direct message</b> 💌: your message reaches the owner along with your identity.
            • <b>Anonymous message</b> 🥷: your message is sent without revealing your identity.
            • You can send any content ( text, photo, video, voice, etc. ) as <b>a single message</b>.
            • Once reviewed, the owner's reply is delivered to you automatically.

            ⚠️ Until you receive a reply, please avoid <b>blocking</b> the bot.

links-dialog = 💠 My social media pages:

language-dialog = <b>Please choose your language 👇</b>
language-changed-dialog = Language updated ✅


<#-- Buttons Dialog -->
message-btn = Direct message |💌
anonymous-message-btn = 🥷| Anonymous message
links-btn = 📟| My pages
help-btn = Help |🆘
language-btn = 💱 Change language 💱

cancel-btn = 🔙| Cancel
reply-btn = • Reply to user •
block-btn = 🚫| Block user
unblock-btn = ☑️| Unblock user



<#-- Messaging Flow -->
send-direct-dialog = <b>Welcome 💛.</b>

                    You can send your message as <b>a single message</b> in any format ( <tg-spoiler>text, photo, video, etc.</tg-spoiler> ). Note that your identity will be <b>visible</b> to the owner.

                    Please avoid <b>blocking</b> the bot before you receive your reply; also, <b>being polite</b> is a strict requirement.

                    <b>Send your message 👇🏻:</b>

send-anon-dialog = <b>Welcome 💛.</b>

                    You can send your message as <b>a single message</b> in any format ( <tg-spoiler>text, photo, video, etc.</tg-spoiler> ). Note that your identity will <b>not be visible</b> to the owner.

                    Please avoid <b>blocking</b> the bot before you receive your reply; also, <b>being polite</b> is a strict requirement.

                    <b>Send your message 👇🏻:</b>

cancelled-dialog = The operation was cancelled and we returned to the <b>main</b> menu.

            To continue, choose one of the buttons below 👇:

message-delivered-dialog = Your message has been received and delivered ✅;

                    Please be <b>patient</b> until you receive the final reply and <u>avoid blocking the bot</u>, because after blocking it you <u>will not</u> receive your answer.

                    To use the bot services, choose one of the buttons below 👇🏻:

you-are-blocked-dialog = <b>Dear user ❕;</b>
                        Your account has been blocked and you can no longer use the bot services.

dont-spam-dialog = <b>Slow down ‼️ </b>
                    You have been blocked for <code>{ $block_duration }</code> seconds due to spam.

<#-- Owner Panel -->
panel-dialog = <b>Admin panel 🛠</b>

            Welcome back, owner. Choose an action below 👇:

toggle-bot-btn = 🔌| Toggle bot
block-user-btn = 🚫| Block user
unblock-user-btn = ✅| Unblock user
broadcast-btn = 📢| Broadcast

bot-enabled-dialog = The bot is now <b>online</b> ✅
bot-disabled-dialog = The bot is now <b>offline</b> ⛔️

bot-status-dialog = <b>Bot status ⚙️</b>

            Choose the bot's status below; the current one is highlighted in green 👇:
bot-status-on-btn = 🟢 Online
bot-status-off-btn = 🔴 Offline
back-panel-btn = 🔙 Back to panel

ask-user-id-dialog = Send the <b>numeric ID</b> of the target user 👇:
invalid-id-dialog = ⚠️ Invalid ID. Please send a valid numeric user ID.

broadcast-ask-dialog = Send the message you want to broadcast to all users 👇:
broadcast-started-dialog = 📢 Broadcast started for <b>{ $total }</b> users…
broadcast-report-dialog = ✅ Broadcast finished.

            • Sent: <b>{ $sent }</b>
            • Failed: <b>{ $failed }</b>
            • Total: <b>{ $total }</b>

<#-- Access Gate -->
bot-off-dialog = <b>The bot is currently offline ⛔️</b>

            Please try again later.

owner-reply-dialog = 💌•  Your message has been <b>reviewed</b> and <b>answered</b>.

                    📝- Reply text:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Dear owner, a new message has arrived for you;
                    <b>👤- Name:</b><code> { $name } </code>
                    <b>🆔- User ID:</b><code> { $user_id } </code>
                    <b>🫆- Username:</b><code> { $user_name } </code>
                    <b>📝- Message:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Dear owner, a new anonymous message has arrived for you;
                    <b>📝- Message:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Send your reply to this message as a single message (text, video, voice, etc.). To cancel, use the button below.
reply-sent-dialog = The reply was sent successfully! ✅
user-blocked-dialog = User blocked ✅
user-unblocked-dialog = User unblocked ✅
reaction-sent-dialog = Reaction set ✅
