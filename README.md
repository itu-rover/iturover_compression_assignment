<img src="media/iturover.png" width="256" height="225" />

# ITU Rover Compression Assignment
Size verdiğimiz **bz2_node** isimli node, bz2 (Burrows–Wheeler) algoritmasıyla sıkıştırılmış bir veriyi on altılı sayı sisteminde (hexadecimal) "/bz2_message" topic'i üzerinde yayınlamaktadır.


Sırasıyla, 
* Yayınlanan topic'i dinlemeniz,
* Verinin sıkıştırılmamış hâlindeki en çok tekrar eden karakteri bulun.
* Daha sonra bu karakterin ASCII tablosunda denk geldiği sayıyı [std_msgs/Char](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/Char.html) mesaj türünde **"/solution"** isimli topic'e publishlemeniz beklenmektedir.

### Örnek:

Size verdiğimiz scriptte verinin sıkıştırılmamış hâli "abcdddef" olsun.

"abcdddef" bz2 algoritması vasıtasıyla compress edildiğinde çıktı b"BZh91AY&SY\x13\x84\x11\xdd\x00\x00\x00\x01\x00?\x00 \x00!\x80\x0c\x03')\xdc]\xc9\x14\xe1B@N\x10Gt" oluyor. Bu verinin on altılı sayı sisteminde karşılığı ise "425a6839314159265359138411dd00000001003f00200021800c032729dc5dc914e142404e104774" oluyor. "/bz2_message" topic'i üzerinden en son elde ettiğimiz on altılı sayı sistemi formunda [std_msgs/String](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/String.html) türünde yayınlanıyor.

Sizden yapmanızı istediğimiz şey, "425a6839314159265359138411dd00000001003f00200021800c032729dc5dc914e142404e104774" ifadesini sıkıştırılmamış hâline (verdiğimiz örnekte "abcddef") getirmek. Ardından bu verinin en çok tekrar eden karakterini (örneğimizde 'd') ve bu karakterin ascii tablosundaki karşılığını (Örn: d karakteri için 100) bulup [std_msgs/Char](http://docs.ros.org/en/noetic/api/std_msgs/html/msg/Char.html) mesaj tipinde publislemeniz istenmektedir.

## ASCII Table
![ASCII Table](/media/ascii-table.png)

