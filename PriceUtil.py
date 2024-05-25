import tkinter
import customtkinter
from jdatetime import datetime as jdatetime
from PIL import Image

Kits = ['انتقال کالا بين گروه ها', 'بدهكاران بر اساس تاريخ فاكتور فروش', 'بدهكاران هر روز ', 'تاريخ وصول چک هاي خرجي', 'تخفيف سطري', 'ترازوي ديجيتالي', 'توليد اتوماتيك بر اساس فرمول توليد', 'چند ارزي جدید', 'حراجي و تخفيفات پلکانی', 'خدمات برحسب درصدي ازمبلغ كل فاكتور', 'سرشكن هزينه درقيمت خريد', 'سرفصل آزاد', 'كيت درج كارمزد', 'گزارش ريز پرداختي هاي مشتريان', 'گزارش عملكرد كاربران', 'گزارشات آنلاين هلو 1 ماهه ', 'گزارشات آنلاين هلو 3 ماهه', 'گزارشات آنلاين هلو 6 ماهه', '...پرداخت به...دريافت از', '...مغايرت بانكي و', 'ادغام اسناد تجميعي', 'اقساط وگزارشات مربوطه', 'انتخاب سرفصل در فاكتور ضايعات', 'انتخاب عكس هر كالا', 'بسته شغلي پيامک', 'پرينت چك','پرينت حواله پخش', 'پرينت حواله و رسيد انباردر ثبت فاكتور', 'پورسانت درصدي از سود فروش + واسطه',   'پورسانت سطري', 'تاريخ ميلادي به جاي هجري شمسي', 'تبديل اسنادموقت به دائم وبرعكس', 'تجزيه', 'تسويه فاكتوربه فاكتور', 'توضيحات چند سطري هر سطر فاكتور ',  'توليد فرموله', 'تيپ قيمت', 'ثبت سنددرپيش فاكتور', 'ثبت سندمشابه وسندمعكوس', 'ثبت قيمت همكاران ومشتريان', 'ثبت كرايه مشتري درفاكتور', 'ثبت ليستي چكها', 'ثبت هزينه در فاكتور خريد و فروش', 'چاپ باركد', 'چك ضمانتي', 'حداقل و حداكثر مبلغ جهت هر كالا ', 'حواله بين انبار', 'خروجي متن', 'ادغام اسناد', 'خلاصه فاكتور ', 'دسته چك ', 'دو واحدي انبار', 'راس چك', 'راس فاكتور', 'سطح دسترسي', 'سفارش ليستي كالاهاو...وتبديل به فاكتور', 'اعشاری شناور', 'سود و ترازنامه بر اساس قيمت دلخواه هر كالا', 'ش دوم فاكتور/ سند', 'شماره سريال', 'طراحي فاكتور', 'فاكتور اشانتيون', 'فروش نقدي', 'في فروش برحسب درصدي ازفي خريد', 'کاربر اضافه سفارش گيري رستوران', 'کاربر اضافه سفارش گيري پخش', 'كاردكس ريالي كالا', 'كالر آيدي', 'گزارش عملكرد كالا', 'گزارش كالاهاي فروش نرفته', 'گزارشات تجميعي', 'ليست بدهكاران از تاريخ خاص ', 'ليست سياه', 'مركز هزينه- درآمد', 'معين اشخاص همراه باريز كالا', 'معين كالا ', 'منطقه بندي طرف حسابها', 'واسطه', 'هزينه حمل', '10 شركتي', '20 شرکتي', '30 شرکتي', 'کاربر اضافه شبکه هلو-پنل مشاغل', 'كاربر اضافه شبكه هلو',  'بارکدخوان آفلاین', 'Tag انبارگرداني', 'تعيين حداكثر مبلغ و تعداد  چك در هر ماه ', 'تنظيم ليست قيمتها', 'توضيحات پيش فرض', 'عدم ثبت سند و فاكتور / فقط پرينت فاكتور', 'عدم نمايش معين يك منطقه خاص', 'كنترل كدفروشنده زمان صدورفاكتور', 'گزارش فاكتور اشخاص']
modulesPrices = ['10,100,000', '3,600,000', '3,600,000', '3,600,000', '3,600,000', '4,600,000', '15,200,000', '57,600,000', '15,200,000', '3,600,000', '4,600,000', '10,100,000', '4,600,000', '5,100,000', '15,200,000', '1,600,000', '3,600,000', '8,100,000', '3,600,000', '4,600,000', '5,100,000', '8,600,000', '6,600,000', '3,600,000', '30,300,000', '3,600,000', '4,600,000', '4,600,000', '6,100,000', '7,100,000', '5,100,000', '3,600,000', '7,100,000', '5,100,000', '3,600,000', '10,100,000', '4,600,000', '3,600,000', '5,100,000', '4,600,000', '3,600,000', '3,600,000', '6,100,000', '5,100,000', '3,600,000', '3,600,000', '5,100,000', '6,100,000', '5,100,000', '7,100,000', '3,600,000', '4,600,000', '3,600,000', '3,600,000', '5,100,000', '3,600,000', '3,600,000', '5,100,000', '3,600,000', '3,600,000', '5,100,000', '3,600,000', '4,600,000', '7,100,000', '4,600,000', '13,200,000', '3,600,000', '4,600,000', '7,600,000', '3,600,000', '20,200,000', '3,600,000', '3,600,000', '4,600,000', '4,600,000', '3,600,000', '3,600,000', '8,100,000', '3,600,000', '50% قیمت', 'هر ۱۰ شرکت ۵۰٪ قیمت', 'هر ۱۰ شرکت ۵۰٪ قیمت', '10% قیمت', '10% قیمت', '15,200,000', '3,600,000', '3,600,000', '5,100,000', '3,600,000', '3,600,000', '7,100,000', '3,600,000', '3,600,000']
appCodes = {'': '', '11': 'فروشگاهی ساده', '12': 'فروشگاهی متوسط', '13': 'فروشگاهی پیشرفته', '15': 'فروشگاهی پیشرفته ۲ کاربره', '21': 'شرکتی ساده', '22': 'شرکتی متوسط', '23': 'شرکتی پیشرفته', '24': 'شرکتی ویژه', '25': 'شرکتی پیشرفته ۲ کاربره', '31': 'تولیدی ساده', '32': 'تولیدی متوسط', '33': 'تولیدی پیشرفته', '35': 'تولیدی پیشرفته ۲ کاربره', '41': 'جامع', '42': 'صنعتی', '44': 'شبکه', '81453': 'الکترونیک', '84955': 'رستوران و کترینگ', '84957': 'رستوران و کترینگ پيشرفته ', '84941': 'رستوران و کترینگ جامع', '84944': 'رستوران و کترینگ شبکه', '84055': 'طباخان', '84057': 'طباخان پیشرفته', '84041': 'طباخان جامع', '84044': 'طباخان شبکه', '82855': 'اغذیه فروشان و مواد غذایی', '82857': 'اغذیه فروشان و مواد غذایی پیشرفته', '82841': 'اغذیه فروشان و مواد غذایی جامع', '82844': 'اغذیه فروشان و مواد غذایی شبکه', '81111': 'نرم افزار مدیریت آرایشگاه', '81113': 'نرم افزار مدیریت آرایشگاه پیشرفته', '81133': 'نرم افزار مدیریت آرایشگاه حرفه ای', '81141': 'نرم افزار مدیریت آرایشگاه جامع', '81144': 'نرم افزار مدیریت آرایشگاه شبکه 44', '81211': 'نرم افزار عینک', '81213': 'نرم افزار عینک پیشرفته', '81241': 'نرم افزار عینک جامع', '81244': 'نرم افزار عینک شبکه', '81321': 'پخش ساده(فروش ندارد)', '81322': 'پخش متوسط (فروش ندارد)', '81323': 'پخش پیشرفته (فروش ندارد)', '81341': 'پخش جامع (فروش ندارد)', '81344': 'پخش شبکه (فروش ندارد)', '81346': 'مدیریت پخش', '81348': 'مدیریت پخش + GPS', '81347': 'مدیریت پخش (شبکه)', '81349': 'مدیریت پخش (شبکه) + GPS', '85012': 'فروش مانتو و پوشاک', '85033': 'فروش مانتو و پوشاک - پیشرفته', '85041': 'مانتو و پوشاک - جامع', '85044': 'مانتو و پوشاک - شبکه', '81812': 'سوپرمارکت', '81813': 'سوپرمارکت پیشرفته', '81841': 'سوپرمارکت جامع', '81844': 'سوپرمارکت شبکه', '81932': 'قنادی و آجیل فروشی', '81933': 'قنادی و آجیل فروشی پیشرفته', '81941': 'قنادی و آجیل فروشی جامع', '81944': 'قنادی و آجیل فروشی شبکه', '82012': 'لوازم یدکی', '82013': 'لوازم یدکی پیشرفته', '82041': 'لوازم یدکی جامع', '82044': 'لوازم یدکی شبکه', '82112': 'نرم افزار آرایشی و بهداشتی', '82113': 'لوازم آرایشی و بهداشتی پیشرفته', '82141': 'لوازم آرایشی و بهداشتی جامع', '82144': 'لوازم آرایشی و بهداشتی شبکه', '82212': 'فراورده های پروتئینی', '82241': 'فراورده های پروتئینی جامع', '82244': 'فراورده های پروتئینی شبکه', '82247': 'اتوماسیون تخصصی فراورده های پروتئینی', '83112': 'لوازم خانگی و صوتی تصویری', '83113': 'لوازم خانگی و صوتی تصویری پیشرفته', '83141': 'لوازم خانگی و صوتی تصویری جامع', '83144': 'لوازم خانگی و صوتی تصویری شبکه', '82412': 'بازرگانی پارچه و پرده', '82413': 'بازرگانی پارچه و پرده پیشرفته', '82441': 'بازرگانی پارچه و پرده جامع', '82444': 'بازرگانی پارچه و پرده شبکه', '82712': 'رنگ و ابزار فروشی', '82713': 'رنگ و ابزار فروشی - پبشرفته', '82741': 'رنگ و ابزار فروشی - جامع', '82744': 'رنگ و ابزار فروشی - شبکه', '20132': 'کامپیوتر، موبایل و ماشین های اداری', '20133': 'کامپیوتر، موبایل و ماشین های اداری - پیشرفته', '20141': 'کامپیوتر، موبایل و ماشین های اداری - جامع', '20144': 'کامپیوتر، موبایل و ماشین های اداری - شبکه', '82912': 'باطری فروشان', '82913': 'باطری فروشان پیشرفته', '82941': 'باطری فروشان جامع', '82944': 'باطری فروشان شبکه', '83012': 'فروشندگان کالای خواب', '83013': 'فروشندگان کالای خواب پیشرفته', '83041': 'فروشندگان کالای خواب جامع', '83044': 'فروشندگان کالای خواب شبکه', '83212': 'لوازم ایمنی و آتش نشانی', '83241': 'لوازم ایمنی و آتش نشانی جامع', '83244': 'لوازم ایمنی و آتش نشانی شبکه', '83311': 'فتوکپی و اوزالید', '83313': 'فتوکپی و اوزالید پیشرفته', '83341': 'فتوکپی و اوزالید جامع', '83344': 'فتوکپی و اوزالید شبکه', '83412': 'فروشندگان مواد شیمیایی', '83413': 'فروشندگان مواد شیمیایی پیشرفته', '83441': 'فروشندگان مواد شیمیایی جامع', '83444': 'فروشندگان مواد شیمیایی شبکه', '83611': 'لوازم پزشکی، آزمایشگاهی و دندانپزشکی', '83612': 'لوازم پزشکی، آزمایشگاهی و دندانپزشکی پیشرفته', '83613': 'لوازم پزشکی، آزمایشگاهی و دندانپزشکی حرفه ای', '83641': 'لوازم پزشکی، آزمایشگاهی و دندانپزشکی جامع', '83644': 'لوازم پزشکی، آزمایشگاهی و دندانپزشکی شبکه', '84112': 'فرش ماشینی و موکت', '84113': 'فرش ماشینی و موکت پیشرفته', '84141': 'فرش ماشینی و موکت جامع ', '84144': 'فرش ماشینی و موکت شبکه', '84212': 'فروشندگان لاستیک', '84241': 'فروشندگان لاستیک جامع', '84244': 'فروشندگان لاستیک شبکه', '20412': 'لوازم بهداشتی و مصالح ساختمانی', '20433': 'لوازم بهداشتی و مصالح ساختمانی - پیشرفته', '20441': 'لوازم بهداشتی و مصالح ساختمانی - جامع', '20444': 'لوازم بهداشتی و مصالح ساختمانی - شبکه', '84412': 'شوفاژ و تهویه مطبوع', '84413': 'شوفاژ و تهویه مطبوع پیشرفته', '84441': 'شوفاژ و تهویه مطبوع جامع', '84444': 'شوفاژ و تهویه مطبوع شبکه', '84512': 'فروشندگان ساعت', '84513': 'فروشندگان ساعت پیشرفته', '84541': 'فروشندگان ساعت جامع', '84544': 'فروشندگان ساعت شبکه', '84811': 'خرازی', '84813': 'خرازی پیشرفته', '84841': 'خرازی جامع', '84844': 'خرازی شبکه', '20032': 'خدمات پس از فروش', '20033': 'خدمات پس از فروش پیشرفته', '20041': 'خدمات پس از فروش جامع', '20044': 'خدمات پس از  فروش شبکه', '20512': 'آهن فروشی', '20533': 'آهن فروشی - پیشرفته', '20541': 'آهن فروشی جامع ', '20544': 'آهن فروشی شبکه ', '20612': 'کیف و کفش', '20633': 'کیف و کفش - پیشرفته', '20641': 'کیف و کفش - جامع ', '20644': 'کیف و کفش - شبکه', '20722': 'کارواش', '20741': 'کارواش - جامع', '20744': 'کارواش - شبکه ', '31065': 'طلا و جواهر', '31085': 'طلا و جواهر پیشرفته', '31087': 'طلافروشی جامع', '31089': 'طلا فروشی شبکه', '21212': 'کاشی و سرامیک', '21241': 'کاشی و سرامیک جامع', '21244': 'کاشی و سرامیک شبکه ', '21313': 'میوه و تره بار', '21341': 'میوه و تره بار - جامع', '21344': 'میوه و تره بار - شبکه ', '21712': 'سنگ بری و سنگ فروشی', '21733': 'سنگ بری و سنگ فروشی - پیشرفته', '21741': 'سنگ بری و سنگ فروشی - جامع', '21744': 'سنگ بری و سنگ فروشی - شبکه', '21831': 'شیشه بری', '21833': 'شیشه بری - پیشرفته', '21841': 'شیشه بری - جامع', '21844': 'شیشه بری - شبکه', '21912': 'لوازم التحریر و کمک آموزشی', '21933': 'لوازم التحریر و کمک آموزشی - پیشرفته', '21941': 'لوازم التحریر و کمک آموزشی - جامع', '21944': 'لوازم التحریر و کمک آموزشی - شبکه', '22012': 'اجاره کالا', '22033': 'اجاره کالا - پیشرفته', '22041': 'اجاره کالا - جامع', '22044': 'اجاره کالا - شبکه', '22223': 'صرافی', '22233': 'صرافی پیشرفته', '22241': 'صرافی جامع', '22244': 'صرافی شبکه', '22532': 'دباغی', '22533': 'دباغی - پیشرفته', '22541': 'دباغی - جامع', '22544': 'دباغی - شبکه', '85311': 'املاک ساده', '85312': 'املاک متوسط', '85313': 'املاک پیشرفته', '85341': 'املاک جامع', '85344': 'املاک شبکه', '85632': 'فروش چوب و MDF', '85633': 'فروش چوب و MDF پیشرفته', '85641': 'فروش چوب و MDF جامع', '85644': 'فروش چوب و MDF شبکه', '85723': 'نمایندگی بیمه', '85741': 'نمایندگی بیمه جامع', '85744': 'نمایندگی بیمه شبکه', '85841': 'ضایعات و اوراقی', '85844': 'ضایعات و اوراقی', '1366': 'فودکورت', '10175': 'شرکتهای بازرگانی', '10177': 'شرکتهای بازرگانی جامع', '10179': 'شرکتهای بازرگانی شبکه', '10285': 'شرکتهای تولیدی', '10287': 'شرکتهای تولیدی جامع', '10289': 'شرکتهای تولیدی شبکه', '10485': 'شرکت های پیمانکاری', '10487': 'شرکت های پیمانکاری جامع', '10489': 'شرکت های پیمانکاری شبکه', '86233': 'نرم افزار تخصصی کلینیک زیبایی - پایه', '86241': 'نرم افزار تخصصی کلینیک زیبایی - جامع', '86244': 'نرم افزار  تخصصی مدیریت مطب  شبکه', '86323': 'نرم افزار تخصصی مدیریت مطب پایه', '86341': 'نرم افزار  تخصصی مدیریت مطب جامع', '86141': 'پنل  تخصصی اماکن ورزشی - سینگل', '86144': 'پنل  تخصصی اماکن ورزشی - شبکه', '85431': 'پنل تخصصی اتو سرویس', '85432': 'پنل تخصصی اتو سرویس متوسط', '85433': 'پنل تخصصی اتو سرویس پیشرفته', '85441': 'پنل تخصصی اتو سرویس جامع', '85444': 'پنل تخصصی اتو سرویس شبکه', '86055': 'کافه رستوران', '86057': 'کافه رستوران پیشرفته', '86041': 'کافه رستوران جامع', '86044': 'کافه رستوران شبکه ', '86047': 'نرم افزار تخصصی کافه رستوران', '85932': 'نان و فرآورده های غلات ', '85933': 'نان و فرآورده های غلات پیشرفته', '85941': 'نان و فرآورده های غلات جامع', '85944': 'نان و فرآورده های غلات  شبکه', '85947': 'اتوماسیون تخصصی نان و فرآورده های غلات', '81947': 'اتوماسیون تخصصی قنادی و آجیل فروشی', '84947': 'اتوماسیون تخصصی رستوران اندروید'}
appPrices = {'': '', '11': '37800000', '12': '68100000', '13': '130800000', '15': '348200000', '21': '43600000', '22': '74700000', '23': '136200000', '24': '272500000', '25': '314900000', '31': '60600000', '32': '116100000', '33': '156400000', '35': '413800000', '41': '353200000', '42': '706400000', '44': '997500000', '81453': '121200000', '84955': '37400000', '84957': '121200000', '84941': '272500000', '84944': '605600000', '84055': '37400000', '84057': '121200000', '84041': '272500000', '84044': '605600000', '82855': '27300000', '82857': '83800000', '82841': '232200000', '82844': '545000000', '81111': '25300000', '81113': '72700000', '81133': '212000000', '81141': '454200000', '81144': '928500000', '81211': '25300000', '81213': '96900000', '81241': '272500000', '81244': '686300000', '81321': '70700000', '81322': '169600000', '81323': '343200000', '81341': '545000000', '81344': '1009200000', '81346': '302800000', '81348': '524800000', '81347': '726700000', '81349': '1816600000', '85012': '70700000', '85033': '145400000', '85041': '393600000', '85044': '726700000', '81812': '55600000', '81813': '129200000', '81841': '312900000', '81844': '605600000', '81932': '70700000', '81933': '177700000', '81941': '363400000', '81944': '756900000', '82012': '31300000', '82013': '97900000', '82041': '272500000', '82044': '605600000', '82112': '61600000', '82113': '133300000', '82141': '252300000', '82144': '585400000', '82212': '80800000', '82241': '323000000', '82244': '656000000', '82247': '989000000', '83112': '50500000', '83113': '145400000', '83141': '272500000', '83144': '605600000', '82412': '36400000', '82413': '126200000', '82441': '282600000', '82444': '605600000', '82712': '31300000', '82713': '116100000', '82741': '232200000', '82744': '454200000', '20132': '72700000', '20133': '185700000', '20141': '333100000', '20144': '676200000', '82912': '26300000', '82913': '118100000', '82941': '267500000', '82944': '555100000', '83012': '33400000', '83013': '113100000', '83041': '312900000', '83044': '585400000', '83212': '37400000', '83241': '262400000', '83244': '605600000', '83311': '32300000', '83313': '128200000', '83341': '282600000', '83344': '555100000', '83412': '56600000', '83413': '177700000', '83441': '434000000', '83444': '797300000', '83611': '30300000', '83612': '89900000', '83613': '201900000', '83641': '363400000', '83644': '1090000000', '84112': '45500000', '84113': '121200000', '84141': '312900000', '84144': '656000000', '84212': '106000000', '84241': '323000000', '84244': '706500000', '20412': '33400000', '20433': '137300000', '20441': '222100000', '20444': '605600000', '84412': '45500000', '84413': '161500000', '84441': '312900000', '84444': '605600000', '84512': '57600000', '84513': '177700000', '84541': '343200000', '84544': '686300000', '84811': '42400000', '84813': '105000000', '84841': '312900000', '84844': '686300000', '20032': '70700000', '20033': '201900000', '20041': '343200000', '20044': '656000000', '20512': '70700000', '20533': '212000000', '20541': '484500000', '20544': '1453300000', '20612': '30300000', '20633': '121200000', '20641': '201900000', '20644': '575300000', '20722': '64600000', '20741': '199900000', '20744': '464300000', '31065': '121200000', '31085': '343200000', '31087': '706500000', '31089': '1312000000', '21212': '52500000', '21241': '232200000', '21244': '524800000', '21313': '65600000', '21341': '190800000', '21344': '343200000', '21712': '45500000', '21733': '161500000', '21741': '312900000', '21744': '605600000', '21831': '42400000', '21833': '161500000', '21841': '312900000', '21844': '605600000', '21912': '47500000', '21933': '140300000', '21941': '272500000', '21944': '545000000', '22012': '32300000', '22033': '126200000', '22041': '302800000', '22044': '524800000', '22223': '121200000', '22233': '302800000', '22241': '484500000', '22244': '1160600000', '22532': '60600000', '22533': '212000000', '22541': '343200000', '22544': '656000000', '85311': '32300000', '85312': '153400000', '85313': '312900000', '85341': '434000000', '85344': '867900000', '85632': '65600000', '85633': '185700000', '85641': '292700000', '85644': '676200000', '85723': '80800000', '85741': '393600000', '85744': '827600000', '85841': '726700000', '85844': '1160600000', '1366': '989000000', '10175': '353300000', '10177': '1009200000', '10179': '1513800000', '10285': '524800000', '10287': '1130300000', '10289': '1766100000', '10485': '635800000', '10487': '1332200000', '10489': '1967900000', '86233': '252300000', '86241': '999100000', '86244': '968900000', '86323': '181700000', '86341': '555100000', '86141': '323000000', '86144': '797300000', '85431': '121200000', '85432': '252300000', '85433': '565200000', '85441': '867900000', '85444': '1312000000', '86055': '37400000', '86057': '121200000', '86041': '272500000', '86044': '605600000', '86047': '847800000', '85932': '70700000', '85933': '177700000', '85941': '363400000', '85944': '756900000', '85947': '1438100000', '81947': '1438100000', '84947': '847800000'}
tamdidPrices = {'11': '13250000', '12': '23800000', '13': '45700000', '15': '121500000', '21': '15250000', '22': '26100000', '23': '47500000', '24': '95200000', '25': '110000000', '31': '21200000', '32': '40500000', '33': '54700000', '35': '144800000', '41': '123500000', '42': '247000000', '44': '349000000', '81453': '42400000', '84955': '13200000', '84957': '42400000', '84941': '95900000', '84944': '215000000', '84055': '13200000', '84057': '42400000', '84041': '94900000', '84044': '215000000', '82855': '9600000', '82857': '29300000', '82841': '81800000', '82844': '190800000', '81111': '9100000', '81113': '25300000', '81133': '74200000', '81141': '158500000', '81144': '329000000', '81211': '9100000', '81213': '33900000', '81241': '95900000', '81244': '238200000', '81321': '25300000', '81322': '59600000', '81323': '120100000', '81341': '190800000', '81344': '357300000', '81346': '106000000', '81348': '183700000', '81347': '254400000', '81349': '635800000', '85012': '25300000', '85033': '51500000', '85041': '137300000', '85044': '254400000', '81812': '19200000', '81813': '45500000', '81841': '109000000', '81844': '215000000', '81932': '25300000', '81933': '62100000', '81941': '127200000', '81944': '264500000', '82012': '11200000', '82013': '34400000', '82041': '95900000', '82044': '215000000', '82112': '21200000', '82113': '46500000', '82141': '88400000', '82144': '199900000', '82212': '28300000', '82241': '113100000', '82244': '229100000', '82247': '346200000', '83112': '17700000', '83113': '51500000', '83141': '95900000', '83144': '215000000', '82412': '12700000', '82413': '43900000', '82441': '98900000', '82444': '215000000', '82712': '11200000', '82713': '40400000', '82741': '81800000', '82744': '158500000', '20132': '25300000', '20133': '64600000', '20141': '116100000', '20144': '236200000', '82912': '9100000', '82913': '40400000', '82941': '93900000', '82944': '193800000', '83012': '11700000', '83013': '39400000', '83041': '109000000', '83044': '199900000', '83212': '13200000', '83241': '91900000', '83244': '215000000', '83311': '11200000', '83313': '44500000', '83341': '98900000', '83344': '193800000', '83412': '19700000', '83413': '62100000', '83441': '153400000', '83444': '278600000', '83611': '10600000', '83612': '31300000', '83613': '70700000', '83641': '127200000', '83644': '381500000', '84112': '15900000', '84113': '42400000', '84141': '109000000', '84144': '229100000', '84212': '36900000', '84241': '113100000', '84244': '248300000', '20412': '11700000', '20433': '48000000', '20441': '77800000', '20444': '215000000', '84412': '15900000', '84413': '56600000', '84441': '109000000', '84444': '215000000', '84512': '19700000', '84513': '62100000', '84541': '120100000', '84544': '240200000', '84811': '14700000', '84813': '36900000', '84841': '109000000', '84844': '240200000', '20032': '25300000', '20033': '70700000', '20041': '120100000', '20044': '229100000', '20512': '25300000', '20533': '74200000', '20541': '169600000', '20544': '516700000', '20612': '10600000', '20633': '42400000', '20641': '70700000', '20644': '196800000', '20722': '22800000', '20741': '69700000', '20744': '162500000', '31065': '42400000', '31085': '120100000', '31087': '248300000', '31089': '464300000', '21212': '18200000', '21241': '81800000', '21244': '183700000', '21313': '22800000', '21341': '65600000', '21344': '120100000', '21712': '15900000', '21733': '56600000', '21741': '109000000', '21744': '215000000', '21831': '14700000', '21833': '56600000', '21841': '109000000', '21844': '215000000', '21912': '16700000', '21933': '49000000', '21941': '95900000', '21944': '190800000', '22012': '11200000', '22033': '43900000', '22041': '106000000', '22044': '183700000', '22223': '42400000', '22233': '106000000', '22241': '169600000', '22244': '415800000', '22532': '21200000', '22533': '74200000', '22541': '120100000', '22544': '229100000', '85311': '11200000', '85312': '53500000', '85313': '109000000', '85341': '153400000', '85344': '312900000', '85632': '22800000', '85633': '65600000', '85641': '98900000', '85644': '236200000', '85723': '28300000', '85741': '137300000', '85744': '289700000', '85841': '254400000', '85844': '401700000', '1366': '346200000', '10175': '123200000', '10177': '350200000', '10179': '529900000', '10285': '183700000', '10287': '395600000', '10289': '617700000', '10485': '225100000', '10487': '466300000', '10489': '691300000', '86233': '88400000', '86241': '349200000', '86244': '643900000', '86323': '63600000', '86341': '193800000', '86141': '113100000', '86144': '278600000', '85431': '42400000', '85432': '88400000', '85433': '197800000', '85441': '300800000', '85444': '459200000', '86055': '13200000', '86057': '42400000', '86041': '95900000', '86044': '212000000', '86047': '292700000', '85932': '25300000', '85933': '61600000', '85941': '127200000', '85944': '262400000', '85947': '494500000', '81947': '494500000', '84947': '292700000'}
networkCodes = ['25', '35', '44', '84944', '84044', '82844', '81144', '81244', '81344', '81349', '81347', '85044', '81844', '81944', '82044', '82144', '82244', '83144', '82444', '82744', '20144', '82944', '83044', '83244', '83344', '83444', '83644', '84144', '84244', '20444', '84444', '84544', '84844', '2044', '20544', '20644', '20744', '31089', '21244', '21344', '21744', '21844', '21944', '22044', '22244', '22544', '85344', '85644', '85744', '85844', '10179', '10289', '10489', '86244', '86144', '85444', '86044', '85944']
khadamatDict ={'ریموت برای 30 دقیقه': '4700000', 'نصب دورکاری': '57200000', 'نصب سینگل' : '3200000', 'نصب سرور': '8500000', 'نصب App': '3200000','نصب درایور': '3200000', 'نصب sql 2008': '3200000', 'نصب sql 2016': '4700000', 'نصب sql 2019': '920000', 'نصب ویندوز': '7500000', 'نصب یندوز سرور': '11000000', 'آموزش اولیه': '3200000', 'آموزش تخصصی': '8500000', 'مشاوره و آموزش': '9200000', 'تعویض سخت افزار': '3200000', 'بازگردانی بک آپ-هرشرکت': '1500000', 'بازگردانی بکآپ چندشزکتی': '4700000', 'طراحی فاکتور + فیش': '9200000', 'طراحی بارکد': '8200000', 'کارشناسی ساعتی': '8500000', 'کارشناس شبکه': '9200000', 'بستن حساب': '11000000', 'نصب مودیان': '4700000', 'آموزش مودیان': '9200000', 'ثبت نام کامل مودیان': '9200000', 'نصب توکن مودیان': '9200000', 'دریافت گواهی امضا': '5000000', 'ایاب ذهاب': '2000000', 'مشاوره بهرامی': '16000000', 'کشف رمز': '2000000', 'نصب دروید': '7500000', 'راه اندازی تبلت برای هر تبلت': '1000000', 'اول دوره کردن': '7500000'}
khadamat = [key for key in khadamatDict]
khadamatPrices = [value for value in khadamatDict.values()]

sanavat = ''
selectedModulePrice = {}
selectedBargashtiPrice = {}
selectedKhadamatPrice = {}
modulesCheckboxes = []
bargashtiCheckboxes = []
khadamatCheckBoxes = []
jameKolArray = set()
takhfifArray = set()


def change_appearance_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)


# about panel animation
class SlidePanel(customtkinter.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos + 0.01
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

def onModulesCheckBoxSelect(price):
    if price in selectedModulePrice:
        selectedModulePrice[price] += 1
    else:
        selectedModulePrice[price] = 1

def onKhadamatCheckBoxSelect(price):
    if price in selectedKhadamatPrice:
        selectedKhadamatPrice[price] += 1
    else:
        selectedKhadamatPrice[price] = 1

def calculate_modules_total_sum():
    total_modules_sum = 0
    for price, count in selectedModulePrice.items():
        price_without_commas = price.replace(',', '')

        try:
            total_modules_sum += count * int(price_without_commas)  # Accumulate the total sum
        except ValueError:
            print(f"Invalid price format: {price}. Skipping calculation.")
    return total_modules_sum

def calculate_khadamat_total_sum():
    total_khadamat_sum = 0
    for price, count in selectedKhadamatPrice.items():

        try:
            total_khadamat_sum += count * int(price)  # Accumulate the total sum
        except ValueError:
            print(f"Invalid price format: {price}. Skipping calculation.")
    return total_khadamat_sum

def onBargashtiCheckBoxSelect(price):
    if price in selectedBargashtiPrice:
        selectedBargashtiPrice[price] += 1
    else:
        selectedBargashtiPrice[price] = 1

def calculate_bargashti_total_sum():
    total_bargashti_sum = 0
    for price, count in selectedBargashtiPrice.items():
        # Remove commas from the price string before converting to an integer
        price_without_commas = price.replace(',', '')

        try:
            total_bargashti_sum += count * int(price_without_commas)  # Accumulate the total sum
        except ValueError:
            print(f"Invalid price format: {price}. Skipping calculation.")
    return total_bargashti_sum

def on_validate(P):
    if len(P) <= 8:
        return True
    else:
        return False

def resetSelectedModulesCheckboxes():
    for checkbox in modulesCheckboxes:
        checkbox.deselect()

def resetSelectedBargashtiCheckboxes():
    for checkbox in bargashtiCheckboxes:
        checkbox.deselect()

def resetSelectedKhadamatCheckboxes():
    for checkbox in khadamatCheckBoxes:
        checkbox.deselect()

def resetEntry():
    originCodeInput.delete(0, tkinter.END)
    destCodeInput.delete(0, tkinter.END)
    tamdidMotevaliInput.delete(0, tkinter.END)
    tamdidDateInput.delete(0, tkinter.END)
    karbarEzafeInput.delete(0, tkinter.END)
    tabdilBeGhoflCheckBox.deselect()
    chandSherkatiCheckBox.deselect()
    destChandSherkatiCheckBox.deselect()
    originChandSherkatiCheckBox.deselect()
    tamdidForKhadamatCheckBox.deselect()
    resetSelectedBargashtiCheckboxes()
    resetSelectedModulesCheckboxes()
    resetSelectedKhadamatCheckboxes()
    upgradeTakhfifInput.delete(0, tkinter.END)
    tamdidTakhfifInput.delete(0, tkinter.END)
    karbarEzafeTakhfifInput.delete(0, tkinter.END)
    chandSherkatiTakhfifInput.delete(0, tkinter.END)
    tabdilBeGhoflTakhfifInput.delete(0, tkinter.END)
    modulesTakhfifInput.delete(0, tkinter.END)
    bargashtiTakhfifInput.delete(0, tkinter.END)
    khadamatTakhfifPercent.delete(0, tkinter.END)
    khadamatTakhfifAmount.delete(0, tkinter.END)
    originCodeInput.configure(placeholder_text='کد محصول')
    destCodeInput.configure(placeholder_text='کد محصول')
    tamdidMotevaliInput.configure(placeholder_text='تعداد سال های متوالی تمدید')
    tamdidDateInput.configure(placeholder_text='تاریخ')
    karbarEzafeInput.configure(placeholder_text='تعداد کاربر')
    upgradeTakhfifInput.configure(placeholder_text='تخفیف')
    tamdidTakhfifInput.configure(placeholder_text='تخفیف')
    karbarEzafeTakhfifInput.configure(placeholder_text='تخفیف')
    chandSherkatiTakhfifInput.configure(placeholder_text='تخفیف')
    tabdilBeGhoflTakhfifInput.configure(placeholder_text='تخفیف')
    modulesTakhfifInput.configure(placeholder_text='تخفیف')
    bargashtiTakhfifInput.configure(placeholder_text='تخفیف')
    khadamatTakhfifPercent.configure(placeholder_text='تخفیف درصدی')
    khadamatTakhfifAmount.configure(placeholder_text='تخفیف مبلغی')

def resetLabel():
    upgradePriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    upgradePriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    tamdidMotevaliPriceAfter.configure(text='0', text_color='#ffffff')
    tamdidMotevaliPriceBefore.configure(text='0', text_color='#ffffff')
    tamdidTashvighiPriceAfterLabel.configure(text='0', text_color='#ffffff')
    tamdidTashvighiPriceBeforeLabel.configure(text='0', text_color='#ffffff')
    karbarEzafePriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    karbarEzafePriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    tabdilBeGhoflPriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    tabdilBeGhoflPriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    chandSherkatiPriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    chandSherkatiPriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    modulesPriceAfter.configure(text='0', text_color='#ffffff')
    modulesPriceBefore.configure(text='0', text_color='#ffffff')
    bargashtiPriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    bargashtiPriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    takhfifPrice.configure(text='0', text_color='#ffffff')
    jameKolPriceAfter.configure(text='0', text_color=('#084175', '#ffffff'))
    jameKolPriceBefore.configure(text='0', text_color=('#084175', '#ffffff'))
    originOutput.configure(text='', text_color=('#084175', '#ffffff'))
    destOutput.configure(text='', text_color=('#084175', '#ffffff'))
    tamdidPriceAfterLabel.configure(text='0', text_color='#ffffff')
    tamdidPriceBeforeLabel.configure(text='0', text_color='#ffffff')
    sanavatLabel.configure(text='', text_color='#ffffff')
    khadamatPriceLabel.configure(text='0', text_color='#ffffff')


def reset():
    selectedModulePrice.clear()
    selectedBargashtiPrice.clear()
    selectedKhadamatPrice.clear()
    resetEntry()
    resetLabel()

def calculateUpgrade(destChandSherkatiCheckBoxValue, originChandSherkatiCheckBoxValue, destCodePrice, originCodePrice, upgradeTakhfifInputData, jamekolCheckBoxValue):
    if destChandSherkatiCheckBoxValue == 'destChandSherkati':
        destCodePrice = int(destCodePrice) + (int(destCodePrice) / 2)
    if originChandSherkatiCheckBoxValue == 'originChandSherkati':
        originCodePrice = int(originCodePrice) + (int(originCodePrice) / 2)

    upgradeDifference = int(destCodePrice) - int(originCodePrice)

    if upgradeTakhfifInputData:
        upgradeTakhfif = int(upgradeTakhfifInputData)
        if upgradeTakhfif > 0:
            upgradeDifference = upgradeDifference - ((upgradeDifference * int(upgradeTakhfif)) / 100)
        upgradeTakhfifAmount = ((upgradeDifference * int(upgradeTakhfif)) / 100)
        if upgradeTakhfifAmount not in takhfifArray:
            takhfifArray.add(int(upgradeTakhfifAmount))

    formattedUpagradeDifferenceAfter = "{:,}".format(int(upgradeDifference))
    formattedUpagradeDifferenceBefore = "{:,}".format(int(upgradeDifference) - int(((upgradeDifference * 10) / 100)))
    upgradePriceAfter.configure(text=formattedUpagradeDifferenceAfter)
    upgradePriceBefore.configure(text=formattedUpagradeDifferenceBefore)
    if jamekolCheckBoxValue == 'jamekol':
        if upgradeDifference not in jameKolArray:
            jameKolArray.add(int(destCodePrice))
    if jamekolCheckBoxValue == 0:
        try:
            jameKolArray.remove(upgradeDifference)
        except:
            print('jmekol tik nadare')

def calculateTamdid(destCodeInputData, jalali_date_str, tamdidMotevaliInputData, tamdidTakhfifInputData):
    if destCodeInputData in appCodes and jalali_date_str:
        tamdidAdiPrice = int(tamdidPrices[destCodeInputData])
        if tamdidAdiPrice not in jameKolArray:
            jameKolArray.add(int(tamdidAdiPrice))
        if tamdidMotevaliInputData and tamdidMotevaliInputData.isdigit():
            if int(tamdidMotevaliInputData) == 2:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 25) / 100)
            elif 2 < int(tamdidMotevaliInputData) <= 3:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 30) / 100)
            elif 3 < int(tamdidMotevaliInputData) <= 4:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 35) / 100)
            elif 4 < int(tamdidMotevaliInputData) <= 5:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 40) / 100)
            elif 5 < int(tamdidMotevaliInputData) <= 6:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 45) / 100)
            elif int(tamdidMotevaliInputData) > 7:
                motevaliPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 50) / 100)

            # if tamdidTakhfifInputData:
            #     tamdidTakhfif = int(tamdidTakhfifInputData)
            #     if tamdidTakhfif > 0:
            #         motevaliPrice = motevaliPrice - ((motevaliPrice * int(tamdidTakhfif)) / 100)
            formattedtamdidMotevaliPrice = "{:,}".format(int(motevaliPrice))
            formattedtamdidMotevaliPriceBefore = "{:,}".format(int(motevaliPrice) - (int(int(motevaliPrice) * 10) / 100))
            tamdidMotevaliPriceAfter.configure(text=formattedtamdidMotevaliPrice)
            tamdidMotevaliPriceBefore.configure(text=formattedtamdidMotevaliPriceBefore)
            if motevaliPrice not in jameKolArray:
                jameKolArray.add(int(motevaliPrice))


        tashvighiPrice = int(tamdidAdiPrice) - ((int(tamdidAdiPrice) * 20) / 100)
        tashvighiPriceBefore = tashvighiPrice - ((int(tashvighiPrice) * 10) / 100)
        formattedTashvighiPrice = "{:,}".format(int(tashvighiPriceBefore))
        formattedTashvighiPriceAfter = "{:,}".format(int(tashvighiPrice))
        if tashvighiPrice not in jameKolArray:
            jameKolArray.add(int(tashvighiPrice))
        day_difference = None
        tamdidPrice = tamdidAdiPrice

        try:
            jalali_day, jalali_month, jalali_year = map(int, [jalali_date_str[:2], jalali_date_str[2:4],
                                                              jalali_date_str[4:]])
            jalali_date = jdatetime(jalali_year, jalali_month, jalali_day).togregorian()
            current_date = jdatetime.now().togregorian()
            date_difference = current_date - jalali_date
            day_difference = date_difference.days
        except (ValueError, IndexError) as e:
            tamdidTashvighiPriceAfterLabel.configure(text="تاریخ نامعتبر", text_color='red')
            tamdidTashvighiPriceBeforeLabel.configure(text='تاریخ نامعتبر', text_color='red')
            tamdidPriceBeforeLabel.configure(text="تاریخ نامعتبر", text_color='red')
            tamdidPriceAfterLabel.configure(text='تاریخ نامعتبر', text_color='red')
        if day_difference is not None:
            if day_difference <= 365:
                tamdidPrice = tamdidAdiPrice
                sanavat = 'بدون سنوات'
            elif 545 >= day_difference > 365:
                tamdidPrice = tamdidAdiPrice + ((int(tamdidAdiPrice) * 10) / 100)
                sanavat = 'بین ۳ تا ۶ ماه'
            elif 730 >= day_difference > 545:
                tamdidPrice = tamdidAdiPrice + ((int(tamdidAdiPrice) * 20) / 100)
                sanavat = 'بین ۶ تا ۱۲ ماه'
            elif 905 >= day_difference > 730:
                tamdidPrice = tamdidAdiPrice + ((int(tamdidAdiPrice) * 30) / 100)
                sanavat = 'بین ۱۲ تا ۱۸ ماه'
            elif 1095 >= day_difference > 905:
                tamdidPrice = tamdidAdiPrice + ((int(tamdidAdiPrice) * 40) / 100)
                sanavat = 'بین ۱۸ تا ۲۴ ماه'
            elif day_difference > 1095:
                tamdidPrice = tamdidAdiPrice + ((int(tamdidAdiPrice) * 50) / 100)
                sanavat = 'بالای ۲ سال'

            if tamdidTakhfifInputData:
                tamdidTakhfif = int(tamdidTakhfifInputData)
                if tamdidTakhfif > 0:
                    tamdidPrice = tamdidPrice - ((tamdidPrice * int(tamdidTakhfif)) / 100)
                tamdidTakhfifAmount = ((tamdidPrice * int(tamdidTakhfif)) / 100)
                if tamdidTakhfifAmount not in takhfifArray:
                    takhfifArray.add(int(tamdidTakhfifAmount))

            tamdidPriceBefore = tamdidPrice - ((int(tamdidPrice) * 10) / 100)
            formattedTamdidPrice = "{:,}".format(int(tamdidPriceBefore))
            formattedTamdidPriceAfter = "{:,}".format(int(tamdidPrice))
            tamdidTashvighiPriceAfterLabel.configure(text=formattedTashvighiPriceAfter)
            tamdidTashvighiPriceBeforeLabel.configure(text=formattedTashvighiPrice)
            tamdidPriceBeforeLabel.configure(text=formattedTamdidPrice)
            tamdidPriceAfterLabel.configure(text=formattedTamdidPriceAfter)
            sanavatLabel.configure(text=sanavat, text_color=('#084175', '#ffffff'))

def calculateKarbarEzafe(destCodeInputData, karbarEzafeInputData, destCodePrice, karbarEzafeTakhfifInputData):
    if destCodeInputData in networkCodes:
        karbarEzafeInput.configure(fg_color='#ffffff', text_color='black')
        karbarEzafePrice = int(destCodePrice) + (int(destCodePrice) * (int(karbarEzafeInputData) * 10) / 100)
        if karbarEzafeTakhfifInputData:
            karabarEzafeTakhfif = int(karbarEzafeTakhfifInputData)
            if karabarEzafeTakhfif > 0:
                karbarEzafePrice = karbarEzafePrice - ((karbarEzafePrice * int(karabarEzafeTakhfif)) / 100)
            karabarEzafeTakhfifAmount = ((karbarEzafePrice * int(karabarEzafeTakhfif)) / 100)
            if karabarEzafeTakhfifAmount not in takhfifArray:
                takhfifArray.add(int(karabarEzafeTakhfifAmount))
        if karbarEzafePrice not in jameKolArray:
            jameKolArray.add(int(karbarEzafePrice))

        karbarEzafeBefore = karbarEzafePrice - ((int(karbarEzafePrice) * 10) / 100)
        formattedKarbarEzafeBefore = "{:,}".format(int(karbarEzafeBefore))
        formattedKarbarEzafePrice = "{:,}".format(int(karbarEzafePrice))
        karbarEzafePriceAfter.configure(text=formattedKarbarEzafePrice)
        karbarEzafePriceBefore.configure(text=formattedKarbarEzafeBefore)
    else:
        karbarEzafePriceAfter.configure(text='کد غیر شبکه', text_color='#f63051')
        karbarEzafePriceBefore.configure(text='کد غیر شبکه', text_color='#f63051')
        karbarEzafeInput.configure(fg_color='#f63051', text_color='#ffffff')


def calculate():
    resetLabel()
    try:
        originCodeInputData = originCodeInput.get()
        destCodeInputData = destCodeInput.get()
        destChandSherkatiCheckBoxValue = destChandSherkatiCheckBox.get()
        originChandSherkatiCheckBoxValue = originChandSherkatiCheckBox.get()
        tamdidMotevaliInputData = tamdidMotevaliInput.get()
        jalali_date_str = tamdidDateInput.get().strip()
        destCodePrice = appPrices[destCodeInputData]
        originCodePrice = appPrices[originCodeInputData]
        karbarEzafeInputData = karbarEzafeInput.get()
        tabdilBeGhoflCheckBoxValue = tabdilBeGhoflCheckBox.get()
        chandSherkatiCheckBoxValue = chandSherkatiCheckBox.get()
        upgradeTakhfifInputData = upgradeTakhfifInput.get()
        tamdidTakhfifInputData = tamdidTakhfifInput.get()
        karbarEzafeTakhfifInputData = karbarEzafeTakhfifInput.get()
        tabdilBeGhoflTakhfifInputData = tabdilBeGhoflTakhfifInput.get()
        chandSherkatiTakhfifInputData = chandSherkatiTakhfifInput.get()
        modulesTakhfifInputData = modulesTakhfifInput.get()
        bargashtiTakhfifInputData = bargashtiTakhfifInput.get()
        khadamatTakhfifPercentData = khadamatTakhfifPercent.get()
        khadamatTakhfifAmountData = khadamatTakhfifAmount.get()
        tamdidForKhadamatValue = tamdidForKhadamatCheckBox.get()
        jamekolCheckBoxValue = jamekolCheckBox.get()
    except:
        reset()

    if originCodeInputData in appCodes and destCodeInputData in appCodes:
        originCodeInput.configure(fg_color='#ffffff', text_color='black')
        destCodeInput.configure(fg_color='#ffffff', text_color='black')
        originOutput.configure(text=appCodes[originCodeInputData])
        destOutput.configure(text=appCodes[destCodeInputData])

        if upgradeTakhfifInputData:
            destTakhfif = int(upgradeTakhfifInputData)
            if destTakhfif > 0:
                destCodePrice = int(destCodePrice) - ((int(destCodePrice) * int(destTakhfif)) / 100)
            destTakhfifAmount = ((int(destCodePrice) * int(destTakhfif)) / 100)
            if destTakhfifAmount not in takhfifArray:
                takhfifArray.add(int(destTakhfifAmount))

        if originCodeInputData == '' and destCodePrice:
            if destChandSherkatiCheckBoxValue == 'destChandSherkati':
                destCodePrice = int(destCodePrice) + (int(destCodePrice) / 2)
            destCodePriceBefore = int(destCodePrice) - ((int(destCodePrice) * 10) / 100)
            formattedDestCodePrice = "{:,}".format(int(destCodePrice))
            formattedDestCodePriceBefore = "{:,}".format(destCodePriceBefore)
            upgradePriceBefore.configure(text=formattedDestCodePriceBefore)
            upgradePriceAfter.configure(text=formattedDestCodePrice)
            if jamekolCheckBoxValue == 'jamekol':
                if destCodePrice not in jameKolArray:
                    jameKolArray.add(int(destCodePrice))
            if jamekolCheckBoxValue == 0:
                try:
                    jameKolArray.remove(destCodePrice)
                except:
                    print('jmekol tik nadare')

            calculateTamdid(destCodeInputData, jalali_date_str, tamdidMotevaliInputData, tamdidTakhfifInputData)

            if tabdilBeGhoflCheckBoxValue == 495000:
                tabdilBeGhofl = 4950000
                if tabdilBeGhoflTakhfifInputData:
                    tabdilBeGhoflTakhfif = int(tabdilBeGhoflTakhfifInputData)
                    if tabdilBeGhoflTakhfif > 0:
                        tabdilBeGhofl = tabdilBeGhofl - ((tabdilBeGhofl * int(tabdilBeGhoflTakhfif)) / 100)
                    tabdilBeGhoflTakhfifAmount = ((tabdilBeGhofl * int(tabdilBeGhoflTakhfif)) / 100)
                    if tabdilBeGhoflTakhfifAmount not in takhfifArray:
                        takhfifArray.add(int(tabdilBeGhoflTakhfifAmount))

                formattedTabdilBeGhofl = "{:,}".format(int(tabdilBeGhofl))
                tabdilBeGhoflBefore = int(tabdilBeGhofl) - ((int(tabdilBeGhofl) * 10) / 100)
                formattedTabdilBeGhoflBefore = "{:,}".format(int(tabdilBeGhoflBefore))
                tabdilBeGhoflPriceAfter.configure(text=formattedTabdilBeGhofl)
                tabdilBeGhoflPriceBefore.configure(text=formattedTabdilBeGhoflBefore)
                if tabdilBeGhofl not in jameKolArray:
                    jameKolArray.add(int(tabdilBeGhofl))

            if chandSherkatiCheckBoxValue == 'chandsherkati':
                chandSherkatiPrice = ((int(destCodePrice) * 50) / 100)
                if chandSherkatiTakhfifInputData:
                    chandSherkatiTakhfif = int(chandSherkatiTakhfifInputData)
                    if chandSherkatiTakhfif > 0:
                        chandSherkatiPrice = chandSherkatiPrice - ((chandSherkatiPrice * int(chandSherkatiTakhfif)) / 100)
                    chandSherkatiTakhfifAmount = ((chandSherkatiPrice * int(chandSherkatiTakhfif)) / 100)
                    if chandSherkatiTakhfifAmount not in takhfifArray:
                        takhfifArray.add(int(chandSherkatiTakhfifAmount))

                chandSherkatiBefore = int(chandSherkatiPrice) - ((int(chandSherkatiPrice) * 10) / 100)
                formattedChandSherkatiAfter = "{:,}".format(int(chandSherkatiPrice))
                formattedChandSherkatiBefore = "{:,}".format(int(chandSherkatiBefore))
                chandSherkatiPriceAfter.configure(text=formattedChandSherkatiAfter)
                chandSherkatiPriceBefore.configure(text=formattedChandSherkatiBefore)
                if chandSherkatiPrice not in jameKolArray:
                    jameKolArray.add(int(chandSherkatiPrice))
        else:
            if (originCodeInputData) and (destCodeInputData):
                calculateUpgrade(destChandSherkatiCheckBoxValue, originChandSherkatiCheckBoxValue, destCodePrice, originCodePrice, upgradeTakhfifInputData, jamekolCheckBoxValue)

        if karbarEzafeInputData:
            calculateKarbarEzafe(destCodeInputData, karbarEzafeInputData, destCodePrice, karbarEzafeTakhfifInputData)
    else:
        originOutput.configure(text='کد نامعتبر', text_color='red')
        upgradePriceAfter.configure(text='کد نامعتبر', text_color='red')
        upgradePriceBefore.configure(text='کد نامعتبر', text_color='red')
        originCodeInput.configure(fg_color='#f63051', text_color='#ffffff')
        destCodeInput.configure(fg_color='#f63051', text_color='#ffffff')


    bargashtiPriceTotalSum = calculate_bargashti_total_sum()
    if bargashtiPriceTotalSum:
        if bargashtiTakhfifInputData:
            bargashtiTakhfif = int(bargashtiTakhfifInputData)
            if bargashtiTakhfif > 0:
                bargashtiPriceTotalSum = int(bargashtiPriceTotalSum) - ((int(bargashtiPriceTotalSum) * int(bargashtiTakhfif)) / 100)
            bargashtiTakhfifAmount = ((int(bargashtiPriceTotalSum) * int(bargashtiTakhfif)) / 100)
            if bargashtiTakhfifAmount not in takhfifArray:
                takhfifArray.add(int(bargashtiTakhfifAmount))

    formattedBargashtiAfter = "{:,}".format(int(bargashtiPriceTotalSum))
    bargashtiPriceAfter.configure(text=str(formattedBargashtiAfter))
    bargashtiPriceCalculatedtBefore = bargashtiPriceTotalSum - ((bargashtiPriceTotalSum * 10) / 100)
    formattedBargashtiAfter = "{:,}".format(int(bargashtiPriceCalculatedtBefore))
    bargashtiPriceBefore.configure(text=str(formattedBargashtiAfter))
    if bargashtiPriceTotalSum not in jameKolArray:
        jameKolArray.add(int(bargashtiPriceTotalSum))

    modulesTotalSum = calculate_modules_total_sum()
    if modulesTakhfifInputData:
        moduleTakhfif = int(modulesTakhfifInputData)
        if moduleTakhfif > 0:
            modulesTotalSum = int(modulesTotalSum) - ((int(modulesTotalSum) * int(moduleTakhfif)) / 100)
        moduleTakhfifAmount = ((int(modulesTotalSum) * int(moduleTakhfif)) / 100)
        if moduleTakhfifAmount not in takhfifArray:
            takhfifArray.add(int(moduleTakhfifAmount))

    formattedModuleAfter = "{:,}".format(int(modulesTotalSum))
    modulesPriceAfter.configure(text=str(formattedModuleAfter))
    modulePriceCalculatedBefore = modulesTotalSum - ((modulesTotalSum * 10) / 100)
    formattedModuleBefore = "{:,}".format(int(modulePriceCalculatedBefore))
    modulesPriceBefore.configure(text=str(formattedModuleBefore))
    if modulesTotalSum not in jameKolArray:
        jameKolArray.add(int(modulesTotalSum))

    khadamatTotalSum = calculate_khadamat_total_sum()
    if tamdidForKhadamatValue == 35:
        khadamatTotalSum = int(khadamatTotalSum) + ((int(khadamatTotalSum) * int(tamdidForKhadamatValue)) / 100)
    if khadamatTakhfifPercentData and khadamatTakhfifAmountData:
        khadamatTakhfifPercent.configure(fg_color='#f63051', text_color='#ffffff')
        khadamatTakhfifAmount.configure(fg_color='#f63051', text_color='#ffffff')
        return

    if khadamatTakhfifPercentData or khadamatTakhfifAmountData:

        if khadamatTakhfifAmountData: khadamatTakhfifPercentData = 0
        if khadamatTakhfifPercentData: khadamatTakhfifAmountData = 0

        khedmatTakhfifPercent = int(khadamatTakhfifPercentData)
        khedmatTakhfifAmount = int(khadamatTakhfifAmountData)

        if not khedmatTakhfifAmount and khedmatTakhfifPercent > 0:
            khedmatTakhfif = ((int(khadamatTotalSum) * int(khedmatTakhfifPercent)) / 100)
            khadamatTotalSum = int(khadamatTotalSum) - ((int(khadamatTotalSum) * int(khedmatTakhfifPercent)) / 100)
            khadamatTakhfifPercent.configure(fg_color='white')
            khadamatTakhfifAmount.configure(fg_color='white')

        elif not khedmatTakhfifPercent and khedmatTakhfifAmount > 0:
            khadamatTotalSum = int(khadamatTotalSum) - khedmatTakhfifAmount
            khedmatTakhfif = khedmatTakhfifAmount
            khadamatTakhfifPercent.configure(fg_color='white')
            khadamatTakhfifAmount.configure(fg_color='white')

        if khedmatTakhfif not in takhfifArray:
            takhfifArray.add(int(khedmatTakhfif))

    formattedKhadamatPrice = "{:,}".format(int(khadamatTotalSum))
    khadamatPriceLabel.configure(text=formattedKhadamatPrice)

    if khadamatTotalSum not in jameKolArray:
        jameKolArray.add(int(khadamatTotalSum))
    else:
        formattedKhadamatPrice = "{:,}".format(int(khadamatTotalSum))
        khadamatPriceLabel.configure(text=formattedKhadamatPrice)
        if khadamatTotalSum not in jameKolArray:
            jameKolArray.add(int(khadamatTotalSum))

    jameKolList = list(jameKolArray)
    jameKolAfter = sum(jameKolList)
    jameKolBefore = jameKolAfter - ((jameKolAfter * 10) / 100)
    formattedJameKolPriceBefore = "{:,}".format(int(jameKolBefore))
    formattedJameKolPriceAfter = "{:,}".format(int(jameKolAfter))
    jameKolPriceBefore.configure(text=formattedJameKolPriceBefore)
    jameKolPriceAfter.configure(text=formattedJameKolPriceAfter)


    jameTakhfifList = list(takhfifArray)
    jameTakhfif = sum(jameTakhfifList)
    formattedJameTakhfif = "{:,}".format(int(jameTakhfif))
    takhfifPrice.configure(text=formattedJameTakhfif)


app = customtkinter.CTk()
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
app.title('SSP Price Utility')
app.geometry('3000 x 3000')
app.resizable(True, True)


# Main App
mainApp = customtkinter.CTkFrame(app, fg_color=('#ffffff', '#000d1f'))
mainApp.grid(row=0, column=0, padx=(10, 10), pady=(5, 5), sticky='s')

leftFrame = customtkinter.CTkFrame(mainApp, fg_color=('#d9e7fa', '#081930'))
leftFrame.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky='e')

middleFrame = customtkinter.CTkFrame(mainApp, fg_color=('#d9e7fa', '#081930'))
middleFrame.grid(row=0, column=1, padx=(5, 5), pady=(5, 5), sticky='n')

betweenRightAndMiddleFrame = customtkinter.CTkFrame(mainApp, fg_color=('#d9e7fa', '#081930'))
betweenRightAndMiddleFrame.grid(row=0, column=2, padx=(5, 5), pady=(5, 5), sticky='s')

rightFrame = customtkinter.CTkFrame(mainApp, fg_color=('#d9e7fa', '#081930'))
rightFrame.grid(row=0, column=3, padx=(5, 5), pady=(5, 5), sticky='w')

# Upgrade Section
upgradeSectionFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#93bcf5', '#1d4070'))
upgradeSectionFrame.grid(row=0, column=0, padx=(10, 10), pady=(5, 5))

destCodeInput = customtkinter.CTkEntry(upgradeSectionFrame, placeholder_text="کد محصول", width=175, height=35)
destCodeInput.grid(row=1, column=0, padx=(10, 10), pady=(3, 5))
destCodeInputLabel = customtkinter.CTkLabel(upgradeSectionFrame, text="کد مقصد", font=customtkinter.CTkFont(size=13, weight="bold"))
destCodeInputLabel.grid(row=0, column=0, padx=(2, 13), pady=(0, 2))

originCodeInput = customtkinter.CTkEntry(upgradeSectionFrame, placeholder_text="کد محصول", width=175, height=35)
originCodeInput.grid(row=1, column=1, padx=(10, 10), pady=(3, 5))
originCodeInputLabel = customtkinter.CTkLabel(upgradeSectionFrame, text="کد مبدا", font=customtkinter.CTkFont(size=13, weight="bold"))
originCodeInputLabel.grid(row=0, column=1, padx=(2, 13), pady=(0, 2))

checkBoxFrame = customtkinter.CTkFrame(upgradeSectionFrame, fg_color=('#93bcf5', '#1d4070'))
checkBoxFrame.grid(row=2, padx=(5, 5), pady=(0, 5), columnspan=2)

destChandSherkatiCheckBox = customtkinter.CTkCheckBox(checkBoxFrame, text='چند شرکتی مقصد', checkbox_width=20, checkbox_height=20, onvalue='destChandSherkati')
destChandSherkatiCheckBox.grid(row=2, column=0, padx=(0, 30), pady=(0, 5))

jamekolCheckBox = customtkinter.CTkCheckBox(checkBoxFrame, text='جمع کل', checkbox_width=20, checkbox_height=20, onvalue='jamekol')
jamekolCheckBox.grid(row=2, column=1, padx=(0, 0), pady=(0, 5))

originChandSherkatiCheckBox = customtkinter.CTkCheckBox(checkBoxFrame, text='چند شرکتی مبدا', checkbox_width=20, checkbox_height=20, onvalue='originChandSherkati')
originChandSherkatiCheckBox.grid(row=2, column=2, padx=(0, 0), pady=(0, 5))

# Extension Section
tamdidFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#579af7', '#05306b'))
tamdidFrame.grid(row=1, column=0, padx=(10, 10), pady=(5, 5))

tamdidMotevaliLabel = customtkinter.CTkLabel(tamdidFrame, text="تمدید متوالی", font=customtkinter.CTkFont(size=13, weight="bold"))
tamdidMotevaliLabel.grid(row=0, column=3, padx=(10, 5), pady=(5, 0))

tamdidMotevaliInput = customtkinter.CTkEntry(tamdidFrame, placeholder_text="تعداد سال های متوالی تمدید", width=250, height=35)
tamdidMotevaliInput.grid(row=0, column=2, padx=(5, 5), pady=(5, 5))

tamdidDateLabel = customtkinter.CTkLabel(tamdidFrame, text="تاریخ شروع گارانتی", font=customtkinter.CTkFont(size=13, weight="bold"))
tamdidDateLabel.grid(row=1, column=3, padx=(5, 5), pady=(0, 0))

tamdidDateLabel = customtkinter.CTkLabel(tamdidFrame, text="قیمت تمدید تشویقی", font=customtkinter.CTkFont(size=13, weight="bold"))
tamdidDateLabel.grid(row=2, column=3, padx=(5, 10), pady=(0, 5))

vcmd1 = app.register(on_validate)
tamdidDateInput = customtkinter.CTkEntry(tamdidFrame, placeholder_text="تاریخ", width=250, height=35, validate="key", validatecommand=(vcmd1, "%P"))
tamdidDateInput.grid(row=1, column=2, padx=(5, 5), pady=(0, 5))

# Others Section
othersFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#93bcf5', '#1d4070'))
othersFrame.grid(row=2, column=0, padx=(10, 10), pady=(5, 5))

extPriceLabel = customtkinter.CTkLabel(othersFrame, text="کاربر اضافه", font=customtkinter.CTkFont(size=13, weight="bold"))
extPriceLabel.grid(row=0, column=1, padx=(30, 10), pady=(0, 5))

karbarEzafeInput = customtkinter.CTkEntry(othersFrame, placeholder_text="تعداد کاربر", width=250, height=35)
karbarEzafeInput.grid(row=0, column=0, padx=(10, 10), pady=(5, 5))

tabdilBeGhoflCheckBox = customtkinter.CTkCheckBox(othersFrame, text='تبدیل به قفل', checkbox_width=20, checkbox_height=20, onvalue=495000)
tabdilBeGhoflCheckBox.grid(row=1, column=1, padx=(10, 10), pady=(5, 5))

chandSherkatiCheckBox = customtkinter.CTkCheckBox(othersFrame, text='چند شرکتی', checkbox_width=20, checkbox_height=20, onvalue='chandsherkati')
chandSherkatiCheckBox.grid(row=2, column=1, padx=(10, 10), pady=(0, 5))

# Kits & Modules Section
modulesFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#579af7', '#05306b'))
modulesFrame.grid(row=3, column=0, padx=(10, 10), pady=(5, 5))

modulesLabel = customtkinter.CTkLabel(modulesFrame, text="کیت ها و ماژول ها", font=customtkinter.CTkFont(size=13, weight="bold"))
modulesLabel.grid(row=0, column=0, padx=(10, 10), pady=(5, 0))

modulesList = customtkinter.CTkScrollableFrame(modulesFrame, width=350, height=190, fg_color=('#8cbdff', '#06469e'))
modulesList.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

for idx, kit in enumerate(Kits):
    pticeItems = customtkinter.CTkLabel(modulesList, text=kit, font=customtkinter.CTkFont(size=11))
    pticeItems.grid(row=idx, column=1, sticky='e', padx=(1, 30))

for idx, price in enumerate(modulesPrices):
    modulesPriceList = customtkinter.CTkCheckBox(modulesList, text=price, font=customtkinter.CTkFont(size=11))
    modulesPriceList.grid(row=idx, column=0, sticky='e', padx=5)
    modulesPriceList.bind("<Button-1>", lambda event, p=price: onModulesCheckBoxSelect(p))
    modulesCheckboxes.append(modulesPriceList)

# kit Bargashti dection
bargashtiFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#93bcf5', '#1d4070'))
bargashtiFrame.grid(row=4, column=0, padx=(10, 10), pady=(5, 5))

bargashtiLabel = customtkinter.CTkLabel(bargashtiFrame, text="کیت های برگشتی", font=customtkinter.CTkFont(size=13, weight="bold"))
bargashtiLabel.grid(row=0, column=0, padx=(10, 10), pady=(5, 0))

bargashtiList = customtkinter.CTkScrollableFrame(bargashtiFrame, width=350, height=190, fg_color=('#b3d3ff', '#345c94'))
bargashtiList.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

for idx, kit in enumerate(Kits):
    bargashtiItems = customtkinter.CTkLabel(bargashtiList, text=kit, font=customtkinter.CTkFont(size=11))
    bargashtiItems.grid(row=idx, column=1, sticky='e', padx=(1, 30))

for idx, price in enumerate(modulesPrices):
    bargashtiPriceList = customtkinter.CTkCheckBox(bargashtiList, text=price, font=customtkinter.CTkFont(size=11))
    bargashtiPriceList.grid(row=idx, column=0, sticky='e', padx=5)
    bargashtiPriceList.bind("<Button-1>", lambda event, p=price: onBargashtiCheckBoxSelect(p))
    bargashtiCheckboxes.append(bargashtiPriceList)

# Takhfif Section
# takhfifFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#579af7', '#05306b'))
# takhfifFrame.grid(row=5, column=0, padx=(10, 10), pady=(5, 5))
#
# takhfifPercentInput = customtkinter.CTkEntry(takhfifFrame, placeholder_text="مبلغ تخفیف", width=135, height=35)
# takhfifPercentInput.grid(row=0, column=0, padx=(10, 10), pady=(10, 5))
#
# takhfifPriceInput = customtkinter.CTkEntry(takhfifFrame, placeholder_text="درصد تخفیف", width=135, height=35)
# takhfifPriceInput.grid(row=0, column=1, padx=(10, 10), pady=(10, 5))
#
# takhfifLabel = customtkinter.CTkLabel(takhfifFrame, text="تخفیف", font=customtkinter.CTkFont(size=15, weight="bold"))
# takhfifLabel.grid(row=0, column=2, padx=(30, 10), pady=(10, 10))

# jame kol section
jameKolFrame = customtkinter.CTkFrame(rightFrame, fg_color=('#579af7', '#05306b'))
jameKolFrame.grid(row=6, column=0, padx=(10, 10), pady=(5, 5))

jameKolLabel = customtkinter.CTkLabel(jameKolFrame, text="جمع کل", font=customtkinter.CTkFont(size=25, weight="bold"))
jameKolLabel.grid(row=0, column=2, padx=(156, 156), pady=(65, 15))


# ______________________________________
# |                                     |
# |  BETWEEN RIGHTN AND MIDDLE SECTION  |
# |_____________________________________|

# Title Section

takhfifTitleFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#ffffff', '#000d1f'))
takhfifTitleFrame.grid(row=0, column=0, padx=(5, 5), pady=(10, 3))

takhfifLabel = customtkinter.CTkLabel(takhfifTitleFrame, text="درصد تخفیف", font=customtkinter.CTkFont(size=12, weight="bold"))
takhfifLabel.grid(row=0, column=0, padx=(10, 10), pady=(1, 1))

# Upgrade Takhfif Section
upgradeTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#93bcf5', '#1d4070'))
upgradeTakhfifFrame.grid(row=1, column=0, padx=(5, 5), pady=(5, 5))

upgradeTakhfifInput = customtkinter.CTkEntry(upgradeTakhfifFrame, placeholder_text="تخفیف", width=60, height=35)
upgradeTakhfifInput.grid(row=1, column=0, padx=(10, 10), pady=(10, 15))


# tamdid takhfif section
tamdidTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#579af7', '#05306b'))
tamdidTakhfifFrame.grid(row=2, column=0, padx=(5, 5), pady=(5, 5))

tamdidTakhfifInput = customtkinter.CTkEntry(tamdidTakhfifFrame, placeholder_text="تخفیف", width=60, height=35)
tamdidTakhfifInput.grid(row=0, column=0, padx=(10, 10), pady=(43, 40))


# karbar ezafe section
karbarEzafeTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#93bcf5', '#1d4070'))
karbarEzafeTakhfifFrame.grid(row=3, column=0, padx=(5, 5), pady=(5, 12))

karbarEzafeTakhfifInput = customtkinter.CTkEntry(karbarEzafeTakhfifFrame, placeholder_text="تخفیف", width=60, height=25)
karbarEzafeTakhfifInput.grid(row=0, column=0, padx=(10, 10), pady=(5, 5))

# tabdil be ghofl section
tabdilBeGhoflTakhfifInput = customtkinter.CTkEntry(karbarEzafeTakhfifFrame, placeholder_text="تخفیف", width=60, height=25)
tabdilBeGhoflTakhfifInput.grid(row=1, column=0, padx=(10, 10), pady=(5, 5))

# chand sherkati section
chandSherkatiTakhfifInput = customtkinter.CTkEntry(karbarEzafeTakhfifFrame, placeholder_text="تخفیف", width=60, height=25)
chandSherkatiTakhfifInput.grid(row=2, column=0, padx=(10, 10), pady=(5, 5))

# modules section
modulesTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#579af7', '#05306b'))
modulesTakhfifFrame.grid(row=6, column=0, padx=(5, 5), pady=(0, 0))

modulesTakhfifInput = customtkinter.CTkEntry(modulesTakhfifFrame, placeholder_text="تخفیف", width=60, height=35)
modulesTakhfifInput.grid(row=0, column=0, padx=(10, 10), pady=(10, 220))

# bargashti section
bargashtiTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#93bcf5', '#1d4070'))
bargashtiTakhfifFrame.grid(row=7, column=0, padx=(5, 5), pady=(10, 5))

bargashtiTakhfifInput = customtkinter.CTkEntry(bargashtiTakhfifFrame, placeholder_text="تخفیف", width=60, height=35)
bargashtiTakhfifInput.grid(row=0, column=0, padx=(10, 10), pady=(10, 225))

#jame kol section

jameTakhfifFrame = customtkinter.CTkFrame(betweenRightAndMiddleFrame, fg_color=('#579af7', '#05306b'))
jameTakhfifFrame.grid(row=8, column=0, padx=(5, 5), pady=(5, 5))

jameTakhfifLabel = customtkinter.CTkLabel(jameTakhfifFrame, text='مجموع', text_color='#ffffff')
jameTakhfifLabel.grid(row=0, column=0, padx=(20, 20), pady=(3, 0))
jameTakhfifLabel1 = customtkinter.CTkLabel(jameTakhfifFrame, text='تخفیف ها', text_color='#ffffff')
jameTakhfifLabel1.grid(row=1, column=0, padx=(20, 20), pady=(0, 47))

# jameTakhfifInput = customtkinter.CTkEntry(jameTakhfifFrame, placeholder_text="مجموع", width=60, height=35)
# jameTakhfifInput.grid(row=0, column=0, padx=(10, 10), pady=(5, 65))


# _____________________________
# |                           |
# |  MIDDLE SECTION           |
# |___________________________|

# Title Section
titleAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#ffffff', '#000d1f'))
titleAfterFrame.grid(row=0, column=0, padx=(5, 5), pady=(10, 3))

AfterLabel = customtkinter.CTkLabel(titleAfterFrame, text="بعد از ارزش افزوده", font=customtkinter.CTkFont(size=12, weight="bold"))
AfterLabel.grid(row=0, column=0, padx=(27, 27), pady=(1, 1))

titleBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#ffffff', '#000d1f'))
titleBeforeFrame.grid(row=0, column=1, padx=(5, 5), pady=(10, 3))

BeforeLabel = customtkinter.CTkLabel(titleBeforeFrame, text="قبل از ارزش افزوده", font=customtkinter.CTkFont(size=12, weight="bold"))
BeforeLabel.grid(row=0, column=1, padx=(27, 27), pady=(1, 1))


# Upgrade Price Section
upgradeSectionAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
upgradeSectionAfterFrame.grid(row=1, column=0, padx=(5, 5), pady=(5, 0))

upgradePriceAfter = customtkinter.CTkLabel(upgradeSectionAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=50, text='0')
upgradePriceAfter.grid(row=0, column=0, pady=(5, 5))

upgradeSectionBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
upgradeSectionBeforeFrame.grid(row=1, column=1, padx=(5, 5), pady=(5, 0))

upgradePriceBefore = customtkinter.CTkLabel(upgradeSectionBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=50, text='0')
upgradePriceBefore.grid(row=0, column=0, pady=(5, 5))

# tamdid section
tamdidMotevaliAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidMotevaliAfterFrame.grid(row=2, column=0, padx=(5, 5), pady=(15, 0))

tamdidMotevaliPriceAfter = customtkinter.CTkLabel(tamdidMotevaliAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidMotevaliPriceAfter.grid(row=0, column=0, pady=(5, 5))

tamdidMotevaliBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidMotevaliBeforeFrame.grid(row=2, column=1, padx=(5, 5), pady=(15, 0))

tamdidMotevaliPriceBefore = customtkinter.CTkLabel(tamdidMotevaliBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidMotevaliPriceBefore.grid(row=0, column=0, pady=(5, 5))

tamdidAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidAfterFrame.grid(row=3, column=0, padx=(5, 5), pady=(1, 1))

tamdidPriceAfterLabel = customtkinter.CTkLabel(tamdidAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidPriceAfterLabel.grid(row=0, column=0, pady=(5, 5))

tamdidBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidBeforeFrame.grid(row=3, column=1, padx=(5, 5), pady=(1, 1))

tamdidPriceBeforeLabel = customtkinter.CTkLabel(tamdidBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidPriceBeforeLabel.grid(row=0, column=0, pady=(5, 5))

tamdidTashvighiAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidTashvighiAfterFrame.grid(row=4, column=0, padx=(5, 5), pady=(0, 15))

tamdidTashvighiPriceAfterLabel = customtkinter.CTkLabel(tamdidTashvighiAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidTashvighiPriceAfterLabel.grid(row=0, column=0, pady=(5, 5))

tamdidTashvighiBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
tamdidTashvighiBeforeFrame.grid(row=4, column=1, padx=(5, 5), pady=(0, 15))

tamdidTashvighiPriceBeforeLabel = customtkinter.CTkLabel(tamdidTashvighiBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=25, text='0')
tamdidTashvighiPriceBeforeLabel.grid(row=0, column=0, pady=(5, 5))

# karbar ezafe section
karbarEzafeAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
karbarEzafeAfterFrame.grid(row=5, column=0, padx=(5, 5), pady=(0, 1))

karbarEzafePriceAfter = customtkinter.CTkLabel(karbarEzafeAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
karbarEzafePriceAfter.grid(row=0, column=0, pady=(5, 5))

karbarEzafeBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
karbarEzafeBeforeFrame.grid(row=5, column=1, padx=(5, 5), pady=(0, 1))

karbarEzafePriceBefore = customtkinter.CTkLabel(karbarEzafeBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
karbarEzafePriceBefore.grid(row=0, column=0, pady=(5, 5))

# tabdil be ghofl section
tabdilBeGhoflAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
tabdilBeGhoflAfterFrame.grid(row=6, column=0, padx=(5, 5), pady=(0, 1))

tabdilBeGhoflPriceAfter = customtkinter.CTkLabel(tabdilBeGhoflAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
tabdilBeGhoflPriceAfter.grid(row=0, column=0, pady=(5, 5))

tabdilBeGhoflBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
tabdilBeGhoflBeforeFrame.grid(row=6, column=1, padx=(5, 5), pady=(0, 1))

tabdilBeGhoflPriceBefore = customtkinter.CTkLabel(tabdilBeGhoflBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
tabdilBeGhoflPriceBefore.grid(row=0, column=0, pady=(5, 5))

# chand sherkati section
chandSherkatiAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
chandSherkatiAfterFrame.grid(row=7, column=0, padx=(5, 5), pady=(0, 5))

chandSherkatiPriceAfter = customtkinter.CTkLabel(chandSherkatiAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
chandSherkatiPriceAfter.grid(row=0, column=0, pady=(5, 5))

chandSherkatiBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
chandSherkatiBeforeFrame.grid(row=7, column=1, padx=(5, 5), pady=(0, 5))

chandSherkatiPriceBefore = customtkinter.CTkLabel(chandSherkatiBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=25, text='0')
chandSherkatiPriceBefore.grid(row=0, column=0, pady=(5, 5))

# modules section
modulesAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
modulesAfterFrame.grid(row=8, column=0, padx=(5, 5), pady=(7, 10))

modulesPriceAfter = customtkinter.CTkLabel(modulesAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=35, text='0')
modulesPriceAfter.grid(row=0, column=0, pady=(5, 5))

modulesBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
modulesBeforeFrame.grid(row=8, column=1, padx=(5, 5), pady=(7, 10))

modulesPriceBefore = customtkinter.CTkLabel(modulesBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=35, text='0')
modulesPriceBefore.grid(row=0, column=0, pady=(5, 5))

# bargashti section
bargashtiAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
bargashtiAfterFrame.grid(row=9, column=0, padx=(5, 5), pady=(222, 10))

bargashtiPriceAfter = customtkinter.CTkLabel(bargashtiAfterFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=35, text='0')
bargashtiPriceAfter.grid(row=0, column=0, pady=(5, 5))

bargashtiBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#93bcf5', '#1d4070'))
bargashtiBeforeFrame.grid(row=9, column=1, padx=(5, 5), pady=(222, 10))

bargashtiPriceBefore = customtkinter.CTkLabel(bargashtiBeforeFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color=('#084175', '#ffffff'), width=150, height=35, text='0')
bargashtiPriceBefore.grid(row=0, column=0, pady=(5, 5))


# takhfif section
takhfifFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
takhfifFrame.grid(row=10, column=0, columnspan=2, padx=(5, 5), pady=(230, 0))

takhfifPrice = customtkinter.CTkLabel(takhfifFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=260, height=25, text='0')
takhfifPrice.grid(row=0, column=0, pady=(5, 5))

#jame kol section
jameKolAfterFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
jameKolAfterFrame.grid(row=11, column=0, padx=(5, 5), pady=(15, 5))

jameKolPriceAfter = customtkinter.CTkLabel(jameKolAfterFrame, font=customtkinter.CTkFont(size=20, weight="bold"), text_color=('#ffffff'), width=150, height=40, text='0')
jameKolPriceAfter.grid(row=0, column=0, pady=(5, 5))

jameKolBeforeFrame = customtkinter.CTkFrame(middleFrame, fg_color=('#579af7', '#05306b'))
jameKolBeforeFrame.grid(row=11, column=1, padx=(5, 5), pady=(15, 5))

jameKolPriceBefore = customtkinter.CTkLabel(jameKolBeforeFrame, font=customtkinter.CTkFont(size=20, weight="bold"), text_color=('#ffffff'), width=150, height=40, text='0')
jameKolPriceBefore.grid(row=0, column=0, pady=(5, 5))


# _____________________________
# |                           |
# |  LEFT SECTION             |
# |___________________________|

# about sidebar
holooLogo = customtkinter.CTkImage(light_image=Image.open("/Users/omid/Coding/Learning Projects/Python learning/SSP/Holoo-500.png"), dark_image=Image.open("/Users/omid/Coding/Learning Projects/Python learning/SSP/Holoo-500.png"), size=(90, 30))
serajLogo = customtkinter.CTkImage(light_image=Image.open("/Users/omid/Coding/Learning Projects/Python learning/SSP/logo-h.png"), dark_image=Image.open("/Users/omid/Coding/Learning Projects/Python learning/SSP/logo-h.png"), size=(100, 30))

animated_panel = SlidePanel(app, 1, 0.6)

aboutApp = customtkinter.CTkLabel(animated_panel, font=customtkinter.CTkFont(size=20, weight="bold"), text='SSP Price Utility', wraplength=380, justify='center').pack(expand=True, fill='both', padx=2, pady=10, side='top')

aboutApp = customtkinter.CTkLabel(animated_panel, font=customtkinter.CTkFont(size=15, weight="bold"), text='نرم افزار پیش رو جهت تسهیل محاسبه و یکپارچگی قیمت های نرم افزارهای مختلف هلو و جلوگیری از خطای انسانی در هنگام محاسبات فروش, توسط تیم تحقیق و توسعه مجموعه سراج سبز پارتیکان آماده سازی و تولید شده و در اختیار کاربران قرار گرفته است. ', wraplength=380, justify='center').pack(expand=True, fill='both', padx=2, pady=10, side='top')

holooLogo_label = customtkinter.CTkLabel(animated_panel, text='', image=holooLogo).pack(expand=True, fill='both', padx=10, pady=10, side='top')

serajLogo_label = customtkinter.CTkLabel(animated_panel, text='', image=serajLogo).pack(expand=True, fill='both', padx=10, pady=10, side='top')

customtkinter.CTkLabel(animated_panel, font=customtkinter.CTkFont(size=10, weight="bold"), text='''سراج سبز پارتیکان 
SSP Price Calculation Utility
created and developed by: Omid Azad
Date created: March 27th 2024
Ver 1.1''', text_color='#04b0db', justify='center').pack(expand=True, fill='both', padx=2, pady=10, side='bottom')

infoFrame = customtkinter.CTkFrame(leftFrame, fg_color=('#93bcf5', '#1d4070'))
infoFrame.grid(row=0, padx=(5, 5), pady=(10, 10))

originLabel = customtkinter.CTkLabel(infoFrame, text='مبدا', font=customtkinter.CTkFont(size=15, weight="bold"))
originLabel.grid(row=0, column=0, padx=(150, 150), pady=(5, 0))
originOutput = customtkinter.CTkLabel(infoFrame, font=customtkinter.CTkFont(size=14, weight="bold"), text_color='#129900', width=150, height=40, text='')
originOutput.grid(row=1, column=0, padx=(5, 5), pady=(0, 5))

destLabel = customtkinter.CTkLabel(infoFrame, text='مقصد', font=customtkinter.CTkFont(size=15, weight="bold"))
destLabel.grid(row=2, column=0, padx=(10, 10), pady=(5, 0))
destOutput = customtkinter.CTkLabel(infoFrame, font=customtkinter.CTkFont(size=14, weight="bold"), text_color='#129900', width=150, height=40, text='')
destOutput.grid(row=3, column=0, padx=(5, 5), pady=(0, 5))

sanavatFrame =  customtkinter.CTkFrame(leftFrame, fg_color=('#93bcf5', '#1d4070'))
sanavatFrame.grid(row=1, padx=(5, 5), pady=(0, 5))

sanavatLabel = customtkinter.CTkLabel(sanavatFrame, text='', width=80, font=customtkinter.CTkFont(size=15))
sanavatLabel.grid(row=0, column=0, padx=(20, 20), pady=(5, 5))

sanavatTitle = customtkinter.CTkLabel(sanavatFrame, text='سنوات تمدید', font=customtkinter.CTkFont(size=15, weight="bold"))
sanavatTitle.grid(row=0, column=1, padx=(100, 20), pady=(5, 5))

# helpFrame = customtkinter.CTkFrame(leftFrame, fg_color=('#b1cdf0', '#00345c'))
# helpFrame.grid(row=5, padx=(5, 5), pady=(10, 5))
#
# aboutApp = customtkinter.CTkLabel(helpFrame, text='''برای تجربه کاربری بهتر و سریعتر می توانید از راهنمای زیر استفاده کنید:
#
# - با وارد کردن کد مبدا و مقصد در قسمت اول میتوانید مابه التفاوت قیمت ارتقا کدهای مختلف را محاسبه کنید.
#
# - اگر در قسمت کد مبدا چیزی وارد نکنید و در قسمت کد مقصد کد نرم افزار را وارد کنید با فشردن دکمه محاسبه قیمت فروش کد مورد نظر را بدست خواهید آورد.
#
# - در صورت انجام تمدید متوالی توسط کاربران هلو, میتوانید تعداد سالهای متوالی تمدید را وارد کنید تا تخفیف محاسبه شود.
#
# - با وارد کردن تاریخ شروع گارانتی نرم افزار هلو (بدون اعشار) نرم افزار قیمت تمدید نرم افزار هلو را بر اساس مدت زمان سپری شده از پایان گارانتی و سنوات تعلق گرفته محاسبه می کند.
#
# - در صورت داشتن کاربر اضافه تعداد کاربرهای اضافه شده به نرم افزار هلو را وارد کنید.
#
# - درصورتی که تمایل به تبدیل قفل سخت افزاری به کارت فعال سازی هوشمند دارید تیک این قسمت را بزنید.
#
# - در صورتی که نرم افزار مورد نظر دارای کیت چند شرکتی است تیک را بزنید, در صورت تمدید تیک را بزنید.
#
# - برای اضافه کردن کیت ها و ماژول ها موارد مورد نظر را از لیست انتخاب کنید.
#
# - در صورت داشتن کیت برگشتی, موارد را از لیست انتخاب کنید.
#
# - درصد و مبلغ تخفیف را می توانید در این قسمت وارد کنید.
# ''', wraplength=320, justify='right')
# aboutApp.grid(row=0, padx=(10, 10), pady=(10, 10))

khadamatFrame = customtkinter.CTkFrame(leftFrame, fg_color=('#579af7', '#05306b'))
khadamatFrame.grid(row=3, column=0, padx=(10, 10), pady=(40, 5))

khadamatLabel = customtkinter.CTkLabel(khadamatFrame, text="خدمات و کارشناسی", font=customtkinter.CTkFont(size=13, weight="bold"))
khadamatLabel.grid(row=0, column=0, padx=(10, 10), pady=(5, 0))

khadamatList = customtkinter.CTkScrollableFrame(khadamatFrame, width=285, height=260, fg_color=('#8cbdff', '#06469e'))
khadamatList.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

for idx, kit in enumerate(khadamat):
    pticeItems = customtkinter.CTkLabel(khadamatList, text=kit, font=customtkinter.CTkFont(size=13))
    pticeItems.grid(row=idx, column=1, sticky='e', padx=(1, 0), columnspan=1)

for idx, price in enumerate(khadamatPrices):
    khadamatPriceList = customtkinter.CTkCheckBox(khadamatList, text=price, font=customtkinter.CTkFont(size=13))
    khadamatPriceList.grid(row=idx, column=0, sticky='w', padx=(10, 25))
    khadamatPriceList.bind("<Button-1>", lambda event, p=price: onKhadamatCheckBoxSelect(p))
    khadamatCheckBoxes.append(khadamatPriceList)

KhadamatTakhfifFrame = customtkinter.CTkFrame(khadamatFrame, fg_color=('#8cbdff', '#06469e'), width=310, height=60)
KhadamatTakhfifFrame.grid(row=3, column=0, padx=(5, 5), pady=(0, 10))

khadamatTakhfifPercent = customtkinter.CTkEntry(KhadamatTakhfifFrame, placeholder_text='تخفیف درصدی', height=35)
khadamatTakhfifPercent.grid(row=0, column=0, padx=(5, 10), pady=(10, 10))

khadamatTakhfifAmount = customtkinter.CTkEntry(KhadamatTakhfifFrame, placeholder_text='تخفیف مبلغی', height=35)
khadamatTakhfifAmount.grid(row=0, column=1, padx=(10, 5), pady=(10, 10))

KhadamatPriceFrame = customtkinter.CTkFrame(khadamatFrame, fg_color=('#8cbdff', '#06469e'), width=310, height=60)
KhadamatPriceFrame.grid(row=4, column=0, padx=(5, 5), pady=(0, 10))

khadamatPriceFrameinFrame = customtkinter.CTkFrame(KhadamatPriceFrame, fg_color=('#579af7', '#05306b'))
khadamatPriceFrameinFrame.grid(row=0, column=0, padx=(5, 5), pady=(10, 10))

khadamatPriceLabel = customtkinter.CTkLabel(khadamatPriceFrameinFrame, font=customtkinter.CTkFont(size=15, weight="bold"), text_color='#ffffff', width=150, height=35, text='0')
khadamatPriceLabel.grid(row=0, column=0, pady=(5, 5))

tamdidForKhadamatCheckBox = customtkinter.CTkCheckBox(KhadamatPriceFrame, text='تمدید ندارد', checkbox_width=20, checkbox_height=20, onvalue=35)
tamdidForKhadamatCheckBox.grid(row=0, column=1, padx=(40, 10), pady=(5, 10))

# calculate button
calculateButton = customtkinter.CTkButton(leftFrame, command=calculate, hover_color="#00b5ac", text='محاسبه', font=customtkinter.CTkFont(size=15, weight="bold"), width=250, height=50, fg_color='#47c159', border_width=2, text_color=("gray10", "#003024"))
calculateButton.grid(row=7, column=0, padx=(10, 10), pady=(10, 10))

# reset button
resetButton = customtkinter.CTkButton(leftFrame, command=reset, hover_color="#c44f4d", text='پاک کردن فرم', font=customtkinter.CTkFont(size=15, weight="bold"), width=250, height=50, fg_color='#f63051', border_width=2, text_color=("gray10", "#DCE4EE"))
resetButton.grid(row=8, column=0, padx=(10, 10), pady=(0, 60))

# appearance button section
appearance_mode_label = customtkinter.CTkLabel(leftFrame, text="Appearance Mode:", anchor="w")
appearance_mode_label.grid(row=9, column=0, padx=(10, 5), pady=(10, 0), sticky='w')
appearance_mode_menu = customtkinter.CTkOptionMenu(leftFrame, command=change_appearance_mode, values=["Light", "Dark", "System"])
appearance_mode_menu.grid(row=10, column=0, padx=(10, 5), pady=(5, 5), sticky='w')

# about button
about_btn = customtkinter.CTkButton(leftFrame, text='About', command=animated_panel.animate)
about_btn.grid(row=11, column=0, padx=(10, 5), pady=(5, 10), sticky='w')

app.mainloop()
