<#-- Commands Discription -->
start-command-discription = Bot opnieuw starten
help-command-discription = Help tonen
links-command-discription = Mijn pagina’s
language-command-discription = Taal wijzigen


<#-- Commands Dialog -->
start-dialog = <b>Hallo! 👋</b>

                Ik help je de eigenaar zowel <b>rechtstreeks</b> als <b>anoniem</b> te bereiken.

                Kies om te beginnen een van de knoppen hieronder 👇:

help-dialog = <b>Bot-handleiding 🆘</b>

            • <b>Direct bericht</b> 💌: je bericht bereikt de eigenaar samen met je identiteit.
            • <b>Anoniem bericht</b> 🥷: je bericht wordt verzonden zonder je identiteit te onthullen.
            • Je kunt elke inhoud ( tekst, foto, video, spraak, enz. ) als <b>één bericht</b> verzenden.
            • Na beoordeling wordt het antwoord van de eigenaar automatisch aan je bezorgd.

            ⚠️ Blokkeer de bot niet totdat je een antwoord hebt ontvangen.

links-dialog = 💠 Mijn socialmediapagina’s:

language-dialog = <b>Kies je taal 👇</b>
language-changed-dialog = Taal bijgewerkt ✅


<#-- Buttons Dialog -->
message-btn = Direct bericht |💌
anonymous-message-btn = 🥷| Anoniem bericht
links-btn = 📟| Mijn pagina’s
help-btn = Help |🆘
language-btn = 💱 Taal wijzigen 💱

cancel-btn = 🔙| Annuleren
reply-btn = • Reageren op gebruiker •
block-btn = 🚫| Blokkeren
unblock-btn = ☑️| Deblokkeren



<#-- Messaging Flow -->
send-direct-dialog = <b>Welkom 💛.</b>

                    Je kunt je bericht als <b>één enkel bericht</b> in elk formaat verzenden ( <tg-spoiler>tekst, foto, video, enz.</tg-spoiler> ). Let op: je identiteit is <b>zichtbaar</b> voor de eigenaar.

                    Blokkeer de bot niet voordat je een antwoord hebt ontvangen; bovendien is <b>beleefdheid</b> noodzakelijk.

                    <b>Verstuur je bericht 👇🏻:</b>

send-anon-dialog = <b>Welkom 💛.</b>

                    Je kunt je bericht als <b>één enkel bericht</b> in elk formaat verzenden ( <tg-spoiler>tekst, foto, video, enz.</tg-spoiler> ). Let op: je identiteit is <b>niet zichtbaar</b> voor de eigenaar.

                    Blokkeer de bot niet voordat je een antwoord hebt ontvangen; bovendien is <b>beleefdheid</b> noodzakelijk.

                    <b>Verstuur je bericht 👇🏻:</b>

cancelled-dialog = De bewerking is geannuleerd en we zijn terug naar het <b>hoofdmenu</b>.

            Kies om verder te gaan een van de knoppen hieronder 👇:

message-delivered-dialog = Je bericht is ontvangen en verzonden ✅;

                    Heb alsjeblieft <b>geduld</b> tot je het definitieve antwoord ontvangt en <u>blokkeer de bot niet</u>, want na het blokkeren ontvang je <u>geen</u> antwoord.

                    Kies een van de knoppen hieronder om de bot te gebruiken 👇🏻:

you-are-blocked-dialog = <b>Beste gebruiker ❕;</b>
                        Je account is geblokkeerd en je kunt de diensten van de bot niet meer gebruiken.

owner-reply-dialog = 💌•  Je bericht is <b>beoordeeld</b> en <b>beantwoord</b>.

                    📝- Antwoordtekst:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Beste eigenaar, er is een nieuw bericht voor je binnengekomen;
                    <b>👤- Naam:</b><code> { $name } </code>
                    <b>🆔- Gebruikers-ID:</b><code> { $user_id } </code>
                    <b>🫆- Gebruikersnaam:</b><code> { $user_name } </code>
                    <b>📝- Bericht:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Beste eigenaar, er is een nieuw anoniem bericht voor je binnengekomen;
                    <b>📝- Bericht:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Stuur je antwoord op dit bericht als één bericht (tekst, video, spraak, enz.). Gebruik de knop hieronder om te annuleren.
reply-sent-dialog = Antwoord succesvol verzonden! ✅
user-blocked-dialog = Gebruiker geblokkeerd ✅
user-unblocked-dialog = Gebruiker gedeblokkeerd ✅
reaction-sent-dialog = Reactie geplaatst ✅
