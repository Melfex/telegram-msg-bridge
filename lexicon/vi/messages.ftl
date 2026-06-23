<#-- Commands Discription -->
start-command-discription = Khởi động lại bot
help-command-discription = Hiển thị trợ giúp
links-command-discription = Trang của tôi
language-command-discription = Đổi ngôn ngữ


<#-- Commands Dialog -->
start-dialog = <b>Xin chào! 👋</b>

                Mình giúp bạn liên hệ với chủ sở hữu theo cả hai cách <b>trực tiếp</b> và <b>ẩn danh</b>.

                Để bắt đầu, hãy chọn một trong các nút bên dưới 👇:

help-dialog = <b>Hướng dẫn bot 🆘</b>

            • <b>Tin nhắn trực tiếp</b> 💌: tin nhắn của bạn đến chủ sở hữu kèm theo danh tính của bạn.
            • <b>Tin nhắn ẩn danh</b> 🥷: tin nhắn của bạn được gửi mà không tiết lộ danh tính.
            • Bạn có thể gửi mọi nội dung ( văn bản, ảnh, video, giọng nói, v.v. ) dưới dạng <b>một tin nhắn</b>.
            • Sau khi xem xét, câu trả lời của chủ sở hữu sẽ được gửi đến bạn tự động.

            ⚠️ Cho đến khi nhận được trả lời, vui lòng đừng <b>chặn</b> bot.

links-dialog = 💠 Các trang mạng xã hội của tôi:

language-dialog = <b>Vui lòng chọn ngôn ngữ của bạn 👇</b>
language-changed-dialog = Đã cập nhật ngôn ngữ ✅


<#-- Buttons Dialog -->
message-btn = Tin nhắn trực tiếp |💌
anonymous-message-btn = 🥷| Tin nhắn ẩn danh
links-btn = 📟| Trang của tôi
help-btn = Trợ giúp |🆘
language-btn = 💱 Đổi ngôn ngữ 💱

cancel-btn = 🔙| Hủy
reply-btn = • Trả lời người dùng •
block-btn = 🚫| Chặn
unblock-btn = ☑️| Bỏ chặn



<#-- Messaging Flow -->
send-direct-dialog = <b>Chào mừng 💛.</b>

                    Bạn có thể gửi tin nhắn dưới dạng <b>một tin nhắn duy nhất</b> ở bất kỳ định dạng nào ( <tg-spoiler>văn bản, ảnh, video, v.v.</tg-spoiler> ). Lưu ý rằng danh tính của bạn sẽ <b>hiển thị</b> với chủ sở hữu.

                    Vui lòng đừng <b>chặn</b> bot trước khi nhận được trả lời; ngoài ra, <b>lịch sự</b> là điều bắt buộc.

                    <b>Hãy gửi tin nhắn của bạn 👇🏻:</b>

send-anon-dialog = <b>Chào mừng 💛.</b>

                    Bạn có thể gửi tin nhắn dưới dạng <b>một tin nhắn duy nhất</b> ở bất kỳ định dạng nào ( <tg-spoiler>văn bản, ảnh, video, v.v.</tg-spoiler> ). Lưu ý rằng danh tính của bạn sẽ <b>không hiển thị</b> với chủ sở hữu.

                    Vui lòng đừng <b>chặn</b> bot trước khi nhận được trả lời; ngoài ra, <b>lịch sự</b> là điều bắt buộc.

                    <b>Hãy gửi tin nhắn của bạn 👇🏻:</b>

cancelled-dialog = Thao tác đã bị hủy và chúng ta đã quay lại menu <b>chính</b>.

            Để tiếp tục, hãy chọn một trong các nút bên dưới 👇:

message-delivered-dialog = Tin nhắn của bạn đã được nhận và gửi đi ✅;

                    Vui lòng <b>kiên nhẫn</b> cho đến khi nhận được trả lời cuối cùng và <u>đừng chặn bot</u>, vì sau khi chặn bạn sẽ <u>không</u> nhận được trả lời.

                    Để sử dụng bot, hãy chọn một trong các nút bên dưới 👇🏻:

you-are-blocked-dialog = <b>Người dùng thân mến ❕;</b>
                        Tài khoản của bạn đã bị chặn và bạn không thể sử dụng dịch vụ của bot nữa.

dont-spam-dialog = <b>Chậm lại ‼️ </b>
                    Bạn đã bị chặn trong <code>{ $block_duration }</code> giây vì spam.

owner-reply-dialog = 💌•  Tin nhắn của bạn đã được <b>xem xét</b> và <b>trả lời</b>.

                    📝- Nội dung trả lời:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Chủ sở hữu thân mến, bạn có một tin nhắn mới;
                    <b>👤- Tên:</b><code> { $name } </code>
                    <b>🆔- ID người dùng:</b><code> { $user_id } </code>
                    <b>🫆- Tên người dùng:</b><code> { $user_name } </code>
                    <b>📝- Tin nhắn:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Chủ sở hữu thân mến, bạn có một tin nhắn ẩn danh mới;
                    <b>📝- Tin nhắn:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Gửi câu trả lời của bạn cho tin nhắn này dưới dạng một tin nhắn (văn bản, video, giọng nói, v.v.). Để hủy, hãy dùng nút bên dưới.
reply-sent-dialog = Đã gửi câu trả lời thành công! ✅
user-blocked-dialog = Đã chặn người dùng ✅
user-unblocked-dialog = Đã bỏ chặn người dùng ✅
reaction-sent-dialog = Đã thêm cảm xúc ✅
