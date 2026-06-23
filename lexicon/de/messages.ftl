<#-- Commands Discription -->
start-command-discription = Bot neu starten
help-command-discription = Hilfe anzeigen
links-command-discription = Meine Seiten
language-command-discription = Sprache ändern


<#-- Commands Dialog -->
start-dialog = <b>Hallo! 👋</b>

                Ich helfe dir, den Inhaber sowohl <b>direkt</b> als auch <b>anonym</b> zu erreichen.

                Wähle zum Starten eine der Schaltflächen unten 👇:

help-dialog = <b>Bot-Anleitung 🆘</b>

            • <b>Direkte Nachricht</b> 💌: Deine Nachricht erreicht den Inhaber zusammen mit deinen Daten.
            • <b>Anonyme Nachricht</b> 🥷: Deine Nachricht wird gesendet, ohne deine Identität preiszugeben.
            • Du kannst beliebige Inhalte ( Text, Foto, Video, Sprache usw. ) als <b>eine Nachricht</b> senden.
            • Nach der Prüfung wird dir die Antwort des Inhabers automatisch zugestellt.

            ⚠️ Bitte <b>blockiere</b> den Bot nicht, bis du eine Antwort erhalten hast.

links-dialog = 💠 Meine Social-Media-Seiten:

language-dialog = <b>Bitte wähle deine Sprache 👇</b>
language-changed-dialog = Sprache aktualisiert ✅


<#-- Buttons Dialog -->
message-btn = Direkte Nachricht |💌
anonymous-message-btn = 🥷| Anonyme Nachricht
links-btn = 📟| Meine Seiten
help-btn = Hilfe |🆘
language-btn = 💱 Sprache ändern 💱

cancel-btn = 🔙| Abbrechen
reply-btn = • Nutzer antworten •
block-btn = 🚫| Sperren
unblock-btn = ☑️| Entsperren



<#-- Messaging Flow -->
send-direct-dialog = <b>Willkommen 💛.</b>

                    Du kannst deine Nachricht als <b>eine einzige Nachricht</b> in jedem Format senden ( <tg-spoiler>Text, Foto, Video usw.</tg-spoiler> ). Beachte: Deine Daten sind für den Inhaber <b>sichtbar</b>.

                    Bitte <b>blockiere</b> den Bot nicht, bevor du eine Antwort erhalten hast; außerdem ist <b>Höflichkeit</b> erforderlich.

                    <b>Sende deine Nachricht 👇🏻:</b>

send-anon-dialog = <b>Willkommen 💛.</b>

                    Du kannst deine Nachricht als <b>eine einzige Nachricht</b> in jedem Format senden ( <tg-spoiler>Text, Foto, Video usw.</tg-spoiler> ). Beachte: Deine Daten sind für den Inhaber <b>nicht sichtbar</b>.

                    Bitte <b>blockiere</b> den Bot nicht, bevor du eine Antwort erhalten hast; außerdem ist <b>Höflichkeit</b> erforderlich.

                    <b>Sende deine Nachricht 👇🏻:</b>

cancelled-dialog = Der Vorgang wurde abgebrochen und wir sind zum <b>Hauptmenü</b> zurückgekehrt.

            Wähle zum Fortfahren eine der Schaltflächen unten 👇:

message-delivered-dialog = Deine Nachricht wurde empfangen und gesendet ✅;

                    Bitte habe <b>Geduld</b>, bis du die endgültige Antwort erhältst, und <u>blockiere den Bot nicht</u>, denn nach dem Blockieren erhältst du <u>keine</u> Antwort.

                    Wähle eine der Schaltflächen unten, um den Bot zu nutzen 👇🏻:

you-are-blocked-dialog = <b>Sehr geehrter Nutzer ❕;</b>
                        Dein Konto wurde gesperrt und du kannst die Dienste des Bots nicht mehr nutzen.

dont-spam-dialog = <b>Langsamer ‼️ </b>
                    Du wurdest wegen Spam für <code>{ $block_duration }</code> Sekunden gesperrt.

owner-reply-dialog = 💌•  Deine Nachricht wurde <b>geprüft</b> und <b>beantwortet</b>.

                    📝- Antworttext:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Sehr geehrter Inhaber, eine neue Nachricht ist für dich eingegangen;
                    <b>👤- Name:</b><code> { $name } </code>
                    <b>🆔- Benutzer-ID:</b><code> { $user_id } </code>
                    <b>🫆- Benutzername:</b><code> { $user_name } </code>
                    <b>📝- Nachricht:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Sehr geehrter Inhaber, eine neue anonyme Nachricht ist für dich eingegangen;
                    <b>📝- Nachricht:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Sende deine Antwort auf diese Nachricht als eine einzige Nachricht (Text, Video, Sprache usw.). Zum Abbrechen die Schaltfläche unten verwenden.
reply-sent-dialog = Antwort erfolgreich gesendet! ✅
user-blocked-dialog = Nutzer gesperrt ✅
user-unblocked-dialog = Nutzer entsperrt ✅
reaction-sent-dialog = Reaktion gesetzt ✅
