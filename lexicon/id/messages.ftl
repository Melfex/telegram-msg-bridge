<#-- Commands Discription -->
start-command-discription = Mulai ulang bot
help-command-discription = Tampilkan bantuan
links-command-discription = Halaman saya
language-command-discription = Ubah bahasa


<#-- Commands Dialog -->
start-dialog = <b>Halo! 👋</b>

                Saya membantu Anda menghubungi pemilik secara <b>langsung</b> maupun <b>anonim</b>.

                Untuk memulai, pilih salah satu tombol di bawah 👇:

help-dialog = <b>Panduan bot 🆘</b>

            • <b>Pesan langsung</b> 💌: pesan Anda sampai ke pemilik beserta identitas Anda.
            • <b>Pesan anonim</b> 🥷: pesan Anda dikirim tanpa mengungkap identitas.
            • Anda dapat mengirim konten apa pun ( teks, foto, video, suara, dll. ) sebagai <b>satu pesan</b>.
            • Setelah ditinjau, balasan pemilik akan dikirim kepada Anda secara otomatis.

            ⚠️ Jangan <b>memblokir</b> bot sampai Anda menerima balasan.

links-dialog = 💠 Halaman media sosial saya:

language-dialog = <b>Silakan pilih bahasa Anda 👇</b>
language-changed-dialog = Bahasa diperbarui ✅


<#-- Buttons Dialog -->
message-btn = Pesan langsung |💌
anonymous-message-btn = 🥷| Pesan anonim
links-btn = 📟| Halaman saya
help-btn = Bantuan |🆘
language-btn = 💱 Ubah bahasa 💱

cancel-btn = 🔙| Batal
reply-btn = • Balas pengguna •
block-btn = 🚫| Blokir
unblock-btn = ☑️| Buka blokir



<#-- Messaging Flow -->
send-direct-dialog = <b>Selamat datang 💛.</b>

                    Anda dapat mengirim pesan sebagai <b>satu pesan</b> dalam format apa pun ( <tg-spoiler>teks, foto, video, dll.</tg-spoiler> ). Perlu diingat, identitas Anda akan <b>terlihat</b> oleh pemilik.

                    Mohon jangan <b>memblokir</b> bot sebelum menerima balasan; selain itu, <b>kesopanan</b> adalah keharusan.

                    <b>Kirim pesan Anda 👇🏻:</b>

send-anon-dialog = <b>Selamat datang 💛.</b>

                    Anda dapat mengirim pesan sebagai <b>satu pesan</b> dalam format apa pun ( <tg-spoiler>teks, foto, video, dll.</tg-spoiler> ). Perlu diingat, identitas Anda <b>tidak akan terlihat</b> oleh pemilik.

                    Mohon jangan <b>memblokir</b> bot sebelum menerima balasan; selain itu, <b>kesopanan</b> adalah keharusan.

                    <b>Kirim pesan Anda 👇🏻:</b>

cancelled-dialog = Operasi dibatalkan dan kita kembali ke menu <b>utama</b>.

            Untuk melanjutkan, pilih salah satu tombol di bawah 👇:

message-delivered-dialog = Pesan Anda telah diterima dan dikirim ✅;

                    Mohon <b>bersabar</b> hingga menerima balasan akhir dan <u>jangan memblokir bot</u>, karena setelah memblokirnya Anda <u>tidak</u> akan menerima balasan.

                    Untuk menggunakan bot, pilih salah satu tombol di bawah 👇🏻:

you-are-blocked-dialog = <b>Pengguna yang terhormat ❕;</b>
                        Akun Anda telah diblokir dan Anda tidak dapat lagi menggunakan layanan bot.

dont-spam-dialog = <b>Pelan-pelan ‼️ </b>
                    Kamu diblokir selama <code>{ $block_duration }</code> detik karena spam.

<#-- Owner Panel -->
panel-dialog = <b>Panel admin 🛠</b>

            Selamat datang kembali, pemilik. Pilih tindakan di bawah 👇:

toggle-bot-btn = 🔌| Nyalakan/matikan bot
block-user-btn = 🚫| Blokir pengguna
unblock-user-btn = ✅| Buka blokir pengguna
broadcast-btn = 📢| Siaran

bot-enabled-dialog = Bot sekarang <b>aktif</b> ✅
bot-disabled-dialog = Bot sekarang <b>nonaktif</b> ⛔️

bot-status-dialog = <b>Status bot ⚙️</b>

            Pilih status bot di bawah; status saat ini ditandai dengan warna hijau 👇:
bot-status-on-btn = 🟢 Aktif
bot-status-off-btn = 🔴 Nonaktif
back-panel-btn = 🔙 Kembali ke panel

ask-user-id-dialog = Kirim <b>ID numerik</b> pengguna 👇:
invalid-id-dialog = ⚠️ ID tidak valid. Kirim ID numerik yang benar.

broadcast-ask-dialog = Kirim pesan yang ingin disiarkan ke semua pengguna 👇:
broadcast-started-dialog = 📢 Siaran dimulai untuk <b>{ $total }</b> pengguna…
broadcast-report-dialog = ✅ Siaran selesai.

            • Terkirim: <b>{ $sent }</b>
            • Gagal: <b>{ $failed }</b>
            • Total: <b>{ $total }</b>

<#-- Access Gate -->
bot-off-dialog = <b>Bot sedang nonaktif ⛔️</b>

            Silakan coba lagi nanti.

owner-reply-dialog = 💌•  Pesan Anda telah <b>ditinjau</b> dan <b>dibalas</b>.

                    📝- Teks balasan:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Pemilik yang terhormat, ada pesan baru untuk Anda;
                    <b>👤- Nama:</b><code> { $name } </code>
                    <b>🆔- ID pengguna:</b><code> { $user_id } </code>
                    <b>🫆- Nama pengguna:</b><code> { $user_name } </code>
                    <b>📝- Pesan:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Pemilik yang terhormat, ada pesan anonim baru untuk Anda;
                    <b>📝- Pesan:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Kirim balasan Anda untuk pesan ini sebagai satu pesan (teks, video, suara, dll.). Untuk membatalkan, gunakan tombol di bawah.
reply-sent-dialog = Balasan berhasil dikirim! ✅
user-blocked-dialog = Pengguna diblokir ✅
user-unblocked-dialog = Blokir pengguna dibuka ✅
reaction-sent-dialog = Reaksi ditambahkan ✅
