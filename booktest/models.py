from django.db import models
# 自定义管理器 加了过滤器
class BookInfoManage(models.Manager):
    def get_queryset(self):
        return  super(BookInfoManage,self).get_queryset().filter(isDelete=False)
    # 在管理器里定义 方法2 推荐这种方案
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcomment=0
        b.isDelete=False
        return b

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    # db_column 自定义字段名称
    bpub_date =models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    # 元选项
    class Meta:
        db_table = 'bookinfo'
    # 管理器:模型进行数据库的查询操作的接口
    ''' 
    定义了管理器默认的管理器就失效了
    就不能用object.all()了
    管理器是模型类的属性
    '''
    books_guanliqi1 = models.Manager()
    books_guanliqi2 =BookInfoManage()
    #定义一个类方法的话  就可以快速创建对象 方法1
    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcomment=0
        b.isDelete=False
        return b
class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=1000)
    isDelete =models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)


class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',null=True,blank=True)