<#-- Commands Discription -->
start-command-discription = Botu yeniden başlat
help-command-discription = Yardımı göster
links-command-discription = Sayfalarım
language-command-discription = Dili değiştir


<#-- Commands Dialog -->
start-dialog = <b>Merhaba! 👋</b>

                Sahibe hem <b>doğrudan</b> hem de <b>anonim</b> olarak ulaşmana yardımcı oluyorum.

                Başlamak için aşağıdaki düğmelerden birini seç 👇:

help-dialog = <b>Bot kılavuzu 🆘</b>

            • <b>Doğrudan mesaj</b> 💌: mesajın kimliğinle birlikte sahibe ulaşır.
            • <b>Anonim mesaj</b> 🥷: mesajın kimliğini açıklamadan gönderilir.
            • Her türlü içeriği ( metin, fotoğraf, video, ses vb. ) <b>tek mesaj</b> olarak gönderebilirsin.
            • İncelemenin ardından sahibin yanıtı sana otomatik olarak iletilir.

            ⚠️ Yanıt alana kadar lütfen botu <b>engelleme</b>.

links-dialog = 💠 Sosyal medya sayfalarım:

language-dialog = <b>Lütfen dilini seç 👇</b>
language-changed-dialog = Dil güncellendi ✅


<#-- Buttons Dialog -->
message-btn = Doğrudan mesaj |💌
anonymous-message-btn = 🥷| Anonim mesaj
links-btn = 📟| Sayfalarım
help-btn = Yardım |🆘
language-btn = 💱 Dili değiştir 💱

cancel-btn = 🔙| İptal
reply-btn = • Kullanıcıya yanıt ver •
block-btn = 🚫| Engelle
unblock-btn = ☑️| Engeli kaldır



<#-- Messaging Flow -->
send-direct-dialog = <b>Hoş geldin 💛.</b>

                    Mesajını herhangi bir biçimde <b>tek bir mesaj</b> olarak gönderebilirsin ( <tg-spoiler>metin, fotoğraf, video vb.</tg-spoiler> ). Kimliğinin sahibe <b>görünür</b> olacağını unutma.

                    Yanıt almadan önce lütfen botu <b>engelleme</b>; ayrıca <b>nezaket</b> de şarttır.

                    <b>Mesajını gönder 👇🏻:</b>

send-anon-dialog = <b>Hoş geldin 💛.</b>

                    Mesajını herhangi bir biçimde <b>tek bir mesaj</b> olarak gönderebilirsin ( <tg-spoiler>metin, fotoğraf, video vb.</tg-spoiler> ). Kimliğinin sahibe <b>görünmeyeceğini</b> unutma.

                    Yanıt almadan önce lütfen botu <b>engelleme</b>; ayrıca <b>nezaket</b> de şarttır.

                    <b>Mesajını gönder 👇🏻:</b>

cancelled-dialog = İşlem iptal edildi ve <b>ana</b> menüye döndük.

            Devam etmek için aşağıdaki düğmelerden birini seç 👇:

message-delivered-dialog = Mesajın alındı ve iletildi ✅;

                    Lütfen nihai yanıtı alana kadar <b>sabırlı</b> ol ve <u>botu engelleme</u>, çünkü engelledikten sonra yanıtını <u>alamazsın</u>.

                    Botu kullanmak için aşağıdaki düğmelerden birini seç 👇🏻:

you-are-blocked-dialog = <b>Değerli kullanıcı ❕;</b>
                        Hesabın engellendi ve artık botun hizmetlerini kullanamazsın.

owner-reply-dialog = 💌•  Mesajın <b>incelendi</b> ve <b>yanıtlandı</b>.

                    📝- Yanıt metni:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Değerli sahip, sana yeni bir mesaj geldi;
                    <b>👤- Ad:</b><code> { $name } </code>
                    <b>🆔- Kullanıcı kimliği:</b><code> { $user_id } </code>
                    <b>🫆- Kullanıcı adı:</b><code> { $user_name } </code>
                    <b>📝- Mesaj:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Değerli sahip, sana yeni bir anonim mesaj geldi;
                    <b>📝- Mesaj:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Bu mesaja yanıtını tek bir mesaj olarak gönder (metin, video, ses vb.). İptal etmek için aşağıdaki düğmeyi kullan.
reply-sent-dialog = Yanıt başarıyla gönderildi! ✅
user-blocked-dialog = Kullanıcı engellendi ✅
user-unblocked-dialog = Kullanıcının engeli kaldırıldı ✅
reaction-sent-dialog = Tepki eklendi ✅
