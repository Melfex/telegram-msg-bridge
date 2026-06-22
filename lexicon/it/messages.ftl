<#-- Commands Discription -->
start-command-discription = Riavvia il bot
help-command-discription = Mostra la guida
links-command-discription = Le mie pagine
language-command-discription = Cambia lingua


<#-- Commands Dialog -->
start-dialog = <b>Ciao! 👋</b>

                Ti aiuto a contattare il proprietario sia in modo <b>diretto</b> che <b>anonimo</b>.

                Per iniziare, scegli uno dei pulsanti qui sotto 👇:

help-dialog = <b>Guida del bot 🆘</b>

            • <b>Messaggio diretto</b> 💌: il tuo messaggio arriva al proprietario con la tua identità.
            • <b>Messaggio anonimo</b> 🥷: il tuo messaggio viene inviato senza rivelare la tua identità.
            • Puoi inviare qualsiasi contenuto ( testo, foto, video, voce, ecc. ) come <b>un unico messaggio</b>.
            • Dopo la verifica, la risposta del proprietario ti viene recapitata automaticamente.

            ⚠️ Finché non ricevi una risposta, evita di <b>bloccare</b> il bot.

links-dialog = 💠 Le mie pagine social:

language-dialog = <b>Scegli la tua lingua 👇</b>
language-changed-dialog = Lingua aggiornata ✅


<#-- Buttons Dialog -->
message-btn = Messaggio diretto |💌
anonymous-message-btn = 🥷| Messaggio anonimo
links-btn = 📟| Le mie pagine
help-btn = Guida |🆘
language-btn = 💱 Cambia lingua 💱

cancel-btn = 🔙| Annulla
reply-btn = • Rispondi all’utente •
block-btn = 🚫| Blocca
unblock-btn = ☑️| Sblocca



<#-- Messaging Flow -->
send-direct-dialog = <b>Benvenuto/a 💛.</b>

                    Puoi inviare il tuo messaggio come <b>un unico messaggio</b> in qualsiasi formato ( <tg-spoiler>testo, foto, video, ecc.</tg-spoiler> ). Nota che la tua identità sarà <b>visibile</b> al proprietario.

                    Evita di <b>bloccare</b> il bot prima di ricevere una risposta; inoltre la <b>cortesia</b> è indispensabile.

                    <b>Invia il tuo messaggio 👇🏻:</b>

send-anon-dialog = <b>Benvenuto/a 💛.</b>

                    Puoi inviare il tuo messaggio come <b>un unico messaggio</b> in qualsiasi formato ( <tg-spoiler>testo, foto, video, ecc.</tg-spoiler> ). Nota che la tua identità <b>non sarà visibile</b> al proprietario.

                    Evita di <b>bloccare</b> il bot prima di ricevere una risposta; inoltre la <b>cortesia</b> è indispensabile.

                    <b>Invia il tuo messaggio 👇🏻:</b>

cancelled-dialog = L’operazione è stata annullata e siamo tornati al menu <b>principale</b>.

            Per continuare, scegli uno dei pulsanti qui sotto 👇:

message-delivered-dialog = Il tuo messaggio è stato ricevuto e inviato ✅;

                    Ti preghiamo di avere <b>pazienza</b> fino alla risposta definitiva e di <u>non bloccare il bot</u>, perché dopo averlo bloccato <u>non</u> riceverai la risposta.

                    Per usare il bot, scegli uno dei pulsanti qui sotto 👇🏻:

you-are-blocked-dialog = <b>Gentile utente ❕;</b>
                        Il tuo account è stato bloccato e non puoi più utilizzare i servizi del bot.

owner-reply-dialog = 💌•  Il tuo messaggio è stato <b>esaminato</b> e ha ricevuto una <b>risposta</b>.

                    📝- Testo della risposta:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Gentile proprietario, è arrivato un nuovo messaggio per te;
                    <b>👤- Nome:</b><code> { $name } </code>
                    <b>🆔- ID utente:</b><code> { $user_id } </code>
                    <b>🫆- Nome utente:</b><code> { $user_name } </code>
                    <b>📝- Messaggio:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Gentile proprietario, è arrivato un nuovo messaggio anonimo per te;
                    <b>📝- Messaggio:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Invia la tua risposta a questo messaggio come un unico messaggio (testo, video, voce, ecc.). Per annullare, usa il pulsante qui sotto.
reply-sent-dialog = Risposta inviata con successo! ✅
user-blocked-dialog = Utente bloccato ✅
user-unblocked-dialog = Utente sbloccato ✅
reaction-sent-dialog = Reazione impostata ✅
