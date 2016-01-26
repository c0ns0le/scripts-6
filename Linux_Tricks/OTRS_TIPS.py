http://hirantha.wikidot.com/setting-up-nginx-for-otrs
http://supportex.net/blog/2011/11/migrating-otrs-apache-nginx/



# 1. lock vs unlock
當你收到 ticket 時，同一群(Quene)負責的人第一個去點 ticket 的人 系統會將 Ticket locked 住給他
如果要改變 ticket 處理的人，請原先的人將 ticket 給 unlock ，才可以讓另一個人將 ticket locked

2. close ticket vs close successful
close ticket : 如果這個 ticket 認為不用處理 請選 close 關掉，為了防止吃單 系統會強迫你註記
close successful : 如果 ticket 處理完畢，在回覆時請選擇 close successful 將單子結束

For 管理 otrs

0. 可以看到 ticket
ro 一定要有, 在 otrs 裡 rw 並不包含 ro

1. 改 ticket 的 queue
最基本要有 owner , move_into 兩個權限，先改 owner 再改 queue

2. 結案通知
在 otrs , Ticket 結束只會發給原本 new ticket 的人
如果希望同個群組都要收到需要自訂 Admin / Notification (Event)
Event 要選 ArticleSend, 收件者則請自訂

1. 不要顯示已經關閉的 Ticket
在 sysconfig 找 ShowClosedTickets 並將 DataSelected 設置為 0

2. 改寄件者名稱
在 vi /opt/otrs/Kernel/Config.pm
$Self->{NotificationSenderName} = “Help Deskt"

3. 中文報表
yum install fonts-chinese
cd /usr/lib/perl5/site_perl/5.8.8/PDF/API2/fonts
ln -s /usr/share/fonts/zh_TW/TrueType/bsmi00lp.ttf
ln -s /usr/share/fonts/chinese/TrueType/ukai.ttf
ln -s /usr/share/fonts/chinese/TrueType/uming.ttf

在 sysconfig 的 Config Options: Framework -> Core\dotsPDF
換掉 fonts


OTRS performace

六月 22, 2010 發表留言

vi /opt/otrs/scripts/apache2-perl-startup.pl

將 Apache::DBI 那一行註解取消掉
ex.
use Apache::DBI ();
Apache::DBI->connect_on_init(‘DBI:mysql:otrs’, ‘otrs’, ‘password’);
use DBI ();
use DBD::mysql ();


OTRS 缺點

六月 8, 2010 發表留言

OTRS 缺點 或是無有提供的功能 (整理中)

OTRS 目前缺點有
1. Queue 無法和 Sub Quene 連動
OTRS 的 Quene 可以對應一個群組 使問題由相關人員去回覆
如 User 指定 To 給 Windows , 我可以設定負責 Windows 的人成為一個 Group 去回覆 Windows 的問題

但問題是 如果我想要做更細項的分類在 Sub Queue 則是無意義的，因為 Sub Queue 無法和上一層的 Queue 連動

2. 無法讓回答 ticket 的服務人員自訂常用回覆
雖然 OTRS 可以允許自訂常用回覆 但這只有 OTRS 管理者才能自訂 不夠方便

