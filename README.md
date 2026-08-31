# Online Shop CLI (Python)

مشروع نظام متجر إلكتروني بسيط شغال من الـ Terminal (CLI)، مبني بـ Python من غير أي Framework أو Database حقيقية — كل البيانات متخزنة في ملفات **JSON**.

المشروع مقسّم لـ 3 ملفات رئيسية:

| الملف | المسؤولية |
|---|---|
| `main.py` | تسجيل/دخول المستخدمين، عرض المنتجات، السلة، الـ Checkout |
| `admin.py` | تسجيل/دخول الأدمن، إضافة منتجات، إضافة خصومات |
| `Account_Credit.py` | نظام الكريديت كارد (إنشاء حساب، شحن رصيد) |

---

## 1. هيكل المشروع

```
project/
├── main.py
├── admin.py
├── Account_Credit.py
└── DataBase/
    ├── Users/
    │   ├── Users.json          # كل حسابات المستخدمين
    │   └── Session_user.json   # المستخدم اللي عامل login دلوقتي
    ├── Products/
    │   ├── List_product.json   # عربة التسوق (Cart)
    │   └── CheckOut.json       # سجل عمليات الشراء المكتملة
    ├── Admin/
    │   ├── Admin.json          # حسابات الأدمن
    │   ├── Products.json       # كتالوج المنتجات (اللي الأدمن ضايفه)
    │   └── Discount.json       # الخصومات المتاحة
    └── Credit/
        ├── Credit.json         # حسابات الكريديت كارد
        └── Session.json        # جلسة الكريديت كارد الحالية
```

---

## 2. ⚠️ ملحوظة مهمة قبل التشغيل

الكود **مش بيعمل الـ Folders دي تلقائي** — لازم تعملها بنفسك يدويًا قبل ما تشغّل `main.py`، وإلا هيديك Error إن المسار مش موجود.

اعمل الهيكل ده جنب الملفات (`main.py`, `admin.py`, `Account_Credit.py`):

```
DataBase/
├── Users/
├── Products/
├── Admin/
└── Credit/
```

يعني تعمل الأمر ده مرة واحدة في مجلد المشروع:

```bash
mkdir -p DataBase/Users DataBase/Products DataBase/Admin DataBase/Credit
```

**ملحوظة**: مش لازم تنشئ ملفات الـ `.json` نفسها (زي `Users.json`, `Session_user.json`... إلخ) — الكود بيعمل الملف تلقائي أول مرة يحاول يكتب فيها (لأن كل دالة `load_x()` بترجع `[]` لو الملف مش موجود). الفولدرات بس هي اللي لازم تتعمل يدوي.

---

## 3. تشغيل المشروع

```bash
python main.py
```

هيظهرلك المنيو الرئيسية:

```
1. Sigh in     → تسجيل حساب مستخدم جديد أو أدمن (InputUser)
2. Login       → تسجيل دخول بحساب مستخدم موجود
3. Show Menu OS → الدخول على منيو المتجر (منتجات / سلة / Checkout)
4. Credit Card  → نظام الكريديت كارد
0. Exit
```

---

## 4. تدفق الاستخدام (User Flow)

```
Sigh in (user) ──► Users.json (يتضاف حساب) ──► Session_user.json (يتسجل Token)
                                                        │
                                                        ▼
                            Show Menu OS ──► Products ──► List_product.json (Cart)
                                                        │
                                                        ▼
                                              Check Out ──► CheckOut.json
                                                        │
                                                        ▼
                                        (يخصم من) Credit/Session.json
```

للـ Checkout لازم يكون عندك:
1. حساب مستخدم مسجّل (`Users.json` + `Session_user.json`)
2. منتجات في السلة (`List_product.json`)
3. حساب كريديت كارد فيه رصيد كافي (`Credit/Session.json`)

---

## 5. ملاحظات ومعروف عنها إنها محدودة (Known Limitations)

- **Session واحدة بس في وقت واحد**: `Session_user.json` و `Credit/Session.json` بيتخزنوا كملف واحد (dict) مش list، يعني مفيش دعم لأكتر من مستخدم شغال بنفس الوقت.
- **الباسوردات متخزنة Plain Text** من غير أي تشفير (مقبول لمشروع تعليمي بس مش للإنتاج).
- **مفيش Error Handling** لو ملف الـ JSON فاضي أو فيه مفتاح ناقص.
- **الأدمن مش بيتحقق من الباسورد** وقت الـ Login، بيتحقق من الـ Username بس.

---

## 6. خريطة ربط ملفات الـ JSON

شوف قسم "خريطة العلاقات" اللي هبعتهولك جوه الشات كـ Diagram تفاعلي — بيوضح إزاي كل ملف بيتربط بالتاني عن طريق المفاتيح المشتركة زي `id` و `Token`.
