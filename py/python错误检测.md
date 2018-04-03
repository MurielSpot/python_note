## 判断对象类型，不对则报错

isinstance() 方法
- 语法：<br/>
  isinstance(object, classinfo)
- 参数<br/>
  object -- 实例对象。<br/>
  classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
- 返回值<br/>
  如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。

isinstance() 与 type() 区别：<br/>
type() 不会认为子类是一种父类类型，不考虑继承关系。<br/>
isinstance() 会认为子类是一种父类类型，考虑继承关系。
