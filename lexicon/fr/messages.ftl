<#-- Commands Discription -->
start-command-discription = Redémarrer le bot
help-command-discription = Afficher l’aide
links-command-discription = Mes pages
language-command-discription = Changer de langue


<#-- Commands Dialog -->
start-dialog = <b>Bonjour ! 👋</b>

                Je vous aide à joindre le propriétaire de façon <b>directe</b> et <b>anonyme</b>.

                Pour commencer, choisissez l’un des boutons ci-dessous 👇 :

help-dialog = <b>Guide du bot 🆘</b>

            • <b>Message direct</b> 💌 : votre message parvient au propriétaire avec votre identité.
            • <b>Message anonyme</b> 🥷 : votre message est envoyé sans révéler votre identité.
            • Vous pouvez envoyer tout contenu ( texte, photo, vidéo, voix, etc. ) en <b>un seul message</b>.
            • Après examen, la réponse du propriétaire vous est transmise automatiquement.

            ⚠️ Tant que vous n’avez pas reçu de réponse, évitez de <b>bloquer</b> le bot.

links-dialog = 💠 Mes réseaux sociaux :

language-dialog = <b>Veuillez choisir votre langue 👇</b>
language-changed-dialog = Langue mise à jour ✅


<#-- Buttons Dialog -->
message-btn = Message direct |💌
anonymous-message-btn = 🥷| Message anonyme
links-btn = 📟| Mes pages
help-btn = Aide |🆘
language-btn = 💱 Changer de langue 💱

cancel-btn = 🔙| Annuler
reply-btn = • Répondre à l’utilisateur •
block-btn = 🚫| Bloquer
unblock-btn = ☑️| Débloquer



<#-- Messaging Flow -->
send-direct-dialog = <b>Bienvenue 💛.</b>

                    Vous pouvez envoyer votre message en <b>un seul message</b> dans n’importe quel format ( <tg-spoiler>texte, photo, vidéo, etc.</tg-spoiler> ). Notez que votre identité sera <b>visible</b> par le propriétaire.

                    Veuillez éviter de <b>bloquer</b> le bot avant d’avoir reçu une réponse ; la <b>politesse</b> est également indispensable.

                    <b>Envoyez votre message 👇🏻 :</b>

send-anon-dialog = <b>Bienvenue 💛.</b>

                    Vous pouvez envoyer votre message en <b>un seul message</b> dans n’importe quel format ( <tg-spoiler>texte, photo, vidéo, etc.</tg-spoiler> ). Notez que votre identité <b>ne sera pas visible</b> par le propriétaire.

                    Veuillez éviter de <b>bloquer</b> le bot avant d’avoir reçu une réponse ; la <b>politesse</b> est également indispensable.

                    <b>Envoyez votre message 👇🏻 :</b>

cancelled-dialog = L’opération a été annulée et nous sommes revenus au menu <b>principal</b>.

            Pour continuer, choisissez l’un des boutons ci-dessous 👇 :

message-delivered-dialog = Votre message a été reçu et envoyé ✅ ;

                    Veuillez faire preuve de <b>patience</b> jusqu’à la réponse finale et <u>éviter de bloquer le bot</u>, car après l’avoir bloqué vous <u>ne</u> recevrez pas votre réponse.

                    Pour utiliser le bot, choisissez l’un des boutons ci-dessous 👇🏻 :

you-are-blocked-dialog = <b>Cher utilisateur ❕ ;</b>
                        Votre compte a été bloqué et vous ne pouvez plus utiliser les services du bot.

owner-reply-dialog = 💌•  Votre message a été <b>examiné</b> et <b>une réponse</b> y a été apportée.

                    📝- Texte de la réponse :
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Cher propriétaire, un nouveau message vous est parvenu ;
                    <b>👤- Nom :</b><code> { $name } </code>
                    <b>🆔- ID utilisateur :</b><code> { $user_id } </code>
                    <b>🫆- Nom d’utilisateur :</b><code> { $user_name } </code>
                    <b>📝- Message :</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Cher propriétaire, un nouveau message anonyme vous est parvenu ;
                    <b>📝- Message :</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Envoyez votre réponse à ce message en un seul message (texte, vidéo, voix, etc.). Pour annuler, utilisez le bouton ci-dessous.
reply-sent-dialog = Réponse envoyée avec succès ! ✅
user-blocked-dialog = Utilisateur bloqué ✅
user-unblocked-dialog = Utilisateur débloqué ✅
reaction-sent-dialog = Réaction ajoutée ✅
