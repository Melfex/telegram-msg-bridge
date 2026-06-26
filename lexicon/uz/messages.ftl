<#-- Commands Discription -->
start-command-discription = Botni qayta ishga tushirish
help-command-discription = Yordamni ko‘rsatish
links-command-discription = Mening sahifalarim
language-command-discription = Tilni o‘zgartirish


<#-- Commands Dialog -->
start-dialog = <b>Salom! 👋</b>

                Egasi bilan <b>to‘g‘ridan-to‘g‘ri</b> va <b>anonim</b> bog‘lanishingizga yordam beraman.

                Boshlash uchun quyidagi tugmalardan birini tanlang 👇:

help-dialog = <b>Bot qo‘llanmasi 🆘</b>

            • <b>To‘g‘ridan-to‘g‘ri xabar</b> 💌: xabaringiz shaxsingiz bilan birga egasiga yetib boradi.
            • <b>Anonim xabar</b> 🥷: xabaringiz shaxsingizni oshkor qilmasdan yuboriladi.
            • Istalgan kontentni ( matn, rasm, video, ovoz va h.k. ) <b>bitta xabar</b> sifatida yuborishingiz mumkin.
            • Ko‘rib chiqilgach, egasining javobi sizga avtomatik yetkaziladi.

            ⚠️ Javob olmaguningizcha botni <b>bloklamang</b>.

links-dialog = 💠 Ijtimoiy tarmoqdagi sahifalarim:

language-dialog = <b>Iltimos, tilingizni tanlang 👇</b>
language-changed-dialog = Til yangilandi ✅


<#-- Buttons Dialog -->
message-btn = To‘g‘ridan-to‘g‘ri xabar |💌
anonymous-message-btn = 🥷| Anonim xabar
links-btn = 📟| Mening sahifalarim
help-btn = Yordam |🆘
language-btn = 💱 Tilni o‘zgartirish 💱

cancel-btn = 🔙| Bekor qilish
reply-btn = • Foydalanuvchiga javob •
block-btn = 🚫| Bloklash
unblock-btn = ☑️| Blokdan chiqarish



<#-- Messaging Flow -->
send-direct-dialog = <b>Xush kelibsiz 💛.</b>

                    Xabaringizni istalgan formatda <b>bitta xabar</b> sifatida yuborishingiz mumkin ( <tg-spoiler>matn, rasm, video va h.k.</tg-spoiler> ). E’tibor bering: shaxsingiz egasiga <b>ko‘rinadi</b>.

                    Javob olmasdan turib botni <b>bloklamang</b>; shuningdek <b>odob</b> ham shart.

                    <b>Xabaringizni yuboring 👇🏻:</b>

send-anon-dialog = <b>Xush kelibsiz 💛.</b>

                    Xabaringizni istalgan formatda <b>bitta xabar</b> sifatida yuborishingiz mumkin ( <tg-spoiler>matn, rasm, video va h.k.</tg-spoiler> ). E’tibor bering: shaxsingiz egasiga <b>ko‘rinmaydi</b>.

                    Javob olmasdan turib botni <b>bloklamang</b>; shuningdek <b>odob</b> ham shart.

                    <b>Xabaringizni yuboring 👇🏻:</b>

cancelled-dialog = Amal bekor qilindi va <b>asosiy</b> menyuga qaytdik.

            Davom etish uchun quyidagi tugmalardan birini tanlang 👇:

message-delivered-dialog = Xabaringiz qabul qilindi va yuborildi ✅;

                    Iltimos, yakuniy javobni olguningizcha <b>sabr</b> qiling va <u>botni bloklamang</u>, chunki bloklaganingizdan keyin javobni <u>ololmaysiz</u>.

                    Botdan foydalanish uchun quyidagi tugmalardan birini tanlang 👇🏻:

you-are-blocked-dialog = <b>Hurmatli foydalanuvchi ❕;</b>
                        Hisobingiz bloklandi va endi bot xizmatlaridan foydalana olmaysiz.

dont-spam-dialog = <b>Sekinroq ‼️ </b>
                    Spam tufayli <code>{ $block_duration }</code> soniyaga bloklandingiz.

<#-- Owner Panel -->
panel-dialog = <b>Boshqaruv paneli 🛠</b>

            Xush kelibsiz, egasi. Quyidan amalni tanlang 👇:

toggle-bot-btn = 🔌| Botni yoqish/oʻchirish
block-user-btn = 🚫| Foydalanuvchini bloklash
unblock-user-btn = ✅| Blokdan chiqarish
broadcast-btn = 📢| Ommaviy xabar

bot-enabled-dialog = Bot endi <b>yoniq</b> ✅
bot-disabled-dialog = Bot endi <b>oʻchiq</b> ⛔️

bot-status-dialog = <b>Bot holati ⚙️</b>

            Quyidan bot holatini tanlang; joriy holat yashil rangda belgilangan 👇:
bot-status-on-btn = 🟢 Yoniq
bot-status-off-btn = 🔴 Oʻchiq
back-panel-btn = 🔙 Panelga qaytish

ask-user-id-dialog = Foydalanuvchining <b>raqamli ID</b>sini yuboring 👇:
invalid-id-dialog = ⚠️ Notoʻgʻri ID. Toʻgʻri raqamli ID yuboring.

broadcast-ask-dialog = Barcha foydalanuvchilarga yubormoqchi boʻlgan xabaringizni yuboring 👇:
broadcast-started-dialog = 📢 Ommaviy yuborish <b>{ $total }</b> foydalanuvchi uchun boshlandi…
broadcast-report-dialog = ✅ Ommaviy yuborish tugadi.

            • Yuborildi: <b>{ $sent }</b>
            • Xatolik: <b>{ $failed }</b>
            • Jami: <b>{ $total }</b>

<#-- Access Gate -->
bot-off-dialog = <b>Bot hozircha oʻchiq ⛔️</b>

            Iltimos, keyinroq urinib koʻring.

owner-reply-dialog = 💌•  Xabaringiz <b>ko‘rib chiqildi</b> va unga <b>javob berildi</b>.

                    📝- Javob matni:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Hurmatli ega, sizga yangi xabar keldi;
                    <b>👤- Ism:</b><code> { $name } </code>
                    <b>🆔- Foydalanuvchi ID:</b><code> { $user_id } </code>
                    <b>🫆- Foydalanuvchi nomi:</b><code> { $user_name } </code>
                    <b>📝- Xabar:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Hurmatli ega, sizga yangi anonim xabar keldi;
                    <b>📝- Xabar:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Ushbu xabarga javobingizni bitta xabar sifatida yuboring (matn, video, ovoz va h.k.). Bekor qilish uchun quyidagi tugmadan foydalaning.
reply-sent-dialog = Javob muvaffaqiyatli yuborildi! ✅
user-blocked-dialog = Foydalanuvchi bloklandi ✅
user-unblocked-dialog = Foydalanuvchi blokdan chiqarildi ✅
reaction-sent-dialog = Reaksiya qo‘yildi ✅
