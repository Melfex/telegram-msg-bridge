<#-- Commands Discription -->
start-command-discription = 봇 다시 시작
help-command-discription = 도움말 표시
links-command-discription = 내 페이지
language-command-discription = 언어 변경


<#-- Commands Dialog -->
start-dialog = <b>안녕하세요! 👋</b>

                저는 여러분이 운영자에게 <b>직접</b> 그리고 <b>익명</b>으로 연락하도록 도와드립니다.

                시작하려면 아래 버튼 중 하나를 선택하세요 👇:

help-dialog = <b>봇 안내 🆘</b>

            • <b>직접 메시지</b> 💌: 메시지가 신원 정보와 함께 운영자에게 전달됩니다.
            • <b>익명 메시지</b> 🥷: 메시지가 신원을 밝히지 않고 전송됩니다.
            • 모든 콘텐츠(텍스트, 사진, 동영상, 음성 등)를 <b>하나의 메시지</b>로 보낼 수 있습니다.
            • 검토 후 운영자의 답변이 자동으로 전달됩니다.

            ⚠️ 답변을 받기 전까지 봇을 <b>차단</b>하지 마세요.

links-dialog = 💠 내 소셜 미디어 페이지:

language-dialog = <b>언어를 선택해 주세요 👇</b>
language-changed-dialog = 언어가 변경되었습니다 ✅


<#-- Buttons Dialog -->
message-btn = 직접 메시지 |💌
anonymous-message-btn = 🥷| 익명 메시지
links-btn = 📟| 내 페이지
help-btn = 도움말 |🆘
language-btn = 💱 언어 변경 💱

cancel-btn = 🔙| 취소
reply-btn = • 사용자에게 답장 •
block-btn = 🚫| 사용자 차단
unblock-btn = ☑️| 차단 해제



<#-- Messaging Flow -->
send-direct-dialog = <b>환영합니다 💛.</b>

                    원하는 형식으로 메시지를 <b>하나의 메시지</b>로 보낼 수 있습니다 ( <tg-spoiler>텍스트, 사진, 동영상 등</tg-spoiler> ). 신원 정보가 운영자에게 <b>표시</b>된다는 점에 유의하세요.

                    답변을 받기 전에는 봇을 <b>차단</b>하지 마세요. 또한 <b>예의</b>는 필수입니다.

                    <b>메시지를 보내세요 👇🏻:</b>

send-anon-dialog = <b>환영합니다 💛.</b>

                    원하는 형식으로 메시지를 <b>하나의 메시지</b>로 보낼 수 있습니다 ( <tg-spoiler>텍스트, 사진, 동영상 등</tg-spoiler> ). 신원 정보가 운영자에게 <b>표시되지 않는다</b>는 점에 유의하세요.

                    답변을 받기 전에는 봇을 <b>차단</b>하지 마세요. 또한 <b>예의</b>는 필수입니다.

                    <b>메시지를 보내세요 👇🏻:</b>

cancelled-dialog = 작업이 취소되었으며 <b>메인</b> 메뉴로 돌아왔습니다.

            계속하려면 아래 버튼 중 하나를 선택하세요 👇:

message-delivered-dialog = 메시지가 수신되어 전송되었습니다 ✅;

                    최종 답변을 받을 때까지 <b>인내심</b>을 가지고 기다려 주시고 <u>봇을 차단하지 마세요</u>. 차단하면 답변을 <u>받지 못합니다</u>.

                    봇 서비스를 이용하려면 아래 버튼 중 하나를 선택하세요 👇🏻:

you-are-blocked-dialog = <b>사용자님 ❕;</b>
                        계정이 차단되어 더 이상 봇 서비스를 이용할 수 없습니다.

dont-spam-dialog = <b>천천히 하세요 ‼️ </b>
                    스팸으로 인해 <code>{ $block_duration }</code>초 동안 차단되었습니다.

<#-- Owner Panel -->
panel-dialog = <b>관리자 패널 🛠</b>

            다시 오신 것을 환영합니다, 주인님. 아래에서 작업을 선택하세요 👇:

toggle-bot-btn = 🔌| 봇 켜기/끄기
block-user-btn = 🚫| 사용자 차단
unblock-user-btn = ✅| 차단 해제
broadcast-btn = 📢| 전체 발송

bot-enabled-dialog = 봇이 이제 <b>온라인</b> 상태입니다 ✅
bot-disabled-dialog = 봇이 이제 <b>오프라인</b> 상태입니다 ⛔️

bot-status-dialog = <b>봇 상태 ⚙️</b>

            아래에서 봇 상태를 선택하세요. 현재 상태는 녹색으로 표시됩니다 👇:
bot-status-on-btn = 🟢 온라인
bot-status-off-btn = 🔴 오프라인
back-panel-btn = 🔙 패널로 돌아가기

ask-user-id-dialog = 대상 사용자의 <b>숫자 ID</b>를 보내세요 👇:
invalid-id-dialog = ⚠️ 잘못된 ID입니다. 유효한 숫자 ID를 보내세요.

broadcast-ask-dialog = 모든 사용자에게 발송할 메시지를 보내세요 👇:
broadcast-started-dialog = 📢 <b>{ $total }</b>명의 사용자에게 발송을 시작했습니다…
broadcast-report-dialog = ✅ 전체 발송 완료.

            • 성공: <b>{ $sent }</b>
            • 실패: <b>{ $failed }</b>
            • 합계: <b>{ $total }</b>

<#-- Access Gate -->
bot-off-dialog = <b>봇이 현재 오프라인입니다 ⛔️</b>

            나중에 다시 시도해 주세요.

owner-reply-dialog = 💌•  메시지가 <b>검토</b>되어 <b>답변</b>되었습니다.

                    📝- 답변 내용:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = 운영자님, 새 메시지가 도착했습니다;
                    <b>👤- 이름:</b><code> { $name } </code>
                    <b>🆔- 사용자 ID:</b><code> { $user_id } </code>
                    <b>🫆- 사용자명:</b><code> { $user_name } </code>
                    <b>📝- 메시지:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = 운영자님, 새 익명 메시지가 도착했습니다;
                    <b>📝- 메시지:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = 이 메시지에 대한 답장을 하나의 메시지(텍스트, 동영상, 음성 등)로 보내세요. 취소하려면 아래 버튼을 사용하세요.
reply-sent-dialog = 답장을 성공적으로 보냈습니다! ✅
user-blocked-dialog = 사용자를 차단했습니다 ✅
user-unblocked-dialog = 사용자 차단을 해제했습니다 ✅
reaction-sent-dialog = 반응을 추가했습니다 ✅
