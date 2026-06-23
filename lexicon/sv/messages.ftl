<#-- Commands Discription -->
start-command-discription = Starta om boten
help-command-discription = Visa hjälpen
links-command-discription = Mina sidor
language-command-discription = Byt språk


<#-- Commands Dialog -->
start-dialog = <b>Hej! 👋</b>

                Jag hjälper dig att nå ägaren både <b>direkt</b> och <b>anonymt</b>.

                Välj en av knapparna nedan för att börja 👇:

help-dialog = <b>Bothjälp 🆘</b>

            • <b>Direktmeddelande</b> 💌: ditt meddelande når ägaren tillsammans med din identitet.
            • <b>Anonymt meddelande</b> 🥷: ditt meddelande skickas utan att avslöja din identitet.
            • Du kan skicka vilket innehåll som helst ( text, foto, video, röst, osv. ) som <b>ett enda meddelande</b>.
            • Efter granskning levereras ägarens svar automatiskt till dig.

            ⚠️ Blockera inte boten förrän du har fått ett svar.

links-dialog = 💠 Mina sociala medier:

language-dialog = <b>Välj ditt språk 👇</b>
language-changed-dialog = Språket har uppdaterats ✅


<#-- Buttons Dialog -->
message-btn = Direktmeddelande |💌
anonymous-message-btn = 🥷| Anonymt meddelande
links-btn = 📟| Mina sidor
help-btn = Hjälp |🆘
language-btn = 💱 Byt språk 💱

cancel-btn = 🔙| Avbryt
reply-btn = • Svara användaren •
block-btn = 🚫| Blockera
unblock-btn = ☑️| Avblockera



<#-- Messaging Flow -->
send-direct-dialog = <b>Välkommen 💛.</b>

                    Du kan skicka ditt meddelande som <b>ett enda meddelande</b> i valfritt format ( <tg-spoiler>text, foto, video, osv.</tg-spoiler> ). Observera att din identitet är <b>synlig</b> för ägaren.

                    Undvik att <b>blockera</b> boten innan du har fått ett svar; dessutom är <b>artighet</b> ett krav.

                    <b>Skicka ditt meddelande 👇🏻:</b>

send-anon-dialog = <b>Välkommen 💛.</b>

                    Du kan skicka ditt meddelande som <b>ett enda meddelande</b> i valfritt format ( <tg-spoiler>text, foto, video, osv.</tg-spoiler> ). Observera att din identitet <b>inte är synlig</b> för ägaren.

                    Undvik att <b>blockera</b> boten innan du har fått ett svar; dessutom är <b>artighet</b> ett krav.

                    <b>Skicka ditt meddelande 👇🏻:</b>

cancelled-dialog = Åtgärden avbröts och vi återvände till <b>huvudmenyn</b>.

            Välj en av knapparna nedan för att fortsätta 👇:

message-delivered-dialog = Ditt meddelande har tagits emot och skickats ✅;

                    Ha <b>tålamod</b> tills du får det slutgiltiga svaret och <u>blockera inte boten</u>, eftersom du efter blockering <u>inte</u> får ditt svar.

                    Välj en av knapparna nedan för att använda boten 👇🏻:

you-are-blocked-dialog = <b>Kära användare ❕;</b>
                        Ditt konto har blockerats och du kan inte längre använda botens tjänster.

dont-spam-dialog = <b>Ta det lugnt ‼️ </b>
                    Du har blockerats i <code>{ $block_duration }</code> sekunder på grund av spam.

owner-reply-dialog = 💌•  Ditt meddelande har <b>granskats</b> och <b>besvarats</b>.

                    📝- Svarstext:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Kära ägare, ett nytt meddelande har kommit till dig;
                    <b>👤- Namn:</b><code> { $name } </code>
                    <b>🆔- Användar-ID:</b><code> { $user_id } </code>
                    <b>🫆- Användarnamn:</b><code> { $user_name } </code>
                    <b>📝- Meddelande:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Kära ägare, ett nytt anonymt meddelande har kommit till dig;
                    <b>📝- Meddelande:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Skicka ditt svar på detta meddelande som ett enda meddelande (text, video, röst, osv.). Använd knappen nedan för att avbryta.
reply-sent-dialog = Svaret har skickats! ✅
user-blocked-dialog = Användaren blockerad ✅
user-unblocked-dialog = Användaren avblockerad ✅
reaction-sent-dialog = Reaktion tillagd ✅
