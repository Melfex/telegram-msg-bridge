<#-- Commands Discription -->
start-command-discription = Reiniciar o bot
help-command-discription = Mostrar a ajuda
links-command-discription = Minhas páginas
language-command-discription = Mudar idioma


<#-- Commands Dialog -->
start-dialog = <b>Olá! 👋</b>

                Eu ajudo você a falar com o dono de forma <b>direta</b> e <b>anônima</b>.

                Para começar, escolha um dos botões abaixo 👇:

help-dialog = <b>Guia do bot 🆘</b>

            • <b>Mensagem direta</b> 💌: sua mensagem chega ao dono junto com a sua identidade.
            • <b>Mensagem anônima</b> 🥷: sua mensagem é enviada sem revelar sua identidade.
            • Você pode enviar qualquer conteúdo ( texto, foto, vídeo, voz, etc. ) como <b>uma única mensagem</b>.
            • Após a análise, a resposta do dono é entregue a você automaticamente.

            ⚠️ Até receber uma resposta, evite <b>bloquear</b> o bot.

links-dialog = 💠 Minhas páginas nas redes sociais:

language-dialog = <b>Por favor, escolha seu idioma 👇</b>
language-changed-dialog = Idioma atualizado ✅


<#-- Buttons Dialog -->
message-btn = Mensagem direta |💌
anonymous-message-btn = 🥷| Mensagem anônima
links-btn = 📟| Minhas páginas
help-btn = Ajuda |🆘
language-btn = 💱 Mudar idioma 💱

cancel-btn = 🔙| Cancelar
reply-btn = • Responder ao usuário •
block-btn = 🚫| Bloquear
unblock-btn = ☑️| Desbloquear



<#-- Messaging Flow -->
send-direct-dialog = <b>Bem-vindo(a) 💛.</b>

                    Você pode enviar sua mensagem como <b>uma única mensagem</b> em qualquer formato ( <tg-spoiler>texto, foto, vídeo, etc.</tg-spoiler> ). Observe que sua identidade ficará <b>visível</b> para o dono.

                    Evite <b>bloquear</b> o bot antes de receber uma resposta; além disso, a <b>cortesia</b> é indispensável.

                    <b>Envie sua mensagem 👇🏻:</b>

send-anon-dialog = <b>Bem-vindo(a) 💛.</b>

                    Você pode enviar sua mensagem como <b>uma única mensagem</b> em qualquer formato ( <tg-spoiler>texto, foto, vídeo, etc.</tg-spoiler> ). Observe que sua identidade <b>não ficará visível</b> para o dono.

                    Evite <b>bloquear</b> o bot antes de receber uma resposta; além disso, a <b>cortesia</b> é indispensável.

                    <b>Envie sua mensagem 👇🏻:</b>

cancelled-dialog = A operação foi cancelada e voltamos ao menu <b>principal</b>.

            Para continuar, escolha um dos botões abaixo 👇:

message-delivered-dialog = Sua mensagem foi recebida e enviada ✅;

                    Por favor, tenha <b>paciência</b> até receber a resposta final e <u>evite bloquear o bot</u>, pois após bloqueá-lo você <u>não</u> receberá sua resposta.

                    Para usar o bot, escolha um dos botões abaixo 👇🏻:

you-are-blocked-dialog = <b>Prezado usuário ❕;</b>
                        Sua conta foi bloqueada e você não pode mais usar os serviços do bot.

dont-spam-dialog = <b>Mais devagar ‼️ </b>
                    Você foi bloqueado por <code>{ $block_duration }</code> segundos por spam.

<#-- Owner Panel -->
panel-dialog = <b>Painel de administração 🛠</b>

            Bem-vindo de volta, proprietário. Escolha uma ação abaixo 👇:

toggle-bot-btn = 🔌| Ligar/desligar bot
block-user-btn = 🚫| Bloquear usuário
unblock-user-btn = ✅| Desbloquear usuário
broadcast-btn = 📢| Transmissão

bot-enabled-dialog = O bot agora está <b>online</b> ✅
bot-disabled-dialog = O bot agora está <b>offline</b> ⛔️

bot-status-dialog = <b>Status do bot ⚙️</b>

            Escolha o status do bot abaixo; o atual aparece em verde 👇:
bot-status-on-btn = 🟢 Online
bot-status-off-btn = 🔴 Offline
back-panel-btn = 🔙 Voltar ao painel

ask-user-id-dialog = Envie o <b>ID numérico</b> do usuário 👇:
invalid-id-dialog = ⚠️ ID inválido. Envie um ID numérico válido.

broadcast-ask-dialog = Envie a mensagem que deseja transmitir a todos os usuários 👇:
broadcast-started-dialog = 📢 Transmissão iniciada para <b>{ $total }</b> usuários…
broadcast-report-dialog = ✅ Transmissão concluída.

            • Enviados: <b>{ $sent }</b>
            • Falhas: <b>{ $failed }</b>
            • Total: <b>{ $total }</b>

<#-- Access Gate -->
bot-off-dialog = <b>O bot está offline no momento ⛔️</b>

            Tente novamente mais tarde.

owner-reply-dialog = 💌•  Sua mensagem foi <b>analisada</b> e <b>respondida</b>.

                    📝- Texto da resposta:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = Prezado dono, uma nova mensagem chegou para você;
                    <b>👤- Nome:</b><code> { $name } </code>
                    <b>🆔- ID do usuário:</b><code> { $user_id } </code>
                    <b>🫆- Nome de usuário:</b><code> { $user_name } </code>
                    <b>📝- Mensagem:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = Prezado dono, uma nova mensagem anônima chegou para você;
                    <b>📝- Mensagem:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = Envie sua resposta a esta mensagem como uma única mensagem (texto, vídeo, voz, etc.). Para cancelar, use o botão abaixo.
reply-sent-dialog = Resposta enviada com sucesso! ✅
user-blocked-dialog = Usuário bloqueado ✅
user-unblocked-dialog = Usuário desbloqueado ✅
reaction-sent-dialog = Reação adicionada ✅
