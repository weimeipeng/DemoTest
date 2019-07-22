#定义一个类
class DemoClass:

    def __init__(self):
        print("初始化一个类")

    def output(self,text):
        print("您刚才输入的是%s" %text)

    def output_none(self):
        print("我不能传递参数")


class childDemoClass(DemoClass):
    # def __init__(self):
    #     print("我是子类")
    
    def output_child(self):
        print("子类里面的输出函数")

if __name__ == '__main__':
    # demo_obj = DemoClass()

    # demo_obj.output("马云")
    # demo_obj.output_none()
    # demo_obj1 = DemoClass()

    # demochild = childDemoClass()
    # demochild.output("健林")
    # demochild.output_child()
    
    squ_tple =(1,2,3,4,5,6)

    #创建迭代器

    seq_it = iter(squ_tple)

    print("第1个元素：%s" %next(seq_it))
    print("第2个元素：%s" %next(seq_it))
    print("第3个元素：%s" %next(seq_it))

