<#-- Commands Discription -->
start-command-discription = הפעלה מחדש של הבוט
help-command-discription = הצגת העזרה
links-command-discription = הדפים שלי
language-command-discription = שינוי שפה


<#-- Commands Dialog -->
start-dialog = <b>שלום! 👋</b>

                אני עוזר לך ליצור קשר עם הבעלים גם <b>ישירות</b> וגם <b>באופן אנונימי</b>.

                כדי להתחיל, בחר אחד מהכפתורים שלמטה 👇:

help-dialog = <b>מדריך לבוט 🆘</b>

            • <b>הודעה ישירה</b> 💌: ההודעה שלך מגיעה לבעלים יחד עם הזהות שלך.
            • <b>הודעה אנונימית</b> 🥷: ההודעה שלך נשלחת מבלי לחשוף את זהותך.
            • ניתן לשלוח כל תוכן ( טקסט, תמונה, וידאו, קול וכו' ) כ<b>הודעה אחת</b>.
            • לאחר הבדיקה, תשובת הבעלים תישלח אליך באופן אוטומטי.

            ⚠️ עד שתקבל תשובה, אנא הימנע מ<b>חסימת</b> הבוט.

links-dialog = 💠 הדפים שלי ברשתות החברתיות:

language-dialog = <b>אנא בחר את השפה שלך 👇</b>
language-changed-dialog = השפה עודכנה ✅


<#-- Buttons Dialog -->
message-btn = הודעה ישירה |💌
anonymous-message-btn = 🥷| הודעה אנונימית
links-btn = 📟| הדפים שלי
help-btn = עזרה |🆘
language-btn = 💱 שינוי שפה 💱

cancel-btn = 🔙| ביטול
reply-btn = • להשיב למשתמש •
block-btn = 🚫| חסימת משתמש
unblock-btn = ☑️| ביטול חסימה



<#-- Messaging Flow -->
send-direct-dialog = <b>ברוך הבא 💛.</b>

                    באפשרותך לשלוח את ההודעה שלך כ<b>הודעה אחת</b> בכל פורמט ( <tg-spoiler>טקסט, תמונה, וידאו וכו'</tg-spoiler> ). שים לב שהזהות שלך תהיה <b>גלויה</b> לבעלים.

                    אנא הימנע מ<b>חסימת</b> הבוט לפני קבלת תשובה; כמו כן <b>נימוס</b> הוא הכרחי.

                    <b>שלח את ההודעה שלך 👇🏻:</b>

send-anon-dialog = <b>ברוך הבא 💛.</b>

                    באפשרותך לשלוח את ההודעה שלך כ<b>הודעה אחת</b> בכל פורמט ( <tg-spoiler>טקסט, תמונה, וידאו וכו'</tg-spoiler> ). שים לב שהזהות שלך <b>לא תהיה גלויה</b> לבעלים.

                    אנא הימנע מ<b>חסימת</b> הבוט לפני קבלת תשובה; כמו כן <b>נימוס</b> הוא הכרחי.

                    <b>שלח את ההודעה שלך 👇🏻:</b>

cancelled-dialog = הפעולה בוטלה וחזרנו לתפריט <b>הראשי</b>.

            כדי להמשיך, בחר אחד מהכפתורים שלמטה 👇:

message-delivered-dialog = ההודעה שלך התקבלה ונשלחה ✅;

                    אנא <b>התאזר בסבלנות</b> עד לקבלת התשובה הסופית ו<u>אל תחסום את הבוט</u>, שכן לאחר חסימתו <u>לא</u> תקבל את תשובתך.

                    כדי להשתמש בבוט, בחר אחד מהכפתורים שלמטה 👇🏻:

you-are-blocked-dialog = <b>משתמש יקר ❕;</b>
                        חשבונך נחסם ולא תוכל עוד להשתמש בשירותי הבוט.

owner-reply-dialog = 💌•  ההודעה שלך <b>נבדקה</b> וקיבלה <b>תשובה</b>.

                    📝- טקסט התשובה:
                    <blockquote expandable>{ $answer_text }</blockquote>

                    ➖➖➖➖➖➖
                    ⏰ <code>{ $time }</code>



<#-- Owner Inbox -->
inbox-direct-dialog = בעלים יקר, התקבלה עבורך הודעה חדשה;
                    <b>👤- שם:</b><code> { $name } </code>
                    <b>🆔- מזהה משתמש:</b><code> { $user_id } </code>
                    <b>🫆- שם משתמש:</b><code> { $user_name } </code>
                    <b>📝- הודעה:</b>
                    <blockquote expandable>{ $message }</blockquote>

inbox-anon-dialog = בעלים יקר, התקבלה עבורך הודעה אנונימית חדשה;
                    <b>📝- הודעה:</b>
                    <blockquote expandable>{ $message }</blockquote>

reply-dialog = שלח את תשובתך להודעה זו כהודעה אחת (טקסט, וידאו, קול וכו'). כדי לבטל, השתמש בכפתור שלמטה.
reply-sent-dialog = התשובה נשלחה בהצלחה! ✅
user-blocked-dialog = המשתמש נחסם ✅
user-unblocked-dialog = חסימת המשתמש בוטלה ✅
reaction-sent-dialog = התגובה נוספה ✅
