<#-- Commands Discription -->
start-command-discription = Reiniciar el bot
help-command-discription = Mostrar la ayuda
links-command-discription = Mis páginas
language-command-discription = Cambiar idioma


<#-- Commands Dialog -->
start-dialog = <b>¡Hola! 👋</b>

                Te ayudo a contactar con el propietario de forma <b>directa</b> y <b>anónima</b>.

                Para empezar, elige uno de los botones de abajo 👇:

help-dialog = <b>Guía del bot 🆘</b>

            • <b>Mensaje directo</b> 💌: tu mensaje llega al propietario junto con tu identidad.
            • <b>Mensaje anónimo</b> 🥷: tu mensaje se envía sin revelar tu identidad.
            • Puedes enviar cualquier contenido ( texto, foto, vídeo, voz, etc. ) como <b>un solo mensaje</b>.
            • Tras la revisión, la respuesta del propietario se te entrega automáticamente.

            ⚠️ Hasta que recibas una respuesta, evita <b>bloquear</b> el bot.

links-dialog = 💠 Mis redes sociales:

language-dialog = <b>Por favor, elige tu idioma 👇</b>
language-changed-dialog = Idioma actualizado ✅


<#-- Buttons Dialog -->
message-btn = Mensaje directo |💌
anonymous-message-btn = 🥷| Mensaje anónimo
links-btn = 📟| Mis páginas
help-btn = Ayuda |🆘
language-btn = 💱 Cambiar idioma 💱

cancel-btn = 🔙| Cancelar
reply-btn = • Responder al usuario •
block-btn = 🚫| Bloquear usuario
unblock-btn = ☑️| Desbloquear usuario



<#-- Messaging Flow -->
send-direct-dialog = <b>Bienvenido/a 💛.</b>

                    Puedes enviar tu mensaje como <b>un solo mensaje</b> en cualquier formato ( <tg-spoiler>texto, foto, vídeo, etc.</tg-spoiler> ). Ten en cuenta que tu identidad será <b>visible</b> para el propietario.

                    Por favor, evita <b>bloquear</b> el bot antes de recibir tu respuesta; además, la <b>cortesía</b> es un requisito imprescindible.

                    <b>Envía tu mensaje 👇🏻:</b>

send-anon-dialog = <b>Bienvenido/a 💛.</b>

                    Puedes enviar tu mensaje como <b>un solo mensaje</b> en cualquier formato ( <tg-spoiler>texto, foto, vídeo, etc.</tg-spoiler> ). Ten en cuenta que tu identidad <b>no será visible</b> para el propietario.

                    Por favor, evita <b>bloquear</b> el bot antes de recibir tu respuesta; además, la <b>cortesía</b> es un requisito imprescindible.

                    <b>Envía tu mensaje 👇🏻:</b>

cancelled-dialog = La operación se canceló y volvimos al menú <b>principal</b>.

            Para continuar, elige uno de los botones de abajo 👇:

message-delivered-dialog = Tu mensaje se recibió y se envió ✅;

                    Por favor, ten <b>paciencia</b> hasta recibir la respuesta final y <u>evita bloquear el bot</u>, ya que tras bloquearlo <u>no</u> recibirás tu respuesta.

                    Para usar los servicios del bot, elige uno de los botones de abajo 👇🏻:

you-are-blocked-dialog = <b>Estimado usuario ❕;</b>
                        Tu cuenta ha sido bloqueada y ya no podrás usar los servicios del bot.

dont-spam-dialog = <b>Más despacio ‼️ </b>
                    Has sido bloqueado durante <code>{ $block_duration }</code> segundos por spam.

owner-reply-dialog = 💌•  Tu mensaje fue <b>revisado</b> y <b>respondido</b>.

                    📝- Texto de la respuesta:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Estimado propietario, ha llegado un nuevo mensaje para ti;
                    <b>👤- Nombre:</b><code> { $name } </code>
                    <b>🆔- ID de usuario:</b><code> { $user_id } </code>
                    <b>🫆- Usuario:</b><code> { $user_name } </code>
                    <b>📝- Mensaje:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Estimado propietario, ha llegado un nuevo mensaje anónimo para ti;
                    <b>📝- Mensaje:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Envía tu respuesta a este mensaje como un solo mensaje (texto, vídeo, voz, etc.). Para cancelar, usa el botón de abajo.
reply-sent-dialog = ¡La respuesta se envió correctamente! ✅
user-blocked-dialog = Usuario bloqueado ✅
user-unblocked-dialog = Usuario desbloqueado ✅
reaction-sent-dialog = Reacción registrada ✅
