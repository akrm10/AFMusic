HELP_1 ="""<b><u>أوامر الادمن :</b></u>

فقط أضف <b> c </b> في بداية الأوامر لاستخدامها في القناة.


ـ وقف او /pause : إيقاف التشغيل الحالي.

ـ استئناف او /resume : استئناف التشغيل الذي تم إيقافه.

ـ تخطي او /skip : تخطي الحالي وبدء تشغيل التالي في القائمة.

ـ ايقاف او /end أو /stop : مسح القائمة وإنهاء التشغيل.

ـ /player : الحصول على لوحة تحكم تفاعلية.

ـ /الاغاني او /queue : عرض قائمة الاغاني المنتظرة.
"""

HELP_2 = """
<b><u>مستخدمون مصرح لهم :</b></u>

يمكن للمستخدمين المصرح لهم استخدام أوامر الادمن في البوت دون وجود صلاحيات الادمن في المحادثة.

ـ /auth [ الرد على المستخدم / معرف المستخدم ] : إضافة مستخدم إلى قائمة المصرح بهم في البوت.

ـ /unauth [ الرد على المستخدم / معرف المستخدم ] : إزالة مستخدم مصرح به من قائمة المصرح بهم.

ـ /authusers : عرض قائمة المستخدمين المصرح بهم في المجموعة.
"""

HELP_3 = """
<u><b>ميزة البث</b></u> [ فقط للمشرفين ] :

ـ /broadcast [ رسالة أو الرد على رسالة ] : بث رسالة إلى محادثات الخادم.

<u>أوضاع البث :</u>
<b>ـ pin</b> : تثبيت رسائل البث في محادثات الخادم.

<b>ـ pinloud</b> : تثبيت رسائل البث في محادثات الخادم وإرسال إشعار إلى الأعضاء.

<b>ـ user</b> : بث الرسالة للمستخدمين الذين بدأوا استخدام البوت.

<b>ـ assistant</b> : بث رسالتك من حساب المساعد الخاص بالبوت.

<b>ـ nobot</b> : يجبر البوت على عدم بث الرسالة.

<b>مثال:</b> <code> /broadcast -user -assistant -pin اختبار البث </code>
"""

HELP_4 = """<u><b>ميزة قائمة الحظر في المحادثات :</b></u> [فقط للمشرفين]

قيد المحادثات السيئة لاستخدام بوتنا.

ـ /blacklistchat [ معرف المحادثة ] : إضافة محادثة إلى قائمة الحظر من استخدام البوت.

ـ /whitelistchat [ معرف المحادثة ] : إزالة الحظر عن محادثة مضافة إلى قائمة الحظر.

ـ /blacklistedchat : عرض قائمة المحادثات المحظورة.
"""

HELP_5 = """
<u><b>حظر المستخدمين :</b></u> [ فقط للمشرفين ]

يبدأ تجاهل المستخدمين المحظورين حتى يتمكنوا من استخدام أوامر البوت.

ـ /block [ اسم المستخدم أو الرد على المستخدم ] : حظر المستخدم من استخدام بوتنا.

ـ /unblock [ اسم المستخدم أو الرد على المستخدم ] : إلغاء حظر المستخدم المحظور.

ـ /blockedusers : عرض قائمة المستخدمين المحظورين.
"""

HELP_6 = """
<u><b>أوامر تشغيل القناة :</b></u>

يمكنك بث الصوت / الفيديو في القناة.

ـ /cplay : يبدأ بث المسار الصوتي المطلوب في محادثة الفيديو الخاصة بالقناة.

ـ /cvplay : يبدأ بث مسار الفيديو المطلوب في محادثة الفيديو الخاصة بالقناة.

ـ /cplayforce أو /cvplayforce : يوقف التيار الحالي ويبدأ بث المسار المطلوب.

ـ /channelplay [ اسم المستخدم أو المعرف ] أو [تعطيل]: يوصل القناة بمجموعة ويبدأ بث المسارات بواسطة الأوامر المرسلة في المجموعة.
"""

HELP_7 = """
<u><b>ميزة الحظر العالمي :</b></u> [فقط للمشرفين]:

ـ /gban [ اسم المستخدم أو الرد على المستخدم ] : يحظر الشخص من جميع المحادثات الخاصة بالبوت ويضيفه إلى قائمة الحظر.

ـ /ungban [ اسم المستخدم أو الرد على المستخدم ] : يلغي الحظر العالمي للشخص.

ـ /gbannedusers : يعرض قائمة المستخدمين المحظورين عالمياً.
"""

HELP_8 = """
<b><u>تكرار التشغيل المستمر :</b></u>

<b>يبدأ بث المقطع الصوتي المستمر</b>

ـ /loop [ enable/disable ]: يفعل/يعطل التكرار للتشغيل الحالي.

ـ /loop [ 1، 2، 3، ... ] : يفعل التكرار للقيمة المحددة.
"""

HELP_9 = """
<u><b>وضع الصيانة :</b></u> [ فقط المطورين ] :

ـ /logs : يحصل على سجلات البوت.

ـ /logger [ enable/disable ] : يبدأ/يتوقف البوت عن تسجيل الأنشطة.

ـ /maintenance [ enable/disable ] : يقوم بتفعيل/تعطيل وضع الصيانة للبوت.
"""

HELP_10 = """
<b><u>الاستجابة والإحصائيات :</b></u>

ـ /start : يبدأ بوت الموسيقى.

ـ /help : يحصل على قائمة المساعدة مع شرح للأوامر.

ـ /ping : يظهر الاستجابة وإحصائيات النظام للبوت.

ـ /stats : يظهر الإحصائيات العامة للبوت.
"""

HELP_11 = """
<u><b>أوامر التشغيل :</b></u>

<b>ـ v :</b> يرمز لتشغيل الفيديو.

<b>ـ force :</b> يرمز للتشغيل القسري.

ـ /play أو /vplay : يبدأ بث الأغنية المطلوبة في محادثة الفيديو.

ـ /playforce أو /vplayforce : يتوقف عن التشغيل الحالي ويبدأ بث الأغنية المطلوبة.
"""

HELP_12 = """
<b><u>ترتيب عشوائي للقائمة :</b></u>

ـ /shuffle : يقوم بترتيب عشوائي للقائمة.

ـ /queue : يعرض القائمة المرتبة عشوائياً.
"""

HELP_13 = """
<b><u>تحديد موقع التشغيل :</b></u>

ـ /seek [ المدة بالثواني ] : يقوم بتحديد موقع التشغيل إلى المدة المعطاة.

ـ /seekback [ المدة بالثواني ] : يقوم بالتراجع إلى الوراء للمدة المعطاة.
"""

HELP_14 = """
<b><u>تحميل الأغنية :</b></u>

ـ بحث او /song [اسم الأغنية/رابط YouTube] : يقوم بتحميل أي مسار من يوتيوب بتنسيق MP3 أو MP4.
"""

HELP_15 = """
<b><u>أوامر السرعة :</b></u>

يمكنك التحكم في سرعة التشغيل للبث الحالي. [الادمن فقط]

ـ /speed or /playback : لضبط سرعة التشغيل الصوتي في المجموعة.

ـ /cspeed or /cplayback : لضبط سرعة التشغيل الصوتي في القناة.
"""
