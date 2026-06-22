<#-- Commands Discription -->
start-command-discription = Mulakan semula bot
help-command-discription = Tunjukkan bantuan
links-command-discription = Halaman saya
language-command-discription = Tukar bahasa


<#-- Commands Dialog -->
start-dialog = <b>Helo! 👋</b>

                Saya membantu anda menghubungi pemilik secara <b>terus</b> dan <b>tanpa nama</b>.

                Untuk bermula, pilih salah satu butang di bawah 👇:

help-dialog = <b>Panduan bot 🆘</b>

            • <b>Mesej terus</b> 💌: mesej anda sampai kepada pemilik bersama identiti anda.
            • <b>Mesej tanpa nama</b> 🥷: mesej anda dihantar tanpa mendedahkan identiti.
            • Anda boleh menghantar sebarang kandungan ( teks, foto, video, suara, dll. ) sebagai <b>satu mesej</b>.
            • Selepas disemak, balasan pemilik dihantar kepada anda secara automatik.

            ⚠️ Jangan <b>sekat</b> bot sehingga anda menerima balasan.

links-dialog = 💠 Halaman media sosial saya:

language-dialog = <b>Sila pilih bahasa anda 👇</b>
language-changed-dialog = Bahasa dikemas kini ✅


<#-- Buttons Dialog -->
message-btn = Mesej terus |💌
anonymous-message-btn = 🥷| Mesej tanpa nama
links-btn = 📟| Halaman saya
help-btn = Bantuan |🆘
language-btn = 💱 Tukar bahasa 💱

cancel-btn = 🔙| Batal
reply-btn = • Balas pengguna •
block-btn = 🚫| Sekat
unblock-btn = ☑️| Nyahsekat



<#-- Messaging Flow -->
send-direct-dialog = <b>Selamat datang 💛.</b>

                    Anda boleh menghantar mesej sebagai <b>satu mesej</b> dalam apa-apa format ( <tg-spoiler>teks, foto, video, dll.</tg-spoiler> ). Ambil perhatian, identiti anda akan <b>kelihatan</b> oleh pemilik.

                    Sila elakkan daripada <b>menyekat</b> bot sebelum menerima balasan; selain itu, <b>kesopanan</b> adalah wajib.

                    <b>Hantar mesej anda 👇🏻:</b>

send-anon-dialog = <b>Selamat datang 💛.</b>

                    Anda boleh menghantar mesej sebagai <b>satu mesej</b> dalam apa-apa format ( <tg-spoiler>teks, foto, video, dll.</tg-spoiler> ). Ambil perhatian, identiti anda <b>tidak akan kelihatan</b> oleh pemilik.

                    Sila elakkan daripada <b>menyekat</b> bot sebelum menerima balasan; selain itu, <b>kesopanan</b> adalah wajib.

                    <b>Hantar mesej anda 👇🏻:</b>

cancelled-dialog = Operasi dibatalkan dan kita kembali ke menu <b>utama</b>.

            Untuk meneruskan, pilih salah satu butang di bawah 👇:

message-delivered-dialog = Mesej anda telah diterima dan dihantar ✅;

                    Sila <b>bersabar</b> sehingga menerima balasan akhir dan <u>jangan sekat bot</u>, kerana selepas menyekatnya anda <u>tidak</u> akan menerima balasan.

                    Untuk menggunakan bot, pilih salah satu butang di bawah 👇🏻:

you-are-blocked-dialog = <b>Pengguna yang dihormati ❕;</b>
                        Akaun anda telah disekat dan anda tidak lagi boleh menggunakan perkhidmatan bot.

owner-reply-dialog = 💌•  Mesej anda telah <b>disemak</b> dan <b>dibalas</b>.

                    📝- Teks balasan:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Pemilik yang dihormati, ada mesej baharu untuk anda;
                    <b>👤- Nama:</b><code> { $name } </code>
                    <b>🆔- ID pengguna:</b><code> { $user_id } </code>
                    <b>🫆- Nama pengguna:</b><code> { $user_name } </code>
                    <b>📝- Mesej:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Pemilik yang dihormati, ada mesej tanpa nama baharu untuk anda;
                    <b>📝- Mesej:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Hantar balasan anda kepada mesej ini sebagai satu mesej (teks, video, suara, dll.). Untuk membatalkan, gunakan butang di bawah.
reply-sent-dialog = Balasan berjaya dihantar! ✅
user-blocked-dialog = Pengguna disekat ✅
user-unblocked-dialog = Pengguna dinyahsekat ✅
reaction-sent-dialog = Reaksi ditambah ✅
