import pymysql
import pymssql
from decimal import Decimal
from common.logger import Log
from common import read_config


class ConnectMySqL:
    """
    连接mysql数据库封装

    """

    def __init__(self):
        self.log = Log()
        """判断是否连接成功"""
        try:
            self.conn = pymysql.connect(host=read_config.MySQL_host, database=read_config.MySQL_database,
                                        user=read_config.MySQL_user,
                                        password=read_config.MySQL_pwd, port=int(read_config.MySQL_port),
                                        charset='utf8')
            self.log.info('数据库连接成功')
        except Exception as e:
            self.log.error('数据库链接异常! {}'.format(e))

    def execute_sql(self, sql, dict_type=False, num=1):
        """返回查询结果集
            sql: 执行的sql语句；
            dict_type: 是否返回的数据是字典类型；
            num： 返回的数据是一个还是多个
        """
        if dict_type:  # 返回数据字典类型
            cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        else:
            cur = self.conn.cursor()
        try:
            with cur as cur:
                cur.execute(sql)  # 执行sql
            if 'delete' in sql:
                self.conn.commit()  # 提交
            else:
                if num == 1:  # 返回一条数据
                    data = cur.fetchone()
                    if dict_type:
                        return data
                    else:
                        return data[0]
                else:  # 返回多条数据
                    data_str = ''
                    data = cur.fetchall()
                    if dict_type:
                        return data
                    else:
                        for i in data:
                            for j in i:
                                data_str += str(j) + ','  # 拼接返回数据
                        return data_str
        except Exception as e:
            self.conn.rollback()
            self.log.error('执行SQL语句出现异常：{}'.format(e))
            return None

    def __del__(self):
        self.conn.close()


class ConnectSqLServer:
    """连接SqlServer数据库封装"""

    def __init__(self):
        self.log = Log()
        """判断是否连接成功"""
        try:
            self.conn = pymssql.connect(host=read_config.SQLServer_host, user=read_config.SQLServer_user,
                                        password=read_config.SQLServer_pwd, port=read_config.SQLServer_port,
                                        database='sharebuy_test', charset='utf8')
            self.log.info('数据库连接成功')
        except Exception as e:
            self.log.error('数据库链接异常! {}'.format(e))

    def execute_sql(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        """
        cur = self.conn.cursor()
        with cur as cur:
            try:
                cur.execute(sql)
            except Exception as e:
                self.log.error('执行SQL语句出现异常：{}'.format(e))
                return False
            else:
                if 'select' in sql:  # 查询
                    resList = cur.fetchall()
                    return resList
                else:
                    self.conn.commit()


def decimal_format(self, money):
    """改变数据库数据编码格式"""
    pay_money = Decimal(money).quantize(Decimal('0.00'))
    return pay_money


if __name__ == '__main__':
    r = ConnectMySqL()
    data = r.execute_sql("select ct.id from customer_tbl as ct ;", num=2)
    data = data.split(',')
