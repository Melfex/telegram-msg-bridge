<#-- Commands Discription -->
start-command-discription = إعادة تشغيل البوت
help-command-discription = عرض المساعدة
links-command-discription = صفحاتي
language-command-discription = تغيير اللغة


<#-- Commands Dialog -->
start-dialog = <b>مرحبًا! 👋</b>

                أساعدك على التواصل مع المالك بطريقتين: <b>مباشرة</b> و<b>مجهولة</b>.

                للبدء، اختر أحد الأزرار في الأسفل 👇:

help-dialog = <b>دليل استخدام البوت 🆘</b>

            • <b>رسالة مباشرة</b> 💌: تصل رسالتك إلى المالك مع هويتك.
            • <b>رسالة مجهولة</b> 🥷: تُرسل رسالتك دون كشف هويتك.
            • يمكنك إرسال أي محتوى ( نص، صورة، فيديو، رسالة صوتية، إلخ. ) ضمن <b>رسالة واحدة</b>.
            • بعد المراجعة، يصلك رد المالك تلقائيًا.

            ⚠️ حتى تستلم ردًّا، يُرجى تجنّب <b>حظر</b> البوت.

links-dialog = 💠 صفحاتي على مواقع التواصل:

language-dialog = <b>الرجاء اختيار لغتك 👇</b>
language-changed-dialog = تم تحديث اللغة ✅


<#-- Buttons Dialog -->
message-btn = رسالة مباشرة |💌
anonymous-message-btn = 🥷| رسالة مجهولة
links-btn = 📟| صفحاتي
help-btn = المساعدة |🆘
language-btn = 💱 تغيير اللغة 💱

cancel-btn = 🔙| إلغاء
reply-btn = • الرد على المستخدم •
block-btn = 🚫| حظر المستخدم
unblock-btn = ☑️| إلغاء حظر المستخدم



<#-- Messaging Flow -->
send-direct-dialog = <b>أهلًا بك 💛.</b>

                    يمكنك إرسال رسالتك ضمن <b>رسالة واحدة</b> بأي صيغة ( <tg-spoiler>نص، صورة، فيديو، إلخ.</tg-spoiler> ). لاحظ أن هويتك ستكون <b>ظاهرة</b> للمالك.

                    يُرجى تجنّب <b>حظر</b> البوت قبل استلام ردّك؛ كما أن <b>حسن الأدب</b> أمر ضروري.

                    <b>أرسل رسالتك 👇🏻:</b>

send-anon-dialog = <b>أهلًا بك 💛.</b>

                    يمكنك إرسال رسالتك ضمن <b>رسالة واحدة</b> بأي صيغة ( <tg-spoiler>نص، صورة، فيديو، إلخ.</tg-spoiler> ). لاحظ أن هويتك <b>لن تكون ظاهرة</b> للمالك.

                    يُرجى تجنّب <b>حظر</b> البوت قبل استلام ردّك؛ كما أن <b>حسن الأدب</b> أمر ضروري.

                    <b>أرسل رسالتك 👇🏻:</b>

cancelled-dialog = تم إلغاء العملية والعودة إلى القائمة <b>الرئيسية</b>.

            للمتابعة، اختر أحد الأزرار في الأسفل 👇:

message-delivered-dialog = تم استلام رسالتك وإرسالها ✅؛

                    يُرجى <b>التحلّي بالصبر</b> حتى تستلم الرد النهائي و<u>تجنّب حظر البوت</u>، لأنك بعد حظره <u>لن</u> تستلم ردّك.

                    لاستخدام خدمات البوت، اختر أحد الأزرار في الأسفل 👇🏻:

you-are-blocked-dialog = <b>عزيزي المستخدم ❕؛</b>
                        تم حظر حسابك ولن تتمكن بعد الآن من استخدام خدمات البوت.

dont-spam-dialog = <b>تمهّل ‼️؛ </b>
                    تم حظرك لمدة <code>{ $block_duration }</code> ثانية بسبب الإزعاج (سبام).

owner-reply-dialog = 💌•  تمت <b>مراجعة</b> رسالتك و<b>الرد</b> عليها.

                    📝- نص الرد:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = عزيزي المالك، وصلتك رسالة جديدة؛
                    <b>👤- الاسم:</b><code> { $name } </code>
                    <b>🆔- المعرّف الرقمي:</b><code> { $user_id } </code>
                    <b>🫆- اسم المستخدم:</b><code> { $user_name } </code>
                    <b>📝- نص الرسالة:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = عزيزي المالك، وصلتك رسالة مجهولة جديدة؛
                    <b>📝- نص الرسالة:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = أرسل ردّك على هذه الرسالة ضمن رسالة واحدة (نص، فيديو، رسالة صوتية، إلخ.). إذا رغبت في الإلغاء فاستخدم الزر في الأسفل.
reply-sent-dialog = تم إرسال الرد بنجاح! ✅
user-blocked-dialog = تم حظر المستخدم ✅
user-unblocked-dialog = تم إلغاء حظر المستخدم ✅
reaction-sent-dialog = تم تسجيل التفاعل ✅
